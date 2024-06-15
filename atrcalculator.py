import streamlit as st

def calculate_stop_loss(entry_price, atr_value, multiplier):
    stop_loss_distance = atr_value * multiplier
    stop_loss_long = entry_price - stop_loss_distance
    stop_loss_short = entry_price + stop_loss_distance
    return stop_loss_long, stop_loss_short

st.title("ATR-Based Stop Loss Calculator")

entry_price = st.number_input("Entry Price:", value=1.0, format="%.5f")
atr_value = st.number_input("ATR Value:", value=0.00090, format="%.5f")
multiplier = st.number_input("Multiplier:", value=1.5, format="%.2f")

if st.button("Calculate Stop Loss"):
    stop_loss_long, stop_loss_short = calculate_stop_loss(entry_price, atr_value, multiplier)
    st.write(f"Long Trade Stop Loss: {stop_loss_long:.5f}")
    st.write(f"Short Trade Stop Loss: {stop_loss_short:.5f}")
