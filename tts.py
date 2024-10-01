from paddleocr import PaddleOCR
from PIL import Image, ImageEnhance
import numpy as np
from gtts import gTTS
import os

ocr_model = PaddleOCR(lang = 'en',use_angle_cls = True)

def preprocess(image_path):
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

def text_to_speech(text,output_folder):
    # Create a gTTS object and save to MP3
    tts = gTTS(text=text, lang='en', slow=True)
    output_file = os.path.join(output_folder, "output.mp3")
    tts.save(output_file)

    return output_file

def final_model(image_path):
    # Extract text from the image
    text = text_extraction(image_path)

    # Convert extracted text to speech
    output = text_to_speech(text)

    return output