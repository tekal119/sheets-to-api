import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "API funcionando correctamente 🚀"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Usa el puerto que Render asigna
    app.run(host='0.0.0.0', port=port)