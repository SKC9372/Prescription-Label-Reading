from paddleocr import PaddleOCR
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import gradio as gr
from gtts import gTTS

ocr_model = PaddleOCR(lang = 'en',use_angle_cls = True)

# Initialize the OCR model
ocr_model = PaddleOCR(lang="en", use_angle_cls=True)

def preprocess(image_path):
    """
    Preprocess the image by enhancing its contrast and sharpness.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        np.ndarray: Preprocessed image as a NumPy array.
    """
    # Open the image
    image = Image.open(image_path)

    # Enhance contrast
    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(0.7)  # Adjust contrast

    # Enhance sharpness
    sharpness = ImageEnhance.Sharpness(image)
    image = sharpness.enhance(2)  # Adjust sharpness

    # Convert the image to a NumPy array
    image_np = np.array(image)

    return image_np

def text_extraction(image_path):
    """
    Extract text from the image using OCR.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        str: Extracted and filtered text as a single string.
    """
    # Preprocess the image
    image = preprocess(image_path)

    # Perform OCR on the image
    ocr_results = ocr_model.ocr(image, cls=True)

    # Keywords to look for in the extracted text
    keywords = ['mg', 'tablet', 'pills', 'quantity', 'qty', 'days', 'month', 'daily', 'hours', 'capsules']
    final_text = []

    # Extract relevant text from OCR results
    for line in ocr_results:
        for item in line:
            text = item[1][0]
            if any(word in text.lower() for word in keywords):
                final_text.append(text)

    return ' '.join(final_text)

def text_to_speech(text):
    """
    Convert text to speech and save it as an MP3 file.

    Args:
        text (str): The text to be converted to speech.

    Returns:
        str: Path to the saved MP3 file.
    """
    # Create a gTTS object and save to MP3
    tts = gTTS(text=text, lang='en', slow=True)
    output_file = "output.mp3"
    tts.save(output_file)

    return output_file

def final_model(image_path):
    """
    Complete workflow for extracting text from an image and converting it to speech.

    Args:
        image_path (str): Path to the input image file.

    Returns:
        str: Path to the saved MP3 file containing the speech.
    """
    # Extract text from the image
    text = text_extraction(image_path)

    # Convert extracted text to speech
    output = text_to_speech(text)

    return output


# Define the Gradio interface
interface = gr.Interface(
    fn=final_model,  # Function to be called
    inputs=gr.Image(type='filepath', label="Upload an Image"),  # Input image with a label
    outputs=gr.Audio(label="Generated Speech"),  # Output audio with a label
    title="Image to Speech Converter",  # Title of the interface
    description="Upload an image containing text, and this tool will extract the text and convert it to speech.",  # Description of the app
)

# Launch the Gradio interface
if __name__ == '__main__':
    interface.launch()