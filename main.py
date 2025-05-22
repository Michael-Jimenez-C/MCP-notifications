from dotenv import load_dotenv
load_dotenv

import os
from mcp.server.fastmcp import FastMCP
from modules.email import send_mail_to_local

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



if __name__ == "__main__":
    mcp.run(transport='stdio')
