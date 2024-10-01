# Prescription Label Reading Project

## About the Project

**Problem Statement:**
Supporting elderly or vulnerable patients is crucial, particularly in the healthcare sector. One significant challenge they face is understanding prescription labels due to reading difficulties or visual impairments. By enabling voice messages through Text-to-Speech (TTS) technology, we can provide peace of mind and empower better services. Our application allows users to receive voice messages that read prescription labels, making it easier to understand medication information. This service can also help track dosage information and share it with caregivers.

## What My Application Does

This application is an OCR (Optical Character Recognition) and Google Text-to-Speech solution that allows users to upload an image of a prescription. The application processes the text within the image and converts all dosage and medication names into a speech format. This feature is particularly beneficial for individuals who struggle with reading or visual impairments, enabling them to hear and comprehend their medication instructions clearly.

## How It Is Made

1. **Image Collection:**
   - Collected sample prescription label images for processing.
   
2. **Image Preprocessing:**
   - Applied image preprocessing techniques to enhance clarity, ensuring accurate OCR detection.

3. **Text Extraction:**
   - Utilized [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) to extract text from the processed images.

4. **Text-to-Speech Conversion:**
   - Leveraged [Google Text-to-Speech](https://cloud.google.com/text-to-speech) to convert the extracted text into speech.

## Deployment

The application is built using Flask for the backend and is successfully deployed on [Render](https://render.com). 

To use the application, visit: [Prescription Label Reading Application](https://prescription-label-reading.onrender.com)

## How to Use

1. Upload an image of your prescription label.
2. The application will process the image to extract text.
3. The extracted text will then be converted into speech, which you can listen to for easy understanding of your medication instructions.

## Technologies Used

- Python
- Flask
- PaddleOCR
- Google Text-to-Speech
- HTML(for the frontend)

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Your contributions are welcome!

## Acknowledgments

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) for OCR functionality.
- [Google Text-to-Speech](https://cloud.google.com/text-to-speech) for speech synthesis capabilities.
- The open-source community for their invaluable contributions.

