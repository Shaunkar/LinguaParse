# app.py
import streamlit as st
from PIL import Image
from config.config import get_api_key
from models.vision_model import VisionModel
from utils.image_utils import process_image

st.set_page_config(page_title="Multilanguage Invoice Extractor")

st.header("Multilanguage Invoice Extractor")
input_prompt = """
You are an expert in understanding invoices. We will upload an image as an invoice, 
and you will have to answer any questions based on the uploaded invoice image.
"""

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button("Tell me about the Invoice")

if submit:
    image_data = process_image(uploaded_file)
    api_key = get_api_key()
    vision_model = VisionModel(api_key)
    response = vision_model.generate_response(input_text, image_data[0], input_prompt)

    st.subheader("The Response is")
    st.write(response)