from libreria_bot_telegram_monitor_web import monitor_website, check_port_status, send_telegram_message

#  Configuración
url = "https://www.uabjb.edu.bo/"  # URL a monitorear
interval =   10 # Intervalo en segundos
telegram_token = "" # tu token
telegram_chat_id = "" # tu id de chat

# Iniciamos el monitor
monitor_website(url, interval, telegram_token, telegram_chat_id)



