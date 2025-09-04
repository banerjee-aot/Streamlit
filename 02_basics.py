import streamlit as st

st.title("Hello!, Welcome To My App_02")

# if st.button("Click Here"):
#     pass


if st.button("Click Here"):
    st.success("Clicked")

tick = st.checkbox("Tick Here")
if tick:
    st.write("You are Checked")

radio = st.radio("Pick your choice :",['Red','Blue','Green'])
st.write(f"You selected {radio}")

speed = st.slider("Fan speed",0,5,1)
st.write(f"Fan speed is {speed}")

numInp = st.number_input("Enter a number",min_value = 1,max_value = 10,step = 1)
st.write(f"Your number is {numInp}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Your number is {name}")


date = st.date_input("Select your date")
if date:
    st.write(f"Your number is {date}")

