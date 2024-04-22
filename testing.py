import json
import threading
import websocket
from flask import Flask, render_template

price = []
asset = ['ethusdt@kline_1m']
data_printed = False  # Flag to track whether data has been printed

app = Flask(__name__)

rel_data = None

def on_message(ws, message):
    global rel_data
    message = json.loads(message)
    rel_data = message['data']['k']['c']

def websocket_thread():
    socket = "wss://stream.binance.com:9443/stream?streams="+ str(asset[0])
    ws = websocket.WebSocketApp(socket, on_message=on_message)
    ws.run_forever()

@app.route('/')
def index():
    return render_template('index.html', rel_data=rel_data)


