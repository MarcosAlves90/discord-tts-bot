from flask import Flask, render_template
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def run():
    app.run(host="0.0.0.0", port=10000)

def start_keepalive():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()