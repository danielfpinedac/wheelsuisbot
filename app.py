<<<<<<< HEAD
from flask import Flask, request, redirect
import requests

app = Flask(__name__)

# === CONFIGURACIÓN ===
VERIFY_TOKEN = "wheelsuis_token123"

import os
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# === Códigos válidos ===
CODIGOS = {"456"}

# === RUTAS PRINCIPALES ===
@app.route("/", methods=["GET"])
def home():
    return "✅ Wheelsuis BOT activo", 200

@app.route("/webhook", methods=["GET"])
def verify_token():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == VERIFY_TOKEN:
        return challenge
    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def receive_message():
    data = request.get_json()
    print("📩 Mensaje recibido:", data)

    try:
        value = data["entry"][0]["changes"][0]["value"]
        if "messages" not in value:
            return "EVENT_RECEIVED", 200

        message = value["messages"][0]
        sender = message["from"]
        text = message["text"]["body"].strip().lower()
        print(f"📨 De {sender}: {text}")

        url_send = "https://graph.facebook.com/v17.0/841814475674471/messages"
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

        # === Mensaje inicial ===
        if "hola" in text and "wheelsuis" in text:
            respuesta = {
                "messaging_product": "whatsapp",
                "to": sender,
                "type": "text",
                "text": {
                    "body": "👋 ¡Claro! Digita el código para darte acceso al grupo Wheelsuis del barrio Cañaveral!"
                }
            }
            requests.post(url_send, headers=headers, json=respuesta)
            print("🟢 Mensaje inicial enviado.")
            return "EVENT_RECEIVED", 200

        # === Código válido ===
        if text in CODIGOS:
            confirm_msg = {
                "messaging_product": "whatsapp",
                "to": sender,
                "type": "text",
                "text": {
                    "body": f"✅ Código {text} verificado.\nPresiona el botón para entrar al grupo Wheelsuis Cañaveral."
                }
            }
            requests.post(url_send, headers=headers, json=confirm_msg)

            template_msg = {
                "messaging_product": "whatsapp",
                "to": sender,
                "type": "template",
                "template": {
                    "name": "join_group_wheelsuis",
                    "language": {"code": "en"}
                }
            }
            requests.post(url_send, headers=headers, json=template_msg)
            print("🟢 Plantilla enviada.")
            return "EVENT_RECEIVED", 200

        # === Código incorrecto ===
        error_msg = {
            "messaging_product": "whatsapp",
            "to": sender,
            "type": "text",
            "text": {"body": "🚫 Lo siento, no tienes acceso a Wheelsuis Cañaveral."}
        }
        requests.post(url_send, headers=headers, json=error_msg)
        print("🔴 Mensaje de error enviado.")

    except Exception as e:
        print("❌ Error procesando el mensaje:", e)

    return "EVENT_RECEIVED", 200

GRUPOS = {
    "canaveral": "https://chat.whatsapp.com/DwEO6W9a2WM15UDFH9pRrB"
}

@app.route("/join/<barrio>")
def join_group(barrio):
    barrio = barrio.lower()
    if barrio in GRUPOS:
        return redirect(GRUPOS[barrio], code=302)
    return "❌ Enlace no encontrado", 404

if __name__ == "__main__":
    app.run(port=5000, debug=True)






=======
from flask import Flask, request, redirect
import requests

app = Flask(__name__)

# === CONFIGURACIÓN ===
VERIFY_TOKEN = "wheelsuis_token123"

import os
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# === Códigos válidos ===
CODIGOS = {"456"}

# === RUTAS PRINCIPALES ===
@app.route("/", methods=["GET"])
def home():
    return "✅ Wheelsuis BOT activo", 200

@app.route("/webhook", methods=["GET"])
def verify_token():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == VERIFY_TOKEN:
        return challenge
    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def receive_message():
    data = request.get_json()
    print("📩 Mensaje recibido:", data)

    try:
        value = data["entry"][0]["changes"][0]["value"]
        if "messages" not in value:
            return "EVENT_RECEIVED", 200

        message = value["messages"][0]
        sender = message["from"]
        text = message["text"]["body"].strip().lower()
        print(f"📨 De {sender}: {text}")

        url_send = "https://graph.facebook.com/v17.0/841814475674471/messages"
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

        # === Mensaje inicial ===
        if "hola" in text and "wheelsuis" in text:
            respuesta = {
                "messaging_product": "whatsapp",
                "to": sender,
                "type": "text",
                "text": {
                    "body": "👋 ¡Claro! Digita el código para darte acceso al grupo Wheelsuis del barrio Cañaveral!"
                }
            }
            requests.post(url_send, headers=headers, json=respuesta)
            print("🟢 Mensaje inicial enviado.")
            return "EVENT_RECEIVED", 200

        # === Código válido ===
        if text in CODIGOS:
            confirm_msg = {
                "messaging_product": "whatsapp",
                "to": sender,
                "type": "text",
                "text": {
                    "body": f"✅ Código {text} verificado.\nPresiona el botón para entrar al grupo Wheelsuis Cañaveral."
                }
            }
            requests.post(url_send, headers=headers, json=confirm_msg)

            template_msg = {
                "messaging_product": "whatsapp",
                "to": sender,
                "type": "template",
                "template": {
                    "name": "join_group_wheelsuis",
                    "language": {"code": "en"}
                }
            }
            requests.post(url_send, headers=headers, json=template_msg)
            print("🟢 Plantilla enviada.")
            return "EVENT_RECEIVED", 200

        # === Código incorrecto ===
        error_msg = {
            "messaging_product": "whatsapp",
            "to": sender,
            "type": "text",
            "text": {"body": "🚫 Lo siento, no tienes acceso a Wheelsuis Cañaveral."}
        }
        requests.post(url_send, headers=headers, json=error_msg)
        print("🔴 Mensaje de error enviado.")

    except Exception as e:
        print("❌ Error procesando el mensaje:", e)

    return "EVENT_RECEIVED", 200

GRUPOS = {
    "canaveral": "https://chat.whatsapp.com/DwEO6W9a2WM15UDFH9pRrB"
}

@app.route("/join/<barrio>")
def join_group(barrio):
    barrio = barrio.lower()
    if barrio in GRUPOS:
        return redirect(GRUPOS[barrio], code=302)
    return "❌ Enlace no encontrado", 404

if __name__ == "__main__":
    app.run(port=5000, debug=True)






>>>>>>> 0832678 (Migrar token a variable de entorno ACCESS_TOKEN)
