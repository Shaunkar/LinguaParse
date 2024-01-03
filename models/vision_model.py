import google.generativeai as genai

class VisionModel:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro-vision')

    def generate_response(self, input_text, image_parts, prompt):
        response = self.model.generate_content([input_text, image_parts, prompt])
        return response.text
