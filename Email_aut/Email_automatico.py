import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# CONFIGURAÇÕES
EMAIL_REMETENTE = ""
SENHA_APP = ""
EMAIL_DESTINO = input("email: ")

CAMINHO_ARQUIVO = ""

# CRIA O EMAIL
msg = MIMEMultipart()
msg["From"] = EMAIL_REMETENTE
msg["To"] = EMAIL_DESTINO
msg["Subject"] = ""

msg.attach(MIMEText(''''''))

# ANEXO
with open(CAMINHO_ARQUIVO, "rb") as arquivo:
    parte = MIMEBase("application", "octet-stream")
    parte.set_payload(arquivo.read())

encoders.encode_base64(parte)
nome_arquivo = os.path.basename(CAMINHO_ARQUIVO)

parte.add_header(
    "Content-Disposition",
    f'attachment; filename="{nome_arquivo}"'
)

msg.attach(parte)

# ENVIO
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(EMAIL_REMETENTE, SENHA_APP)
server.send_message(msg)
server.quit()

print("✅ E-mail enviado com sucesso!")
