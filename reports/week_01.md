# Week 1 Report  
## Sign Language Recognition Using Deep Learning

---

# 📌 Project Title

**Sign Language Recognition Using Deep Learning**

---

# 🎯 Week 1 Objective

The main goal of Week 1 was to explore and understand the ASL Alphabet dataset before starting deep learning model training.

This week focused on:

- downloading and extracting the dataset;
- understanding folder structure;
- analyzing class distribution;
- visualizing hand gesture images;
- checking image properties;
- preparing the project for preprocessing and CNN training.

---

# 📂 Dataset Information

For this project, I selected the **ASL Alphabet Dataset** from Kaggle.

Dataset Link:

https://www.kaggle.com/datasets/grassknoted/asl-alphabet

The dataset contains images of hand gestures representing letters from American Sign Language (ASL).

The dataset is organized into folders where each folder represents one gesture class.

Example:

```text
A/
B/
C/
...
Z/
space/
del/
nothing/
```

---

# 💡 Why I Chose This Dataset

I chose this dataset because it is more practical and visually interesting than a simple text classification project.

The project combines:

- Deep Learning;
- Computer Vision;
- Artificial Intelligence;
- Accessibility Technology.

This topic also has social importance because sign language recognition systems can potentially help improve communication accessibility.

Another reason for choosing this dataset is that it allows me to build a Streamlit demo application later in the project.

---

# 🛠 Work Completed During Week 1

During Week 1, I completed the following tasks:

## 1. Dataset Download

The dataset was downloaded directly from Kaggle using the Kaggle API inside Google Colab.

This method was significantly faster than manually uploading the ZIP file.

---

## 2. Dataset Extraction

The ZIP archive was extracted successfully into the project workspace.

After extraction, I inspected the dataset structure and located the main training folders.

---

## 3. Class Analysis

I identified all gesture classes included in the dataset.

The dataset contains:

- alphabet letters A–Z;
- additional gesture classes:
  - del
  - space
  - nothing

This makes the problem a multi-class image classification task.

---

## 4. Class Distribution Visualization

I counted the number of images inside each class folder and visualized the class distribution using graphs.

This analysis helped me understand whether the dataset is balanced.

From the visualization, the dataset appears relatively balanced, which is good for CNN training.

---

## 5. Image Visualization

I displayed sample images from different classes to better understand the visual structure of the dataset.

The images showed:

- different finger positions;
- hand shapes;
- gesture patterns;
- clean backgrounds.

This confirmed that the dataset is suitable for image classification.

---

## 6. Image Property Analysis

I checked:

- image size;
- image mode;
- image shape;
- pixel value range.

The dataset uses RGB images with pixel values ranging from 0 to 255.

I also found that image resizing will be required before CNN training.

---

# 📊 Key Findings

During Week 1, I discovered that:

- the dataset is well-structured;
- classes are stored in separate folders;
- the dataset is suitable for CNN-based deep learning;
- preprocessing will be required;
- image normalization will be important;
- data augmentation can improve model robustness.

---

# 🧠 Technical Skills Practiced

During this week, I practiced:

- dataset extraction;
- file system navigation in Python;
- image loading using PIL;
- visualization using Matplotlib and Seaborn;
- basic computer vision analysis;
- dataset inspection inside Google Colab.

---

# 🚀 Challenges Faced

One challenge during Week 1 was uploading large dataset files directly into Google Colab.

To solve this problem, I used the Kaggle API, which allowed me to download the dataset directly from Kaggle servers much faster.

Another challenge was identifying the correct dataset folder after extraction because the dataset contained many subfolders.

---

# 📅 Plan for Week 2

In Week 2, I plan to focus on preprocessing and data augmentation.

The next tasks include:

- image resizing;
- normalization;
- train-validation split;
- image generators;
- data augmentation;
- preparation for CNN training.

I will also visualize augmented images to better understand preprocessing effects.

---

# ✅ Week 1 Conclusion

Week 1 focused on understanding the ASL Alphabet dataset and preparing the project environment.

I successfully downloaded, extracted, explored, and visualized the dataset.

The dataset appears suitable for a deep learning computer vision project and provides a strong foundation for CNN model training in the next stages of the project.

The project is now ready for Week 2 preprocessing and augmentation.
