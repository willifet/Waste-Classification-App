import gradio as gr
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

# Load your trained model
model = tf.keras.models.load_model("waste classification model.h5", custom_objects={'KerasLayer': hub.KerasLayer})

# Define your waste class labels
class_names = ['batteries', 'clothes', 'e-waste', 'glass', 'light blubs',
               'metal', 'organic', 'paper', 'plastic']
IMG_SIZE = 224

# Image preprocessing function
def preprocess_image(image):
    image = tf.convert_to_tensor(image, dtype=tf.float32)
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE)) / 255.0
    return tf.expand_dims(image, axis=0)

# Prediction function
def predict_waste(image):
    processed = preprocess_image(image)
    preds = model.predict(processed)
    label = class_names[np.argmax(preds)]
    confidence = float(np.max(preds))
    return f"{label} ({confidence:.2f})"

# Example images – update these paths with actual examples in your Colab space
examples = [
    ["examples/Zeitungen-und-Zeitschriften.png"],
    ["examples/hazardous-toxic-electronic-waste-mixture-260nw-1593448036.jpg"],
    ["examples/composting_medium-size.jpg"],
    ["examples/zero-waste-recycling-wooden-thing-wooden-background-zero-waste-recycling-wooden-thing-wooden-background-flat-lay-158056259.jpg"],
    ["examples/plastic waste.png"]
     ]


# Launch Gradio Interface
iface = gr.Interface(
    fn=predict_waste,
    inputs=gr.Image(type="numpy", label="Upload a Waste Image"),
    outputs="text",
    title="Waste Classification Model 🌱",
    description="Upload an image of a waste item to classify it as one of 9 categories.",
    examples=examples
)

iface.launch()