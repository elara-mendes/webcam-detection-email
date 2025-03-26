# Detecção de Objetos e Envio por Email

[English Ver.](README_en.md)

Este projeto utiliza **YOLO** para detectar objetos em imagens capturadas pela webcam e envia as imagens detectadas por e-mail automaticamente.

## 🚀 Tecnologias Utilizadas
- Python 3.10 (Conda)
- OpenCV
- YOLO (You Only Look Once)
- Threading
- Queue
- Glob

## 📌 Funcionalidades
- Captura imagens da webcam.
- Detecta objetos utilizando **YOLO**.
- Salva imagens quando objetos são detectados.
- Envia as imagens capturadas por e-mail.
- Gerencia a fila de envio de e-mails com **threads**.
- Exclui imagens antigas para otimizar o armazenamento.

## 📂 Estrutura do Projeto
```
/
├── images/              # Diretório onde as imagens detectadas são armazenadas
├── utils/
│   ├── send_mail.py         # Script para envio de e-mails 
│   ├── get_webcam_info.py   # Script para identificar qual a sua webcam
├── face_detection.py    # Script para detecção facial sem envio de e-mails atrelado
├── main.py              # Script principal do projeto
├── yolo11n.pt           # Modelo YOLO pré-treinado
└── README.md            # Documentação do projeto
```

## 🛠️ Como Usar
1. **Crie um ambiente Conda e instale as dependências:**
   ```bash
   conda create -n obj_detection python=3.10 -y
   conda activate obj_detection
   pip install opencv-python ultralytics
   ```
2. **Execute o script principal:**
   ```bash
   python main.py
   ```
3. **Pressione 'q' para sair do programa.**

## 📧 Configuração de Email
Para permitir o envio automático de imagens, edite `utils/send_mail.py` com suas credenciais SMTP.

## ⚠️ Requisitos
- Python 3.10 (Conda)
- Webcam conectada
