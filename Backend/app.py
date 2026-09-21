from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from PIL import Image
from skimage.feature import hog

import numpy as np
import joblib
import os


# =====================================================
# PATHS
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

FRONTEND_DIR = os.path.join(
    BASE_DIR,
    "frontend"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "hog_svm_model.pkl"
)


# =====================================================
# CHECK PATHS
# =====================================================

print("========================================")
print("BASE DIR:", BASE_DIR)
print("FRONTEND DIR:", FRONTEND_DIR)
print("MODEL PATH:", MODEL_PATH)

print(
    "index.html exists:",
    os.path.exists(
        os.path.join(FRONTEND_DIR, "index.html")
    )
)

print(
    "style.css exists:",
    os.path.exists(
        os.path.join(FRONTEND_DIR, "style.css")
    )
)

print(
    "script.js exists:",
    os.path.exists(
        os.path.join(FRONTEND_DIR, "script.js")
    )
)

print(
    "model exists:",
    os.path.exists(MODEL_PATH)
)

print("========================================")


# =====================================================
# FLASK APP
# =====================================================

# IMPORTANT:
# Tell Flask that FRONTEND_DIR is the static folder.

app = Flask(
    __name__,
    static_folder=FRONTEND_DIR,
    static_url_path="/static"
)

CORS(app)


# =====================================================
# LOAD MODEL
# =====================================================

if not os.path.exists(MODEL_PATH):

    raise FileNotFoundError(
        f"Model not found:\n{MODEL_PATH}"
    )


model = joblib.load(MODEL_PATH)

print("HOG + SVM model loaded successfully!")


# =====================================================
# IMAGE SETTINGS
# =====================================================

IMG_SIZE = (128, 128)


# =====================================================
# HOME PAGE
# =====================================================

@app.route("/")
def home():

    return send_from_directory(
        FRONTEND_DIR,
        "index.html"
    )


# =====================================================
# PREDICTION API
# =====================================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        # ---------------------------------------------
        # Check whether image was uploaded
        # ---------------------------------------------

        if "image" not in request.files:

            return jsonify({
                "success": False,
                "error": "No image uploaded."
            }), 400


        file = request.files["image"]


        # ---------------------------------------------
        # Check filename
        # ---------------------------------------------

        if file.filename == "":

            return jsonify({
                "success": False,
                "error": "No image selected."
            }), 400


        # ---------------------------------------------
        # Check extension
        # ---------------------------------------------

        allowed_extensions = (
            ".jpg",
            ".jpeg",
            ".png"
        )

        filename = file.filename.lower()


        if not filename.endswith(
            allowed_extensions
        ):

            return jsonify({
                "success": False,
                "error":
                    "Only JPG, JPEG and PNG images are allowed."
            }), 400


        # ---------------------------------------------
        # Load image
        # ---------------------------------------------

        image = Image.open(
            file.stream
        ).convert("L")


        print(
            "Original image size:",
            image.size
        )


        # ---------------------------------------------
        # Resize
        # ---------------------------------------------

        image = image.resize(
            IMG_SIZE
        )


        # ---------------------------------------------
        # Convert to NumPy
        # ---------------------------------------------

        image_array = np.array(
            image
        )


        print(
            "Processed image shape:",
            image_array.shape
        )


        # ---------------------------------------------
        # HOG FEATURE EXTRACTION
        # ---------------------------------------------

        hog_features = hog(

            image_array,

            orientations=9,

            pixels_per_cell=(8, 8),

            cells_per_block=(2, 2),

            block_norm="L2-Hys"
        )


        print(
            "HOG feature count:",
            len(hog_features)
        )


        # ---------------------------------------------
        # Reshape for SVM
        # ---------------------------------------------

        hog_features = hog_features.reshape(
            1,
            -1
        )


        # ---------------------------------------------
        # SVM PREDICTION
        # ---------------------------------------------

        prediction_value = model.predict(
            hog_features
        )[0]


        # ---------------------------------------------
        # Probability
        # ---------------------------------------------

        if hasattr(
            model,
            "predict_proba"
        ):

            probabilities = model.predict_proba(
                hog_features
            )[0]

        else:

            probabilities = None


        # ---------------------------------------------
        # Determine result
        # ---------------------------------------------

        if prediction_value == 1:

            result = "Tumor Detected"

            if probabilities is not None:

                score = float(
                    probabilities[1]
                )

            else:

                score = 1.0

        else:

            result = "No Tumor"

            if probabilities is not None:

                score = float(
                    probabilities[0]
                )

            else:

                score = 1.0


        score_percentage = round(
            score * 100,
            2
        )


        print(
            "Prediction:",
            result
        )

        print(
            "Probability:",
            score_percentage,
            "%"
        )


        # ---------------------------------------------
        # Return JSON
        # ---------------------------------------------

        return jsonify({

            "success": True,

            "prediction": result,

            "probability":
                score_percentage

        })


    except Exception as e:

        print(
            "Prediction error:",
            str(e)
        )


        return jsonify({

            "success": False,

            "error": str(e)

        }), 500


# =====================================================
# START SERVER
# =====================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=False

    )