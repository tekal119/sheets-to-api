import os
from flask import Flask

app = Flask(__name__)
import requests
@app.route('/')
# Configuración del bot de Telegram
TELEGRAM_BOT_TOKEN == '7291475602:AAEKIkIrlG-RUWyiGsm3u8jzsFZucute3yg'
TELEGRAM_CHAT_ID = '5278452082'

def enviar_a_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def home():
    return "API funcionando correctamente 🚀"
# Nueva ruta para recibir datos desde Google Sheets y enviarlos a Telegram
@app.route('/actualizar_tareas', methods=['POST'])
def actualizar_tareas():
    data = request.get_json()
    print("Datos recibidos:", data)  # Esto ayuda a depurar si llegan correctamente
    
    # Extraer datos y enviarlos a Telegram
    mensaje = f"Nueva tarea actualizada:\nFila: {data['fila']}\nDatos: {data['datos']}"
    enviar_a_telegram(mensaje)
    
    return jsonify({"status": "Recibido", "data": data})
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Usa el puerto que Render asigna
    app.run(host='0.0.0.0', port=port)
