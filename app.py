from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
      <head>
        <style>
          body {
            background:#121212;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
            margin:0;
          }
          h1 {
            font-family:sans-serif;
            font-size:2rem;
            color:#00ffcc;
            text-shadow:0 0 10px #00ffcc,0 0 20px #00ffcc;
            animation: glow 2s infinite alternate;
          }
          @keyframes glow {
            from { text-shadow:0 0 5px #00ffcc; }
            to { text-shadow:0 0 20px #ff00ff; color:#ff00ff; }
          }
        </style>
      </head>
      <body>
        <h1>|| MyselfNeon ||</h1>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
