from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Bookinfo ProductPage - Daniel Liberato</h1><p>Versao FIAP Entregue!</p>"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    port = os.environ.get('PORT', '9080')
    app.run(host='0.0.0.0', port=int(port))