from dotenv import load_dotenv
load_dotenv

from mcp.server.fastmcp import FastMCP
from modules.email import send_mail_to_local
from modules.telegram import notificar_telegram, enviar_archivo

mcp = FastMCP("mail-mcp")


@mcp.tool()
async def send_mail_local(subject:str, message:str, files:list[str]=[]):
    '''
    De uso local, en caso de que no sea posible enviar al servidor de correos principal.
    subject: asunto del correo
    message: mensaje
    files: lista de rutas hacia los archivos, por defecto []
    '''
    return send_mail_to_local(subject, message, files)

@mcp.tool()
async def send_telegram_message(message:str):
    '''
    Envia un mensaje a los usuarios de telegram
    message: mensaje
    '''
    return notificar_telegram(message)

@mcp.tool()
async def send_telegram_file(files:list[str]=[]):
    '''
    Envia un archivo a los usuarios de telegram
    files: lista de rutas hacia los archivos, por defecto []
    '''
    return enviar_archivo(files)

if __name__ == "__main__":
    mcp.run(transport='stdio')
