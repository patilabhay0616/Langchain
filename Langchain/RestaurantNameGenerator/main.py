import streamlit as st
import Langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Italian", "Indian", "Mexican", "Arabic", "American"))

def generate_restaurant_name_and_items(cuisine):
    return{
        'restaurant_name': 'Curry Delight',
        'Menu_items': 'Samosa, paneer tikka'
    }

if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    Menu_items = response['Menu_items'].split(",")
    st.write("**Menu Items**")
    for item in Menu_items:
        st.write("-", item)