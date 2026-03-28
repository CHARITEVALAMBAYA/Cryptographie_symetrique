from flask import Flask, render_template, request
from cryptography.fernet import Fernet
import base64

app = Flask(__name__)


SECRET_KEY = Fernet.generate_key()
cipher_suite = Fernet(SECRET_KEY)

@app.route("/", methods=["GET", "POST"])
def index():
    resultat = ""
    type_action = ""
    
    if request.method == "POST":
        texte = request.form.get("message", "")
        action = request.form.get("action")
        
        try:
            if action == "chiffrer":
                token = cipher_suite.encrypt(texte.encode())
                resultat = token.decode()
                type_action = "Message Chiffré"
            elif action == "dechiffrer":
                decoded = cipher_suite.decrypt(texte.encode())
                resultat = decoded.decode()
                type_action = "Message Déchiffré"
        except Exception:
            resultat = "Erreur : Clé invalide ou format incorrect."
            type_action = "Erreur"

    return render_template("index.html", resultat=resultat, type_action=type_action)

if __name__ == "__main__":
    app.run(debug=True)