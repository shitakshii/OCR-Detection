from flask import Flask, render_template, request
import os
import pytesseract
from preprocess import preprocess_image

# Create Flask app
app = Flask(__name__)

# Folder to store uploaded images
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)   # Create folder if not exists


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    text = None

    if request.method == 'POST':
        # Get uploaded file
        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', text="⚠ No file selected")

        # Save uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        print("✅ File saved at:", os.path.abspath(filepath))  # Debugging line

        try:
            # Preprocess image
            processed_image = preprocess_image(filepath)

            # Extract text using Tesseract
            text = pytesseract.image_to_string(processed_image)

        except Exception as e:
            text = f"❌ Error processing image: {str(e)}"

    return render_template('index.html', text=text)


if __name__ == "__main__":
    app.run(debug=True)
