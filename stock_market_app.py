import streamlit as st
import pandas as pd
import yfinance as yf
import datetime

st.title("Stock Market App")
st.write("Hopefully this app becomes a big one!!!")


start_date = st.date_input("Select start date",datetime.date(2019,1,1))
end_date = st.date_input("Select end date",datetime.date(2024,12,31))

# ticker_symbol = 'ITC.BO'
ticker_symbol = st.text_input("Enter the stock ticker symbol", "ITC.BO")

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d', start=f'{start_date}', end=f'{end_date}' )

st.dataframe(ticker_df)

st.write("## Daily Closing Price Trend")
st.line_chart(ticker_df.Close)

col1, col2 = st.columns(2)

with col1:
    st.write("## Daily Closing Plot")
    st.line_chart(ticker_df.Close)
    
with col2:
    st.write('## Daily volume plot')
    st.line_chart(ticker_df.Volume)