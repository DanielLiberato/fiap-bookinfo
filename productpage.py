from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bookinfo - Daniel Liberato</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1e1e2f 0%, #2d2d44 100%);
                color: #ffffff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: #252537;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.5);
                text-align: center;
                max-width: 500px;
                width: 90%;
                border: 1px solid #383850;
            }
            h1 {
                color: #ed145b; /* Cor de destaque (tipo FIAP Pink) */
                margin-bottom: 10px;
                font-size: 2.5em;
            }
            h2 {
                color: #fff;
                font-weight: 300;
                font-size: 1.2em;
                margin-bottom: 30px;
            }
            .status-badge {
                background-color: #00c853;
                color: white;
                padding: 8px 15px;
                border-radius: 50px;
                font-weight: bold;
                font-size: 0.9em;
                display: inline-block;
                margin-bottom: 20px;
            }
            p {
                color: #a0a0b0;
                line-height: 1.6;
            }
            .footer {
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #383850;
                font-size: 0.8em;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>📚 Bookinfo</h1>
            <h2>Product Page Microservice</h2>
            
            <div class="status-badge">✅ Versão Estável: 1.0.0</div>
            
            <p>
                Aplicação entregue via <strong>Pipeline CI/CD Automatizado</strong>.<br>
                Container rodando em arquitetura Docker.
            </p>
            
            <div class="footer">
                Desenvolvido por <strong>Daniel Liberato</strong><br>
                MBA em DevOps & Cloud Engineering - FIAP
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    port = os.environ.get('PORT', '9080')
    app.run(host='0.0.0.0', port=int(port))