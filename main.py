from dotenv import load_dotenv
load_dotenv

import os
from mcp.server.fastmcp import FastMCP

import smtplib
from email.message import EmailMessage
import mimetypes


mcp = FastMCP("mail-mcp")


DESTINATION = os.environ.get('DESTINATION', 'me@local.local')
ACCOUNT = os.environ.get('ACCOUNT', 'me@local.local')
PASSWORD = os.environ.get('APPPASS', '123')


@mcp.tool()
def send_mail_local(subject:str, message:str, files:list[str]=[]):
    '''
    De uso local, en caso de que no sea posible enviar al servidor de correos principal.
    subject: asunto del correo
    message: mensaje
    files: lista de rutas hacia los archivos, por defecto []
    '''
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = ACCOUNT
    msg["To"] = DESTINATION

    msg.set_content(message)
    for i in files:
        if not os.path.exists(i):
            continue
        tipo_mime, _ = mimetypes.guess_type(i)
        tipo_mime, subtipo = tipo_mime.split("/") if tipo_mime else ("application","octec-stream")
        with open(i, 'rb') as file:
            msg.add_attachment(
                file.read(),
                maintype=tipo_mime,
                subtype = subtipo,
                filename = os.path.basename(i)
            )

    with smtplib.SMTP('localhost', 1025) as smtp:
        smtp.send_message(msg)

if __name__ == "__main__":
    mcp.run(transport='stdio')
