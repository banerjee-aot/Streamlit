# import streamlit as st
# import requests

# st.title("Currency Converter")

# amount = st.number_input("Enter the amount in INR", min_value = 1)

# target_currency = st.selectbox("Convert to",["USD", "EUR", "GBP", "JPY"])

# if st.button("Convert"):
#     url = "https://open.er-api.com/v6/latest/INR"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         rate = data["rates"][target_currency]
#         converted = rate * amount
#         st.success(f"{amount} INR = {converted: .2f} {target_currency}")
#     else:
#         st.error("Failed to fetch conversion rate")







# Modified


import streamlit as st
import requests

st.title("Currency Converter")

url = "https://open.er-api.com/v6/latest/INR"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    currencies = list(data["rates"].keys())  # dynamic currency list
else:
    st.error("Failed to fetch currency data")
    currencies = []  # fallback empty list

amount = st.number_input("Enter the amount in INR", min_value=1)

target_currency = st.selectbox("Convert to", currencies)

if st.button("Convert"):
    if response.status_code == 200:
        rate = data["rates"][target_currency]
        converted = rate * amount
        st.success(f"{amount} INR = {converted:.2f} {target_currency}")
    else:
        st.error("Failed to fetch conversion rate")



