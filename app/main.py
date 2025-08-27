from fastapi import FastAPI, WebSocket
import requests, json
import numpy as np

from .strategy import generate_signal

app = FastAPI()

@app.get("/")
def home():
    return {"ok": True, "msg": "IA Online 🚀"}

@app.websocket("/ws/signals")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        try:
            # Puxa candles da Binance (par BTC/USDT, timeframe 1m)
            url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=50"
            candles = requests.get(url).json()
            closes = np.array([float(c[4]) for c in candles])

            # Gera sinal de compra/venda
            signal, rsi = generate_signal(closes)

            await ws.send_text(json.dumps({
                "symbol": "BTCUSDT",
                "rsi": float(rsi),
                "signal": signal
            }))
        except Exception as e:
            await ws.send_text(json.dumps({"error": str(e)}))
