from flask import Flask, session, redirect, url_for
import os
from fiscal_routes import fiscal_bp # Importa apenas o fiscal
from secrets import token_hex

app = Flask(__name__)
app.secret_key = token_hex(16)

# Registra apenas o módulo Fiscal
app.register_blueprint(fiscal_bp)

@app.route('/')
def home():
    # Redireciona direto para a central de downloads ao abrir o site
    return redirect(url_for('fiscal.central_downloads'))

if __name__ == '__main__':
    print("Módulo Fiscal iniciado! Acesse: http://127.0.0.1:5000")
    app.run(debug=True)
