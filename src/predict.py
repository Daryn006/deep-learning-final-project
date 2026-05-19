import numpy as np
from PIL import Image
import tensorflow as tf

CLASS_NAMES = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z",
    "del", "nothing", "space"
]

# Load trained CNN model
def load_asl_model(model_path="models/asl_cnn_final_model.h5"):
    model = tf.keras.models.load_model(model_path)
    return model

# Preprocess uploaded image
def preprocess_image(image, img_size=64):

    image = image.convert("RGB")
    image = image.resize((img_size, img_size))

    image_array = np.array(image)
    image_array = image_array / 255.0

    image_array = np.expand_dims(image_array, axis=0)

    return image_array

# Predict ASL sign
def predict_sign(image, model):

    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image)

    predicted_index = np.argmax(prediction)

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = float(np.max(prediction)) * 100

    return predicted_class, confidence
