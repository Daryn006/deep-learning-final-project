# Week 3 Report — CNN Model Training and Evaluation

## Project
Sign Language Recognition Using Deep Learning

---

# Overview

During Week 3, the main focus of the project was building, training, and evaluating a Convolutional Neural Network (CNN) model for American Sign Language (ASL) alphabet recognition.

The goal of this stage was to create a deep learning model capable of classifying hand gesture images into the correct ASL letter classes.

This week represents the core deep learning phase of the project.

---

# Tasks Completed

## 1. Dataset Preparation

The ASL Alphabet dataset was downloaded from Kaggle and extracted in Google Colab.

Dataset:
- ASL Alphabet Dataset
- Source: Kaggle
- Author: grassknoted

The dataset contains hand gesture images representing:
- A–Z letters
- del
- nothing
- space

Total classes:
- 29 classes

---

## 2. Image Preprocessing

The dataset images were preprocessed before training.

### Preprocessing steps:
- image resizing to 64×64;
- normalization using rescale = 1./255;
- train-validation split;
- batch generation.

Preprocessing helps improve model stability and training efficiency.

---

## 3. Data Augmentation

Image augmentation techniques were applied to improve model generalization.

### Augmentation methods:
- rotation;
- zoom;
- width shifting;
- height shifting;
- brightness adjustment.

These techniques help the model become more robust to different hand positions and lighting conditions.

---

# CNN Model Development

A Convolutional Neural Network (CNN) architecture was created using TensorFlow and Keras.

## Model Structure

The CNN model included:
- convolutional layers;
- max pooling layers;
- flatten layer;
- dense layers;
- dropout regularization;
- softmax output layer.

The final output layer contains 29 neurons because the dataset has 29 gesture classes.

---

# Model Training

The model was trained using:
- Adam optimizer;
- categorical crossentropy loss;
- accuracy evaluation metric.

Additional techniques:
- EarlyStopping;
- ModelCheckpoint.

The model was trained for 10 epochs.

---

# Model Evaluation

After training, the model was evaluated using:
- validation accuracy;
- validation loss;
- accuracy graph;
- loss graph;
- confusion matrix;
- classification report.

The evaluation helped analyze:
- model performance;
- classification quality;
- prediction errors;
- confusing gesture classes.

---

# Files Generated

During Week 3, the following files were generated:

## Models
- `models/asl_cnn_model.h5`
- `models/asl_cnn_final_model.h5`

## Results
- `results/accuracy_plot.png`
- `results/loss_plot.png`
- `results/confusion_matrix.png`

---

# Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Seaborn
- Google Colab

---

# Challenges Faced

One challenge was configuring the correct dataset path after downloading the dataset from Kaggle.

Another challenge was the long training time due to the large number of images in the dataset.

---

# Conclusion

Week 3 was focused on the main deep learning implementation of the project.

By the end of the week:
- a CNN model was successfully trained;
- the model was evaluated using multiple metrics;
- graphs and confusion matrix were generated;
- trained models were saved.

The project is now ready for the next stage, where a Streamlit application will be developed for real-time user interaction.

---

# Next Step

Week 4 will focus on:
- Streamlit application development;
- user image upload;
- prediction interface;
- model deployment testing.
