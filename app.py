from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MyselfNeon</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: #121212;
                color: #00ffcc;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-align: center;
            }
            .box {
                padding: 20px 40px;
                border: 2px solid #00ffcc;
                border-radius: 12px;
                background: rgba(255, 255, 255, 0.05);
                box-shadow: 0 0 15px #00ffcc;
                font-size: 2rem;
                letter-spacing: 2px;
            }
            .box span {
                color: #ff00ff;
            }
        </style>
    </head>
    <body>
        <div class="box">
            || <span>MyselfNeon</span> ||
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
