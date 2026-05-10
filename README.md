# Sign Language Recognition Dataset Guide

## Overview

This directory contains the dataset used for the **Sign Language Recognition using Deep Learning** project.

The goal of this project is to build an AI model that can recognize hand gestures representing letters from sign language. This project has social importance because sign language recognition can support accessibility and help communication between hearing and non-hearing people.

The task is an **image classification** problem.

---

## Dataset Source

**Dataset Name:** Sign Language MNIST  
**Source:** Kaggle  
**Dataset Link:** https://www.kaggle.com/datasets/datamunge/sign-language-mnist  
**Task Type:** Image Classification  
**Image Type:** Grayscale hand gesture images  
**Image Size:** 28 × 28 pixels  
**Format:** CSV files  

---

## Dataset Description

The dataset contains images of hand gestures representing letters from the American Sign Language alphabet.

Each image is stored as pixel values in CSV format.  
Every row represents one image.

Each image has:

- 784 pixel values;
- 1 label column;
- 28 × 28 grayscale structure.

The label represents the letter shown by the hand gesture.

---

## Files

Usually, the dataset contains two main files:

```text
sign_mnist_train.csv
sign_mnist_test.csv
```

| File | Description |
|---|---|
| sign_mnist_train.csv | Training dataset |
| sign_mnist_test.csv | Testing dataset |

---

## Data Structure

Each row contains:

| Column | Description |
|---|---|
| label | Class label of the hand gesture |
| pixel1 - pixel784 | Pixel values of the 28×28 image |

Example:

```text
label, pixel1, pixel2, pixel3, ..., pixel784
```

---

## Image Information

| Feature | Value |
|---|---|
| Image size | 28 × 28 |
| Color mode | Grayscale |
| Pixel range | 0–255 |
| Input shape for CNN | 28 × 28 × 1 |

---

## Project Task

The model receives a hand gesture image as input and predicts the corresponding sign language class.

Input:

```text
Hand gesture image
```

Output:

```text
Predicted sign language letter
```

---

## Why This Dataset Was Chosen

I chose this dataset because:

- it is suitable for deep learning;
- it is not too heavy for Google Colab or a laptop;
- it is good for CNN models;
- it has social importance;
- it can be used to build a simple digital assistant;
- it supports image preprocessing and augmentation;
- it is suitable for a Streamlit demo application.

---

## Planned Workflow

The project workflow:

```text
Dataset loading
      ↓
Exploratory Data Analysis
      ↓
Image preprocessing
      ↓
Data augmentation
      ↓
CNN model training
      ↓
Model evaluation
      ↓
Streamlit app demo
```

---

## Directory Structure

```text
data/
├── README.md
├── sign_mnist_train.csv
└── sign_mnist_test.csv
```


---

## Next Steps

After downloading the dataset:

1. Load train and test CSV files.
2. Check class distribution.
3. Visualize sample hand gesture images.
4. Normalize pixel values.
5. Reshape images for CNN.
6. Apply data augmentation.
7. Train CNN model.
8. Evaluate model performance.
9. Build Streamlit demo app.

---

