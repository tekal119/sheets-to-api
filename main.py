from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API funcionando correctamente 🚀"

@app.route('/actualizar_tareas', methods=['POST'])
def actualizar_tareas():
    data = request.get_json()
    print("📥 Datos recibidos:", data)
    return jsonify({"status": "ok", "message": "Tarea recibida correctamente"})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
