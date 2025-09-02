# OCR-Detection
A Flask-based OCR web app that extracts text from images and PDFs using Tesseract. Includes preprocessing for higher accuracy and a simple upload interface.”
# 🖼️ OCR Web App (Flask + Tesseract)

A simple **Flask-based OCR (Optical Character Recognition) web application** that allows you to upload images  and extract text from them using **Tesseract OCR**.  

---

## 🚀 Features
- Upload **images (`.jpg`, `.png`)**
- Automatic preprocessing (grayscale → blur → threshold) for better OCR accuracy
- Extract text using **Tesseract**
- Easy-to-use web interface built with Flask
- Supports both **local images** 

---

## 📂 Project Structure
ocr-app/
│── app.py # Main Flask application
│── preprocess.py # Preprocessing and PDF handling
│── requirements.txt # Dependencies
│── uploads/ # Uploaded files (auto-created)
│── templates/
│ └── index.html # Upload form
