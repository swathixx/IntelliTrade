# 📈 IntelliTrade: AI-Powered Stock Forecasting Platform

Welcome to **IntelliTrade**, a simple yet powerful stock forecasting web application built using Python and Streamlit.

This project uses mock price data to simulate predictions for future stock prices and suggests trading actions (BUY / SELL / HOLD) based on the RSI (Relative Strength Index).

---

## 🚀 Features

- 🔤 Enter any stock ticker (e.g., AAPL, TSLA)
- 🎯 Choose forecast range (1–30 days)
- 📈 View past 30-day trend with future forecast
- 🧠 Get a smart trading suggestion (BUY / SELL / HOLD)
- 📄 Download predictions as CSV or PDF (optional)
- 💻 Lightweight UI built using Streamlit

---

## 🛠️ Built With

- Python 3.x  
- Streamlit  
- Pandas & NumPy  
- Matplotlib  
- Scikit-learn  
- fpdf (for PDF generation)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/IntelliTrade.git
cd IntelliTrade

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
🧪 Demo
🔍 Input:
Ticker: AAPL

Forecast Days: 7

✅ Output:
Daily predicted prices

Suggested Action: HOLD

RSI: 57.8

📚 Project Structure
bash
Copy code
IntelliTrade/
├── app.py               # Streamlit app UI
├── data_fetcher.py      # Simulates historical stock data
├── predictor.py         # Scales and predicts future values
├── strategy.py          # Suggests trade action based on RSI
├── requirements.txt     # Python package dependencies
└── README.md            # Project documentation

👩‍💻 Author
Swathika Saravanan
B.E. Computer Science and Engineering
Final Year Student
✉️ [swathisaravanan2255@gmail.com]


📌 License
This project is for academic/demo purposes and is shared freely for learning.





