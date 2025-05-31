from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot está rodando!"

def run():
    app.run(host="0.0.0.0", port=10000)

def start_keepalive():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()