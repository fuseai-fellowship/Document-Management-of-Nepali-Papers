import streamlit as st
import home
import slider

# Query params to handle navigation
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["main"])[0]

if page == "main":
    home
elif page == "details":
    slider
