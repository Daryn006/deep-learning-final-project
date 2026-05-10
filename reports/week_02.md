# Week 2 Report  
## Sign Language Recognition Using Deep Learning

---

# 📌 Project Title

**Sign Language Recognition Using Deep Learning**

---

# 🎯 Week 2 Objective

The main goal of Week 2 was to preprocess the ASL Alphabet dataset and prepare it for deep learning model training.

This week focused on:

- loading the image dataset;
- resizing images;
- normalizing pixel values;
- creating training and validation generators;
- applying data augmentation;
- visualizing preprocessing results;
- preparing the dataset pipeline for CNN training.

---

# 📂 Dataset Used

For this project, I used the **ASL Alphabet Dataset** from Kaggle.

Dataset Link:

https://www.kaggle.com/datasets/grassknoted/asl-alphabet

The dataset contains hand gesture images representing American Sign Language letters and additional gesture classes.

The dataset is organized into separate folders where each folder represents one gesture class.

---

# 🛠 Work Completed During Week 2

---

# 1. Dataset Preparation

The dataset was downloaded directly from Kaggle using the Kaggle API inside Google Colab.

This method was much faster than manually uploading large ZIP files.

After downloading, the dataset archive was extracted successfully into the working environment.

---

# 2. Dataset Path Detection

I searched through the extracted dataset folders and identified the correct training dataset directory.

The final dataset path contained folders for:

```text
A, B, C, ..., Z, del, nothing, space
```

This confirmed that the dataset is suitable for multi-class image classification.

---

# 3. Image Size Selection

Before training a CNN model, all images must have the same dimensions.

For this project, I selected:

```text
64 × 64
```

This image size provides a good balance between:

- training speed;
- memory usage;
- visual detail retention.

---

# 4. Data Normalization

The original pixel values ranged from:

```text
0 → 255
```

During preprocessing, all images were normalized into the range:

```text
0 → 1
```

using:

```python
rescale = 1./255
```

Normalization is important because neural networks train more efficiently on smaller numerical ranges.

---

# 5. Data Augmentation

One of the most important parts of Week 2 was data augmentation.

I applied several augmentation techniques:

- rotation;
- zoom;
- width shifting;
- height shifting;
- brightness variation.

These transformations create multiple modified versions of the same image.

This helps the model become more robust and reduces overfitting.

---

# 6. Training and Validation Split

I used `ImageDataGenerator` with:

```text
validation_split = 0.2
```

This automatically split the dataset into:

- training data;
- validation data.

The training dataset is used for learning, while the validation dataset helps evaluate model performance during training.

---

# 7. Generator Creation

I created:

- `train_generator`
- `validation_generator`

These generators automatically:

- load images from folders;
- resize images;
- normalize images;
- create batches;
- apply augmentation during training.

This creates an efficient deep learning pipeline.

---

# 8. Visualization of Augmented Images

I visualized several augmented versions of ASL gesture images.

This helped me understand how the model will see slightly modified gesture variations during training.

The visualization also confirmed that augmentation is working correctly.

---

# 📊 Key Findings

During Week 2, I discovered that:

- preprocessing is essential before CNN training;
- normalized images are easier for neural networks to process;
- augmentation creates more diverse training data;
- image generators simplify dataset handling;
- the dataset structure works very well with TensorFlow generators.

---

# 🧠 Technical Skills Practiced

During Week 2, I practiced:

- image preprocessing;
- TensorFlow image generators;
- data normalization;
- dataset splitting;
- data augmentation;
- image visualization;
- CNN input preparation.

---

# ⚠ Challenges Faced

During Week 2, I experienced several technical challenges.

The first issue was related to dataset path detection because the dataset contained multiple nested folders.

Another challenge involved visualizing augmented images correctly.  
Some images appeared extremely dark or overexposed during early testing, so I adjusted the visualization pipeline.

I also encountered issues with undefined variables such as:

```python
IMG_SIZE
BATCH_SIZE
SEED
```

These problems were fixed by properly organizing notebook cells.

---

# 🚀 Why Week 2 Is Important

Week 2 is one of the most important stages of the project because preprocessing directly affects model quality.

Even a strong CNN architecture may perform poorly if the preprocessing pipeline is weak.

By preparing the dataset correctly now, the model training process in Week 3 will become more stable and accurate.

---

# 📅 Plan for Week 3

In Week 3, I will begin CNN model training.

The next tasks include:

- building a custom CNN architecture;
- training the model;
- tracking accuracy and loss;
- evaluating performance;
- creating confusion matrices;
- saving the trained model.

I also plan to compare different CNN approaches if time allows.

---

# ✅ Week 2 Conclusion

Week 2 focused on preparing the ASL Alphabet dataset for deep learning.

I successfully:

- normalized the images;
- resized the dataset;
- created training and validation generators;
- applied data augmentation;
- visualized augmented samples;
- prepared the dataset pipeline for CNN training.

The project is now fully ready for Week 3 model development and training.
