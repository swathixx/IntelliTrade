import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from fpdf import FPDF
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(page_title="IntelliTrade", layout="wide")
st.title("📈 IntelliTrade: AI-Powered Stock Forecast")

def fetch_stock_data(ticker, start, end):
    dates = pd.date_range(start=start, end=end)
    df = pd.DataFrame({
        "Close": np.random.rand(len(dates)) * 100 + 100,
        "RSI": np.clip(np.random.normal(50, 10, size=len(dates)), 0, 100)
    }, index=dates)
    return df

def prepare_data(data):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data[['Close']])
    return None, None, scaler

def load_model():
    return None

def predict_next_days(model, data, scaler, days):
    last_price = data['Close'].iloc[-1]
    return [last_price + i for i in range(1, days + 1)]

def get_trade_signal(preds, rsi):
    if rsi < 30:
        return "BUY"
    elif rsi > 70:
        return "SELL"
    return "HOLD"

# UI
ticker = st.text_input("Enter Stock Ticker", value="AAPL")
forecast_days = st.slider("Forecast Days", 1, 30, 7)

if st.button("🔍 Predict"):
    data = fetch_stock_data(ticker, "2020-01-01", datetime.today().strftime("%Y-%m-%d"))
    rsi = data['RSI'].iloc[-1]
    _, _, scaler = prepare_data(data)
    model = load_model()
    forecast = predict_next_days(model, data, scaler, forecast_days)
    signal = get_trade_signal(forecast, rsi)

    fig, ax = plt.subplots()
    data['Close'][-30:].plot(ax=ax, label="Past")
    ax.plot(range(len(data), len(data)+forecast_days), forecast, label="Forecast")
    ax.legend()
    st.pyplot(fig)

    for i, p in enumerate(forecast, 1):
        st.write(f"Day {i}: ${p:.2f}")
    st.success(f"🧠 Suggested Action: {signal} | RSI: {rsi:.2f}")
