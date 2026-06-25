import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests

st.title("📈 Real-Time Stock Market Dashboard")

# User input
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA)", "AAPL")

if symbol:
    # Example API (replace with your own key if needed)
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=d8ue2tpr01qinhuhdv40d8ue2tpr01qinhuhdv4g"
    response = requests.get(url).json()

    if "c" in response:
        st.subheader(f"Current Price: ${response['c']}")
        st.write(f"High: {response['h']} | Low: {response['l']} | Open: {response['o']}")

        # Simple graph
        df = pd.DataFrame({
            "Price": [response['o'], response['c'], response['h'], response['l']],
            "Type": ["Open", "Current", "High", "Low"]
        })
        fig = go.Figure([go.Bar(x=df["Type"], y=df["Price"])])
        st.plotly_chart(fig)
    else:
        st.error("Could not fetch data. Check symbol or API key.")
