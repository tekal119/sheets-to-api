import os
from flask import Flask, request, jsonify
import requests  # Asegurándome de que 'requests' esté importado correctamente

app = Flask(__name__)

# Configuración del bot de Telegram
TELEGRAM_BOT_TOKEN = "7291475602:AAEKIkIrlG-RUWyiGsm3u8jzsFZucute3yg"
TELEGRAM_CHAT_ID = '5278452082'

def enviar_a_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()  # Retornar la respuesta de la API para ver si hubo éxito
print(f"Servidor corriendo en http://0.0.0.0:{port}")

@app.route('/')
def home():
    return "API funcionando correctamente 🚀"

# Nueva ruta para recibir datos desde Google Sheets y enviarlos a Telegram
@app.route('/actualizar_tareas', methods=['POST'])
def actualizar_tareas():
    data = request.get_json()  # Obtener los datos enviados a la API
    print(f"Datos recibidos: {data}")  # Esto ayuda a depurar si llegan correctamente

    # Extraer datos y enviarlos a Telegram
    mensaje = f"Nueva tarea actualizada:\n\nFila: {data['fila']}\nDatos: {data['datos']}"
    enviar_a_telegram(mensaje)

    return jsonify({"status": "Recibido", "data": data})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Usar el puerto que Render asigna
    app.run(host="0.0.0.0", port=port)
