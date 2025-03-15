import os
from flask import Flask, request, jsonify
import requests

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
    return response.json()

@app.route('/')
def home():
    return "API funcionando correctamente 🚀"

@app.route('/actualizar_tareas', methods=['POST'])
def actualizar_tareas():
    data = request.get_json()

    prioridad = data.get("C2", "Sin prioridad")
    categoria = data.get("D2", "Sin categoría")
    tarea = data.get("E2", "Sin tarea")
    start_date = data.get("F2", "Sin fecha de inicio").split("T")[0]  # Convertir formato de fecha
    endline_date = data.get("G2", "").split("T")[0] if data.get("G2") else ""
    responsable = data.get("I2", "Sin responsable")
    notas = data.get("J2", "Sin detalles")
    recordatorio1 = data.get("L2", "").split("T")[0] if data.get("L2") else ""
    recordatorio2 = data.get("M2", "").split("T")[0] if data.get("M2") else ""
    recordatorio3 = data.get("N2", "").split("T")[0] if data.get("N2") else ""

    # Mensaje según responsable
    if responsable.lower() == "tekal":
        mensaje = f"Tekal, el día *{start_date}* programaste este recordatorio para que te acuerdes de *ESTO*:\n\n"
    else:
        mensaje = f"El día *{start_date}* programaste este recordatorio para recordarle a *{responsable}* de lo siguiente:\n\n"

    mensaje += f"📂 *Para* {categoria}\n"
    mensaje += f"🔥 *Con una prioridad:* {prioridad}\n\n"
    mensaje += f"✅ *Tenés que:* {tarea}\n"
    mensaje += f"📝 Lo cual implica: {notas}\n\n"

    # Solo agregar la fecha de finalización si es válida
    if endline_date:
        mensaje += f"📅 *Debe estar terminado para el día:* {endline_date}\n\n"

    # Agregar recordatorios si existen
    if recordatorio1:
        mensaje += f"🔔 *Recordatorio para el día:* {recordatorio1}\n"
    if recordatorio2:
        mensaje += f"🔔 *Otro recordatorio para el día:* {recordatorio2}\n"
    if recordatorio3:
        mensaje += f"⚡ *Un recordatorio más para el día* {recordatorio3}, así que para este día tenés que tener todo listo.\n"

    mensaje += "\n🔥 *Tekal, SOS EL 1!! SABELO, RECORDALO SIEMPRE* 🔥"

    enviar_a_telegram(mensaje)
    
    return jsonify({"status": "Recibido", "data": data})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
