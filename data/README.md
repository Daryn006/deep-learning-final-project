# Dataset Information

## About This Folder

This folder contains the dataset resources used in the **Sign Language Recognition using Deep Learning** project.

The dataset is based on images of hand gestures from the American Sign Language (ASL) alphabet.

These images are used to train a deep learning model capable of recognizing sign language letters from visual input.

---

# 📌 Dataset Used

For this project, I selected the following dataset:

**ASL Alphabet Dataset**

Source:

https://www.kaggle.com/datasets/grassknoted/asl-alphabet

The dataset was downloaded from Kaggle and extracted locally for preprocessing and CNN model training.

---

# 🖼 Dataset Content

The dataset contains thousands of hand gesture images representing different ASL letters.

Each folder corresponds to one class.

Example:

```text
A/
B/
C/
D/
...
Z/
space/
nothing/
del/
```

Each image belongs to one gesture category.

---

# 📊 Dataset Characteristics

| Property | Value |
|---|---|
| Data Type | Image Dataset |
| Problem Type | Multi-Class Classification |
| Classes | 29 |
| Image Format | JPG |
| Color Type | RGB |
| Main Task | Sign Language Recognition |

---

# 🧠 What The Model Learns

Using this dataset, the model learns:

- hand shapes;
- finger positions;
- gesture patterns;
- visual differences between letters.

The final goal is for the model to predict the correct sign language gesture from an uploaded image.

---

# 🛠 How The Dataset Will Be Used

The dataset will be used for:

- exploratory data analysis;
- image preprocessing;
- image normalization;
- data augmentation;
- CNN model training;
- model evaluation;
- Streamlit application testing.

---

# 🔄 Planned Image Processing

Before training the model, the images will go through several preprocessing stages:

```text
Image Loading
      ↓
Resizing
      ↓
Normalization
      ↓
Data Augmentation
      ↓
CNN Training
```

---

# 🎯 Why This Dataset Is Suitable

This dataset is suitable for the project because:

- it contains real gesture images;
- it is compatible with CNN architectures;
- it supports computer vision tasks;
- it allows augmentation techniques;
- it is visually understandable;
- it has practical and social value.

---

# 📁 Dataset Folder Structure

Expected structure:

```text
data/
├── README.md
├── asl_alphabet_train/
├── asl_alphabet_test/
└── dataset.zip
```

Depending on extraction settings, folder names may differ slightly.

---

# ⚠ Important Note

Raw dataset files are not uploaded directly to GitHub because image datasets are too large.

Instead, this README provides:

- dataset description;
- dataset source;
- project usage explanation.

