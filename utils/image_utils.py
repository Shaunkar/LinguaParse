import pathlib
from PIL import Image

def process_image(uploaded_file):
    """Processes an uploaded image and prepares it for the model.

    Args:
        uploaded_file: The uploaded image file object.

    Returns:
        A list of image parts in the format required by the model,
        typically a list of dictionaries containing MIME types and image data.
    """

    try:
        # Read the image bytes
        image_bytes = uploaded_file.getvalue()

        # Perform any necessary image processing here
        # ... (e.g., resizing, format conversion, cropping, etc.)

        # Prepare image parts for the model
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the MIME type
                "data": image_bytes  # Include the processed image bytes
            }
        ]

        return image_parts

    except Exception as e:
        raise ValueError(f"Error processing image: {e}") from e
