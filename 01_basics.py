import streamlit as st

st.title("Hello!, Welcome To My App_1")
st.subheader("Brewed with streamlit")
st.text("This is the interactive app")
st.write("Choose your fav variety")

myDrop = st.selectbox("Choose a colour :",['Red','Blue','Green','Black','White'])
st.write(f"You choose {myDrop}")
st.success("Your color has been brewed")
