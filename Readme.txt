Brain Tumor Detection — HOG + SVM


-----------------------------Project workflow-----------------------------------


MRI Dataset
   ↓
Load Images
   ↓
Grayscale + Resize
   ↓
HOG Feature Extraction
   ↓
Train/Test Split
   ↓
SVM
   ↓
Accuracy + Classification Report
   ↓
Confusion Matrix
   ↓
Save Model
   ↓
Test New MRI Image



----------------------------------------------------------------------------------------

📱 Flutter Mobile App
        │
        │ MRI image
        ↓
🐍 Flask Backend
        │
        ├── Load hog_svm_model.pkl
        ├── Resize image
        ├── Grayscale
        ├── HOG extraction
        └── SVM prediction
        │
        ↓
📊 Result
   Tumor / No Tumor




----------------------------------------------------------------------------------------

| Component              | Used |
| ---------------------- | ---- |
| Dataset                | ✅    |
| Image preprocessing    | ✅    |
| Grayscale              | ✅    |
| Resize                 | ✅    |
| HOG feature extraction | ✅    |
| Train/Test split       | ✅    |
| **SVM**                | ✅    |
| Accuracy               | ✅    |
| Classification report  | ✅    |
| Confusion matrix       | ✅    |
| New-image prediction   | ✅    |
| Saved model            | ✅    |









-------------------------------------------------------------------------------------
STEP 1  → Setup Python environment                    ✅ DONE
STEP 2  → Dataset setup                              ✅ DONE
STEP 3  → Image preprocessing                        ✅ DONE
STEP 4  → HOG feature extraction                    ✅ DONE
STEP 5  → Train SVM                                  ✅ DONE
STEP 6  → Test SVM + accuracy                        ✅ DONE
STEP 7  → Save HOG + SVM model                       ✅ DONE
STEP 8  → Create Flask backend                       ✅ DONE
STEP 9  → Test Flask API                             ✅ DONE

STEP 10 → Create HTML/CSS/JS frontend                ⏳
STEP 11 → Connect frontend to Flask `/predict`      ⏳
STEP 12 → Upload MRI from website                    ⏳
STEP 13 → Display prediction                         ⏳
STEP 14 → Display model probability                  ⏳
STEP 15 → Add validation/error handling              ⏳
STEP 16 → Improve UI                                 ⏳
STEP 17 → Test complete application                  ⏳
STEP 18 → Prepare project/report/resume              ⏳

-----------------------------------------------------------------------------
D:\BrainTumorDetection
│
├── Backend
│   └── app.py
│
├── model
│   └── hog_svm_model.pkl
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── Brain_Tumor_HOG_SVM.ipynb
│
└── venv

----------------------------------------------------------------------------
             USER
               │
               ↓
       ┌─────────────────┐
       │   Upload MRI    │
       └────────┬────────┘
                ↓
       ┌─────────────────┐
       │  MRI Preview    │
       └────────┬────────┘
                ↓
       ┌─────────────────┐
       │  Analyze MRI    │
       └────────┬────────┘
                ↓
          Flask Backend
                ↓
             HOG
                ↓
              SVM
                ↓
       ┌────────┴─────────┐
       ↓                  ↓
   NO TUMOR             TUMOR
   98.40%               91.11%
   -----------------------------------------------------------------------------

   