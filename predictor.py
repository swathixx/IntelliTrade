def prepare_data(data):
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data[['Close']])
    return None, None, scaler

def load_model():
    return None

def predict_next_days(model, data, scaler, days):
    last_price = data['Close'].iloc[-1]
    return [last_price + i for i in range(1, days + 1)]
