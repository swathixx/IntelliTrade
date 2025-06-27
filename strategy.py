def get_trade_signal(predictions, rsi):
    if rsi < 30:
        return "BUY"
    elif rsi > 70:
        return "SELL"
    else:
        return "HOLD"
