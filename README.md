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

Layer Tool/Framework Purpose
Model TensorFlow + MobileNetV2 Lightweight image classification
Real-time App OpenCV + Gradio Webcam frame capture + UI
Deployment Hugging Face Spaces Public demo hosting
DevOps Git + GitHub Actions (opt) CI/CD for deployment
Monitoring Streamlit (optional) Live usage & accuracy

dashboard 

