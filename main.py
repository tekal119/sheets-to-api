from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# URL del Webhook de Google Apps Script que ya tenés funcionando
WEBHOOK_GOOGLE_SCRIPT = "https://script.google.com/macros/s/AKfycbzg44oxDb0whJcBlO08n5rV8ZJsvkR8BB5EswGQLWdJ6EQNVnHVHv-pyucubDG8HSr1/exec"

@app.route('/')
def home():
    return "✅ API puente funcionando correctamente 🚀"

@app.route('/actualizar_tareas', methods=['POST'])
def actualizar_tareas():
    try:
        data = request.get_json()

        # Reenvía directamente el JSON recibido al webhook de Apps Script
        response = requests.post(WEBHOOK_GOOGLE_SCRIPT, json=data)

        return jsonify({
            "status": "ok",
            "mensaje": "Datos reenviados a Google Apps Script",
            "respuesta_script": response.text
        })

    except Exception as e:
        return jsonify({"status": "error", "mensaje": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
