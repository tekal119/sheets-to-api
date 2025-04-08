import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configuración del destino al que reenviar los datos (puede ser tu webhook de Google Sheets)
DESTINO_WEBHOOK = "https://script.google.com/macros/s/AKfycbzg44oxDb0whJcBlO08n5rV8ZJsvkR8BB5EswGQLWdJ6EQNVnHVHv-pyucubDG8HSr1/exec"

@app.route('/')
def home():
    return "API funcionando como puente ✅"

@app.route('/puente', methods=['POST'])
def reenviar_datos():
    data = request.get_json()

    try:
        # Enviar el JSON recibido directamente al webhook de destino
        response = requests.post(DESTINO_WEBHOOK, json=data)
        return jsonify({
            "status": "ok",
            "forwarded_to": DESTINO_WEBHOOK,
            "original_data": data,
            "response_from_webhook": response.text
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
