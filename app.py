from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <body style="background-color:black; color:yellow; display:flex; justify-content:center; align-items:center; height:100vh; margin:0; font-family:sans-serif;">
        || MyselfNeon ||
    </body>
    """

if __name__ == "__main__":
    app.run()
