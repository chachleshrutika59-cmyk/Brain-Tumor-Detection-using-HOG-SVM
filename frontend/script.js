// ========================================
// Brain Tumor Detection
// Frontend JavaScript
// ========================================


// Flask API address

const API_URL = "/predict";


// Get HTML elements

const imageInput =
    document.getElementById("imageInput");

const imagePreview =
    document.getElementById("imagePreview");

const previewPlaceholder =
    document.getElementById("previewPlaceholder");

const analyzeButton =
    document.getElementById("analyzeButton");

const loading =
    document.getElementById("loading");

const errorMessage =
    document.getElementById("errorMessage");

const resultContainer =
    document.getElementById("resultContainer");

const resultIcon =
    document.getElementById("resultIcon");

const prediction =
    document.getElementById("prediction");

const probability =
    document.getElementById("probability");

const probabilityBar =
    document.getElementById("probabilityBar");


// ========================================
// IMAGE SELECTION
// ========================================

imageInput.addEventListener("change", function () {

    // Reset previous result

    resultContainer.style.display = "none";

    errorMessage.style.display = "none";


    // Check if file selected

    if (this.files.length === 0) {

        analyzeButton.disabled = true;

        imagePreview.style.display = "none";

        previewPlaceholder.style.display = "block";

        return;
    }


    const file = this.files[0];


    // Check file type

    const allowedTypes = [
        "image/jpeg",
        "image/png"
    ];


    if (!allowedTypes.includes(file.type)) {

        showError(
            "Please select a JPG, JPEG or PNG image."
        );

        this.value = "";

        analyzeButton.disabled = true;

        return;
    }


    // Show image preview

    const reader = new FileReader();


    reader.onload = function (event) {

        imagePreview.src =
            event.target.result;

        imagePreview.style.display =
            "block";

        previewPlaceholder.style.display =
            "none";

    };


    reader.readAsDataURL(file);


    // Enable button

    analyzeButton.disabled = false;

});


// ========================================
// ANALYZE BUTTON
// ========================================

analyzeButton.addEventListener(
    "click",
    analyzeImage
);


// ========================================
// ANALYZE IMAGE FUNCTION
// ========================================

async function analyzeImage() {

    // Make sure image exists

    if (imageInput.files.length === 0) {

        showError(
            "Please select an MRI image first."
        );

        return;
    }


    const file =
        imageInput.files[0];


    // Create FormData

    const formData =
        new FormData();


    formData.append(
        "image",
        file
    );


    // UI state

    loading.style.display =
        "block";

    analyzeButton.disabled =
        true;

    errorMessage.style.display =
        "none";

    resultContainer.style.display =
        "none";


    try {

        // Send image to Flask

        const response =
            await fetch(
                API_URL,
                {
                    method: "POST",
                    body: formData
                }
            );


        // Convert response to JSON

        const data =
            await response.json();


        // Check server response

        if (!response.ok || !data.success) {

            throw new Error(
                data.error ||
                "Prediction failed."
            );
        }


        // Display result

        displayResult(
            data.prediction,
            data.probability
        );


    }

    catch (error) {

        console.error(error);

        showError(
            "Unable to connect to the Flask server. " +
            "Make sure app.py is running on port 5000."
        );

    }

    finally {

        loading.style.display =
            "none";

        analyzeButton.disabled =
            false;
    }

}


// ========================================
// DISPLAY RESULT
// ========================================

function displayResult(
    result,
    score
) {

    resultContainer.style.display =
        "block";


    const scoreValue =
        Number(score);


    probability.textContent =
        scoreValue.toFixed(2) + "%";


    probabilityBar.style.width =
        scoreValue + "%";


    // Tumor

    if (
        result.toLowerCase()
            .includes("tumor detected")
    ) {

        resultIcon.textContent =
            "🔴";

        prediction.textContent =
            "TUMOR DETECTED";

    }


    // No Tumor

    else {

        resultIcon.textContent =
            "🟢";

        prediction.textContent =
            "NO TUMOR";

    }

}


// ========================================
// ERROR MESSAGE
// ========================================

function showError(message) {

    errorMessage.textContent =
        message;

    errorMessage.style.display =
        "block";

}