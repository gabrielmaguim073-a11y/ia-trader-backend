import talib
import numpy as np

def generate_signal(closes):
    """
    Recebe uma lista de preços de fechamento e retorna um sinal de trade.
    Estratégia simples usando RSI:
    - RSI < 30 → BUY
    - RSI > 70 → SELL
    - Caso contrário → HOLD
    """
    # Calcula RSI com período de 14 candles
    rsi = talib.RSI(closes, timeperiod=14)[-1]

    if rsi < 30:
        return "BUY", rsi
    elif rsi > 70:
        return "SELL", rsi
    else:
        return "HOLD", rsi
