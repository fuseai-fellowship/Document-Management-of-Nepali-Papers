import streamlit as st
import cv2
from PIL import Image
import numpy as np

# st.markdown(
#     """
#     <style>
#     footer {visibility: hidden;}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.markdown("<h1 style='text-align: center;'>Documents containing words</h1>", unsafe_allow_html=True)

image_files = [
    "/home/pranjal/Downloads/prac/Education.jpg",
    "/home/pranjal/Downloads/prac/policy.png"
]

if "image_index" not in st.session_state:
    st.session_state["image_index"] = 0

def load_image(image_path):
    img = cv2.imread(image_path)  
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
    return img_rgb

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("Previous Image"):
        if st.session_state["image_index"] > 0:
            st.session_state["image_index"] -= 1

with col3:
    if st.button("Next Image"):
        if st.session_state["image_index"] < len(image_files) - 1:
            st.session_state["image_index"] += 1

image_path = image_files[st.session_state["image_index"]]
image = load_image(image_path)

st.image(image, use_column_width=True)
