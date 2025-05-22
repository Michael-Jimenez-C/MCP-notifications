import os
import requests

BOT_TOKEN = os.environ.get('BOT_TOKEN')

def get_users():
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
    res = requests.get(url).json()

    CHAT_IDs = {
        r['message']['chat']['id']
        for r in res.get('result', [])
        if 'message' in r and 'chat' in r['message']
    }
    return CHAT_IDs

def notificar_telegram(mensaje):
    CHAT_IDs = get_users()
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = None
    for chat_id in CHAT_IDs:
        data = {
            "chat_id": chat_id,
            "text": mensaje,
            "parse_mode": "Markdown",
        }
        response = requests.post(url, data=data)
    if response:
        return response.ok
    return False

def enviar_archivo(files = []):
    CHAT_IDs = get_users()
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    response = None
    for file in files:
        attachment = {}
        if not os.path.exists(file):
            return False
        attachment['document'] = open(file,'rb')
        for chat_id in CHAT_IDs:
            data = {
                "chat_id": chat_id
            }
            response = requests.post(url, data=data, files=attachment)
    if response:
        return response.ok
    return False