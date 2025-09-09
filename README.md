## Project Title: 

### Waste Classification for Smart Recycling in UK Cities

## Project Overview:

The project focuses on developing a real-time computer vision system for waste classification using image input interface. The goal is to support smart recycling systems by classifying common waste types( e.g plastic, paper, metal, food).

A lightweight **MobileNetV2 model** was fine-tune using the open-source **TACO dataset**, and integrated into a **real-time Gradio interface**. The final application is deployed on Hugging Face Space, enabling public demos without specialized hardware. 

### Business Problems Addressed:

* ~22% of recyclable materials are rejected due to contamination from incorrect disposal
* Lack of user awareness ata the disposal moment
* Inconsistent recycling compliance across different city locations
* Need for public-facing demos to engage stakeholders and city councils

### Steps follows in Project building

* Train an image classification model (MobileNetV2) on 6+ waste categories
* Build a real-time classifier using OpenCV and Gradio
* Deploy the model on Hugging Face Spaces
* Provide real-time feedback and visual UI for users
* Ensure robustness across varying lighting and object shapes

### ️🛠️Tech Stack & Tools:


* Model -> TensorFlow + MobileNetV2 it's a Lightweight image classification
* Real-time App -> OpenCV + Gradio for Webcam frame capture and UI
* Deployment -> Hugging Face Spaces free open-source Public demo hosting
* DevOps -> Git + GitHub CI/CD for deployment
* Monitoring -> Streamlit for Live usage & accuracy dashboard

### Dataset Description

**Source**: TACO (Trash Annotations in Contex)

* images: Urban waste photos from public bins
* annotations: COCO-style bounding boxes and labels
* categories: Plastic, paper, metal, glass, food, cardboard

### 🔁Workflow Summary

**1. Data Preparation**
   * Ingest and clean TACO dataset
   * Resize, flip, and augment images for better generalization
   * Convert labels to appropriate training format

**2. Model Training**
   * Fine-tune MobileNetV2 on selected waste classes
   *Evaluate using F1 score, accuracy, and confusion matrix
   *(Optional) Export to TensorFlow Lite for edge deployment

**3. Real-Time App Integration**
  * Capture live webcam frames using cv2.VideoCapture()
  * Preprocess each frame to match model input size
  * Pass frames to the trained model for prediction
  * Display class label live using cv2.putText() and Gradio

**4. Deployment**
  * Host Gradio interface on Hugging Face Spaces
  * Export model (.h5 or .onnx)
  * Optional GitHub Actions for CI/CD pipeline

### Project Impacts

* Real-time sorting guidance for the public via smart bins
* Reduced contamination in city waste streams
* Actionable data for city councils through analytics dashboards
* Increased awareness and behavioral change in waste disposal habits

### ✅Key Delivarables:

* Cleaned and augmented TACO dataset
* Trained MobileNetV2 model (.h5 or .tflite)
* Gradio app with webcam input and real-time prediction
* Public deployment on Hugging Face Spaces
* Final strategy report with recommendations

