import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configuración del bot de Telegram
TELEGRAM_BOT_TOKEN = "7291475602:AAEKIkIrlG-RUWyiGsm3u8jzsFZucute3yg"
TELEGRAM_CHAT_ID = "5278452082"

def enviar_a_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/')
def home():
    return "API funcionando correctamente 🚀"

@app.route('/actualizar_tareas', methods=['POST'])
def actualizar_tareas():
    data = request.get_json()
    print(f"📩 Datos recibidos: {data}")  # Log de depuración

    # Extraer datos con valores predeterminados si faltan
    prioridad = data.get("C2", "Sin prioridad")
    categoria = data.get("D2", "Sin categoría")
    tarea = data.get("E2", "Sin tarea")
    start_date = data.get("F2", "Sin fecha de inicio")
    endline_date = data.get("G2", "")
    responsable = data.get("I2", "Sin responsable")
    notas = data.get("J2", "Sin detalles")
    recordatorio1 = data.get("L2", "")
    recordatorio2 = data.get("M2", "")
    recordatorio3 = data.get("N2", "")

    # Mensaje según el responsable
    if isinstance(responsable, str) and responsable.lower() == "tekal":
        mensaje = f"Tekal, el día {start_date} programaste este recordatorio para que te acuerdes de *ESTO*:\n\n"
    else:
        mensaje = f"El día {start_date} programaste este recordatorio para recordarle a *{responsable}* de lo siguiente:\n\n"

    mensaje += f"📂 Para: *{categoria}*\n"
    mensaje += f"🔥 Con una prioridad: *{prioridad}*\n"
    mensaje += f"✅ Tenés que: *{tarea}*, lo cual implica: {notas}\n"

    # Solo agregar la fecha de finalización si es válida
    if endline_date and any(char.isdigit() for char in endline_date):  # Verifica si contiene números
        mensaje += f"📅 Debe estar terminado para el día: *{endline_date}*\n"

    # Agregar recordatorios si existen
    if recordatorio1:
        mensaje += f"🔔 Recordatorio para el día: *{recordatorio1}*\n"
    if recordatorio2:
        mensaje += f"🔔 Otro recordatorio para el día: *{recordatorio2}*\n"
    if recordatorio3:
        mensaje += f"🔔 Un recordatorio más para el día *{recordatorio3}*, así que para este día tenés que tener todo listo.\n"

    mensaje += "\n⚡ *Tekal, SOS EL 1!! SABELO, RECORDALO SIEMPRE* 🔥"

    # Enviar a Telegram
    resultado = enviar_a_telegram(mensaje)
    print(f"📤 Respuesta de Telegram: {resultado}")

    return jsonify({"status": "Recibido", "data": data, "telegram_response": resultado})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
