import streamlit as st
from config import get_api_key
from models import VisionModel
from utils import process_image

# Configure page title
st.set_page_config(page_title="Multilanguage Invoice Extractor")

# Create an instance of the VisionModel
api_key = get_api_key()
model = VisionModel(api_key)

# App layout and elements
st.header("Multilanguage Invoice Extractor")

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

if st.button("Tell me about the Invoice"):
    try:
        image_parts = process_image(uploaded_file)
        prompt = """
        You are an expert in understanding invoices. We will upload an image as invoice and you will have to answer any questions based on the uploaded invoice image.
        """
        response = model.generate_response(input_text, image_parts, prompt)

        st.subheader("The Response is")
        st.write(response)

    except ValueError as e:
        st.error(e)