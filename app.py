from flask import Flask,url_for,render_template,send_file,request
from tts import text_extraction,text_to_speech
import os

app = Flask(__name__)

# Folder to store uploaded files temporarily
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title = 'Home')

@app.route('/label_reading', methods=['GET', 'POST'])
def label():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('pres_reading.html', error='No file part in the request')

        file = request.files['file']

        if file.filename == '':
            return render_template('pres_reading.html', error='No selected file')

        if file:
            # Save the uploaded image
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Process the image to extract text and convert to speech
            text = text_extraction(file_path)
            if not text:
                return render_template('pres_reading.html', error='No relevant text found')

            # Convert the extracted text to speech
            output_file = text_to_speech(text,app.config['UPLOAD_FOLDER'])

            # Generate a URL for the file download
            file_url = url_for('download_file', filename="output.mp3")

            # Return the HTML with a download link
            return render_template('pres_reading.html', file_url=file_url)
    
    # This return will handle GET requests, or if POST fails to meet any condition
    return render_template('pres_reading.html')

    
# Route to handle file download
@app.route('/uploads/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=False)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port= int(os.getenv("PORT",5000)))