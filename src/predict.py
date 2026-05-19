import numpy as np
from PIL import Image
import tensorflow as tf


CLASS_NAMES = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z",
    "del", "nothing", "space"
]


def load_asl_model(model_path="models/asl_cnn_final_model.h5"):
    model = tf.keras.models.load_model(model_path)
    return model


def preprocess_image(image, img_size=64):
    image = image.convert("RGB")
    image = image.resize((img_size, img_size))

    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    return image_array


def predict_asl_sign(model, image):
    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image, verbose=0)

    predicted_index = int(np.argmax(prediction))
    predicted_class = CLASS_NAMES[predicted_index]
    confidence = float(np.max(prediction) * 100)

    top_3_indexes = prediction[0].argsort()[-3:][::-1]

    top_3 = []

    for index in top_3_indexes:
        top_3.append({
            "class": CLASS_NAMES[index],
            "confidence": float(prediction[0][index] * 100)
        })

    return predicted_class, confidence, top_3
