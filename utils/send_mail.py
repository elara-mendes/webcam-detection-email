import smtplib
import os, imghdr
from email.message import EmailMessage

YOUR_EMAIL = "elaradomingos@gmail.com"
APP_PASSWORD = os.getenv("GMAIL_PASSWORD") # Your Gmail Password
RECEIVER_EMAIL = "elaradomingos@gmail.com"


def email_send(image):
    email_message = EmailMessage()
    email_message["Subject"] = "Someone's here!"
    email_message.set_content("Take a look at the image")

    with open(image, "rb") as image_file:
        img = image_file.read()

    email_message.add_attachment(img, maintype="image", subtype=imghdr.what(None, img))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(YOUR_EMAIL, APP_PASSWORD)
    gmail.sendmail(YOUR_EMAIL, RECEIVER_EMAIL, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    email_send(image=r"")
