import asyncio
import requests

def check_port_status(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return "OK"
        else:
            return f"HTTP {response.status_code} {response.reason}"
    except requests.exceptions.ConnectionError:
        return "El puerto no responde o está cerrado"
    except requests.exceptions.Timeout:
        return "El puerto responde pero el servicio web no"

async def send_telegram_message(token, chat_id, message): # función asincrona para ejecutar instrucciones de fondo, permitiendo continuar las acciones mientras por detrás se completan
    import telegram

    bot = telegram.Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=message) # pausa la ejecucion de la funcion asincrona

def monitor_website(url, interval, telegram_token, telegram_chat_id):
    import time

    while True:
        result = check_port_status(url) # el asyncio espera a que se ejecute el resultado para proseguir
        if result != "OK":
            message = f"Fallo en la web {url}: {result}"
            asyncio.run(send_telegram_message(telegram_token, telegram_chat_id, message)) # para que ejecute un metodo asincrono
        time.sleep(interval)

        