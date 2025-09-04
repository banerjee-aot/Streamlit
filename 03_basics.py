import streamlit as st

st.title("Layout Desgin")

col1, col2 = st.columns(2)


with col1:
    st.header("Click One")
    st.image('https://images.pexels.com/photos/618833/pexels-photo-618833.jpeg',width=200)
    btn1 = st.button("Click Me")
with col2:
    st.header("Click Two")
    st.image('https://images.pexels.com/photos/15286/pexels-photo.jpg',width=200)
    btn2 = st.button("Click Here")


if btn1:
    st.success("You clicked One !")
elif btn2:
    st.success("You clicked Two !")

name = st.sidebar.text_input("Enter your name")
location = st.sidebar.selectbox("Choose your location ",['Mountains','Forest','Sea','River','City'])
st.write(f"Welcome {name} and your location is {location}")


with st.expander("More Locations : ") :
    st.write("""  
    1. Darjeeling
    2. Jaldapara
    3. Digha
    4. Kolkata
 """)
    

st.markdown('# Welcome to my js code')
st.markdown("""
### Spread Operator (`...`)
- Expands (spreads) an array or object into individual elements.
- Used in arrays, objects, and function calls.

```javascript
let arr = [1, 2, 3];
let newArr = [...arr, 4, 5];
console.log(newArr); // [1, 2, 3, 4, 5]

let obj = { a: 1, b: 2 };
let newObj = { ...obj, c: 3 };
console.log(newObj); // { a: 1, b: 2, c: 3 }
""")


