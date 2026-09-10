Paste the following:

# 🧠 Brain Tumor Detection using HOG + SVM

A simple machine learning web application that classifies brain MRI images into:

- 🟢 No Tumor
- 🔴 Tumor Detected

The system uses **HOG (Histogram of Oriented Gradients)** for feature extraction and **SVM (Support Vector Machine)** for image classification.

The trained machine learning model is integrated into a **Flask backend** with a simple **HTML, CSS and JavaScript** web interface.

---

## 🚀 Project Overview

Brain Tumor Detection System is an educational machine learning project designed to demonstrate how traditional machine learning techniques can be applied to medical image classification.

### Workflow

```text
MRI Image
    ↓
Image Preprocessing
    ↓
Resize to 128 × 128
    ↓
Grayscale Conversion
    ↓
HOG Feature Extraction
    ↓
SVM Classification
    ↓
Prediction
    ↓
Web Interface
🛠️ Technologies Used
Python
Scikit-learn
Scikit-image
NumPy
Pillow
Joblib
Flask
Flask-CORS
HTML5
CSS3
JavaScript
🤖 Machine Learning Algorithm
HOG – Histogram of Oriented Gradients

HOG is used to extract important shape and edge information from MRI images.

In this project, the image is resized to:

128 × 128

HOG parameters:

Orientations: 9
Pixels per cell: 8 × 8
Cells per block: 2 × 2
Block normalization: L2-Hys
SVM – Support Vector Machine

The extracted HOG features are given to an SVM classifier.

The SVM classifies the MRI image into:

0 → No Tumor
1 → Tumor Detected
🌐 Web Application

The project provides a simple web interface where the user can:

Upload an MRI image
Preview the selected image
Click Analyze MRI
Send the image to the Flask backend
Extract HOG features
Run the trained SVM model
Display the prediction and model score
📁 Project Structure
BrainTumorDetection/
│
├── Backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── model/
│   └── hog_svm_model.pkl
│
├── .gitignore
│
└── README.md
📊 Dataset

The project uses a brain MRI image dataset containing two classes:

yes → Tumor images
no  → No-tumor images

Current dataset:

Tumor (yes): 155 images
No Tumor (no): 98 images
Total: 253 images

The dataset is not included in this repository.

⚙️ Installation
1. Clone the repository
git clone https://github.com/chachleshrutika59-cmyk/Brain-Tumor-Detection-using-HOG-SVM.git
2. Open the project
cd Brain-Tumor-Detection-using-HOG-SVM
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows:

venv\Scripts\activate
5. Install required packages
pip install flask flask-cors pillow scikit-image scikit-learn numpy joblib
▶️ Running the Application

Go to the Backend folder:

cd Backend

Run:

python app.py

The Flask server will start at:

http://127.0.0.1:5000

Open this address in your browser.

🔍 Prediction Process

When an MRI image is uploaded:

Upload Image
     ↓
Convert to Grayscale
     ↓
Resize to 128 × 128
     ↓
Extract HOG Features
     ↓
Load Trained SVM Model
     ↓
Predict Class
     ↓
Display Result
📌 Example Results
No Tumor
Prediction: No Tumor
Model Score: 98.40%
Tumor Detected
Prediction: Tumor Detected
Model Score: 91.11%

The displayed score represents the model's prediction probability/score and should not be interpreted as a medical diagnosis.

🎯 Project Objectives
Apply machine learning to MRI image classification
Understand HOG feature extraction
Implement Support Vector Machine classification
Integrate a trained ML model with Flask
Build a simple web-based prediction interface
Demonstrate an end-to-end machine learning workflow
🔮 Future Improvements
Increase the size and diversity of the dataset
Apply data augmentation
Improve model evaluation
Add confusion matrix and classification reports
Compare SVM with other machine learning algorithms
Add user authentication
Store prediction history
Deploy the application online
Explore deep learning approaches such as CNNs
⚠️ Disclaimer

This project is developed for educational and demonstration purposes only.

It is not intended to provide medical diagnosis, treatment, or clinical advice.

MRI results should always be evaluated by qualified medical professionals.

👩‍💻 Author

Shrutika Chachle

Machine Learning Project

⭐ Project Highlights
✔ Image preprocessing
✔ HOG feature extraction
✔ SVM classification
✔ Trained ML model
✔ Flask REST API
✔ HTML/CSS/JavaScript interface
✔ Real-time image prediction