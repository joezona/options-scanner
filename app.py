import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Tastytrade API Base URL
BASE_URL = "https://api.cert.tastyworks.com"

# Web App Layout
st.set_page_config(page_title="Options Trading Scanner", layout="wide")
st.title("📈 Options Trading Scanner")
st.markdown("Find high-probability options trades based on real-time data.")

# Sidebar Controls
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("🔑 Enter your Tastytrade API Key", type="password")
symbol = st.sidebar.text_input("📊 Stock Symbol (e.g., SPY, AAPL)", "SPY")
risk_level = st.sidebar.radio("⚖️ Risk Level", ["High Probability", "Riskier Strategies"], index=0)

if api_key:
    # Fetch options data from Tastytrade API
    headers = {"Authorization": f"Bearer {api_key}"}
    url = f"{BASE_URL}/v1/markets/options/{symbol}/chains"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        options = data.get("data", {}).get("items", [])
        
        if options:
            df = pd.DataFrame(options)
            
            # Filtering logic (High probability: 16-30 Delta, Riskier: <16 or >30 Delta)
            if risk_level == "High Probability":
                df = df[(df['delta'] >= -0.30) & (df['delta'] <= 0.30)]
            
            df = df.sort_values(by="probability_of_profit", ascending=False)
            
            st.subheader("📌 Recommended Trades")
            st.dataframe(df[["symbol", "strike-price", "expiration-date", "delta", "probability-of-profit"]])
            
            # Visualization
            st.subheader("📊 Probability of Profit vs Strike Price")
            fig = px.scatter(df, x="strike-price", y="probability-of-profit", size="delta", color="delta",
                             labels={"strike-price": "Strike Price", "probability-of-profit": "Probability of Profit"},
                             title=f"{symbol} Options Profitability")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("⚠️ No options data found for this symbol.")
    else:
        st.error("❌ Failed to fetch data. Check your API key and symbol.")
else:
    st.warning("🔑 Enter your API key to fetch data.")
