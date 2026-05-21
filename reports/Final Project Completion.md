# Week 4 Report — Final Project Completion

## Student Information

| Field | Information |
|---|---|
| Student Name | Daryn |
| Project Title | Sign Language Recognition Using Deep Learning |
| Course | Deep Learning |
| Project Type | Computer Vision / Image Classification |
| Desired Grade | A / 100% |

---

## Executive Summary

During Week 4, I finalized the complete deep learning project for American Sign Language recognition.

The project was improved from a basic CNN notebook into a complete AI prototype with model comparison, advanced evaluation, and Streamlit deployment.

The final system can classify ASL gesture images into 29 classes and display predictions through an interactive web interface.

---

## Key Week 4 Deliverables

| Deliverable | Status |
|---|---|
| Final Google Colab notebook | Completed |
| Dataset preprocessing | Completed |
| Data augmentation | Completed |
| Custom CNN model | Completed |
| MobileNetV2 transfer learning model | Completed |
| Model comparison | Completed |
| Advanced evaluation metrics | Completed |
| Confusion matrix | Completed |
| Classification report | Completed |
| Error analysis | Completed |
| Streamlit application | Completed |
| GitHub project organization | Completed |

---

## 1. Final Notebook Completion

The final notebook was created in Google Colab.

Notebook file:

```text
notebooks/Final Deep Learning Project.ipynb
```

The notebook includes the full project pipeline:

- project overview;
- dataset information;
- Kaggle dataset download;
- image preprocessing;
- data augmentation;
- Custom CNN model;
- MobileNetV2 transfer learning model;
- model training;
- model comparison;
- model evaluation;
- prediction testing;
- confusion matrix;
- classification report;
- error analysis;
- Streamlit explanation;
- final conclusion.

Each code block contains comments, making the notebook easier to understand and explain during project defense.

---

## 2. Dataset Information

The project uses the ASL Alphabet Dataset from Kaggle.

Dataset link:

```text
https://www.kaggle.com/datasets/grassknoted/asl-alphabet
```

The dataset contains images representing:

- letters A–Z;
- del;
- nothing;
- space.

Total number of classes:

```text
29 classes
```

This dataset was used for a multi-class image classification task.

---

## 3. Image Preprocessing

Several preprocessing techniques were applied before training:

- image resizing to 128×128;
- normalization of pixel values from 0–255 to 0–1;
- RGB image conversion;
- train-validation split;
- batch generation.

Image preprocessing helped standardize the input data and improve model training stability.

---

## 4. Data Augmentation

Data augmentation was applied only to the training dataset.

The following augmentation techniques were used:

- rotation;
- zoom;
- width shifting;
- height shifting;
- brightness adjustment.

These techniques helped the model learn more robust ASL gesture patterns under different visual conditions.

Validation data was not augmented. Only rescaling was applied to validation data.

This was done to avoid data leakage and make evaluation more realistic.

---

## 5. Custom CNN Model

The first model was a Custom Convolutional Neural Network.

The architecture contains:

- Conv2D layers;
- BatchNormalization layers;
- MaxPooling2D layers;
- Flatten layer;
- Dense layer;
- Dropout layer;
- Softmax output layer.

CNN was selected because it is effective for image classification and can automatically learn visual features such as hand shapes, finger positions, and gesture patterns.

Dropout was used to reduce overfitting.

BatchNormalization was used to improve training stability.

---

## 6. MobileNetV2 Transfer Learning Model

To improve the project level, MobileNetV2 was added as a transfer learning model.

MobileNetV2 was selected because it is:

- lightweight;
- fast;
- suitable for mobile applications;
- effective for image classification;
- useful for real-time AI systems.

The pretrained ImageNet base was frozen, and a custom classification head was added for ASL recognition.

Transfer learning helps the model reuse pretrained visual features such as edges, textures, and shapes.

---

## 7. Hyperparameter Tuning

Several hyperparameters were tested manually.

| Parameter | Values Tested | Final Choice |
|---|---:|---:|
| Image size | 64, 128 | 128 |
| Batch size | 16, 32 | 32 |
| Learning rate | 0.001, 0.0001 | 0.0001 |
| Dropout | 0.3, 0.5 | 0.5 |
| Optimizer | SGD, Adam | Adam |

The final values were selected based on validation accuracy and validation loss.

A smaller learning rate helped the model train more stably.

---

## 8. Model Training

Both models were trained using ASL hand gesture images.

Models trained:

- Custom CNN;
- MobileNetV2 Transfer Learning.

The training process included:

```python
model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=10
)
```

During training, the models learned:

- finger positions;
- hand shapes;
- gesture structures;
- visual differences between ASL classes.

The best model was saved as:

```text
models/best_asl_model.keras
```

---

## 9. Model Comparison

Two models were compared:

- Custom CNN;
- MobileNetV2.

The models were compared using:

- Accuracy;
- Loss;
- Precision;
- Recall;
- F1-score.

Example comparison table:

| Model | Accuracy | Loss | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|---:|
| Custom CNN | 0.841897 | 0.805794 | 0.862590 | 0.841897 | 0.840506 |
| MobileNetV2 | 0.823563 | 0.574871 | 0.843827 | 	0.823563 |  |

The comparison helps identify which model performs better and generalizes better on validation data.

---

## 10. Model Evaluation Metrics

The final model was evaluated using both general and class-level metrics.

| Metric | Meaning |
|---|---|
| Accuracy | Overall percentage of correct predictions |
| Loss | Model error |
| Precision | Correctness of predicted classes |
| Recall | Ability to find real class examples |
| F1-score | Balance between precision and recall |
| Confusion Matrix | Class-by-class error analysis |

Accuracy alone is not enough for evaluating a multi-class classification model.

Therefore, precision, recall, F1-score, and confusion matrix were also used.
## Model Evaluation Results

The final model was evaluated using precision, recall, F1-score, and support for each ASL class.

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| A | 0.9982 | 0.9467 | 0.9718 | 600 |
| B | 0.7576 | 1.0000 | 0.8621 | 600 |
| C | 0.9569 | 1.0000 | 0.9780 | 600 |
| D | 0.9930 | 0.9417 | 0.9666 | 600 |
| E | 0.7541 | 0.9867 | 0.8549 | 600 |
| F | 1.0000 | 0.9933 | 0.9967 | 600 |
| G | 0.9591 | 0.9383 | 0.9486 | 600 |
| H | 0.9310 | 0.9450 | 0.9380 | 600 |
| I | 1.0000 | 0.6083 | 0.7565 | 600 |
| J | 0.9335 | 0.8650 | 0.8979 | 600 |
| K | 1.0000 | 0.9100 | 0.9529 | 600 |
| L | 0.9983 | 1.0000 | 0.9992 | 600 |
| M | 0.5334 | 0.9317 | 0.6784 | 600 |
| N | 0.6659 | 0.4883 | 0.5635 | 600 |
| O | 0.9979 | 0.7767 | 0.8735 | 600 |
| P | 0.8420 | 0.9950 | 0.9121 | 600 |
| Q | 0.9876 | 0.7933 | 0.8799 | 600 |
| R | 0.6934 | 0.8367 | 0.7583 | 600 |
| S | 0.7297 | 0.2700 | 0.3942 | 600 |
| T | 1.0000 | 0.7750 | 0.8732 | 600 |
| U | 0.5019 | 0.6483 | 0.5658 | 600 |
| V | 0.7251 | 0.8967 | 0.8018 | 600 |
| W | 0.6592 | 0.6867 | 0.6727 | 600 |
| X | 0.5000 | 0.5500 | 0.5238 | 600 |
| Y | 0.9693 | 0.8417 | 0.9010 | 600 |
| Z | 0.9962 | 0.8633 | 0.9250 | 600 |
| del | 0.9404 | 0.9733 | 0.9566 | 600 |
| nothing | 0.9983 | 1.0000 | 0.9992 | 600 |
| space | 0.9931 | 0.9533 | 0.9728 | 600 |

### Overall Results

| Metric | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Accuracy | 0.8419 | 0.8419 | 0.8419 | 17400 |
| Macro Avg | 0.8626 | 0.8419 | 0.8405 | 17400 |
| Weighted Avg | 0.8626 | 0.8419 | 0.8405 | 17400 |

### Result Interpretation

The model achieved an overall accuracy of **84.19%** on the validation dataset.

The best-performing classes were:

- F
- L
- nothing
- C
- A
- space

These classes achieved very high precision, recall, and F1-score.

The weaker classes were:

- S
- X
- N
- U
- W
- M

These results show that the model has difficulty with visually similar ASL signs. For example, letters such as **M**, **N**, **S**, **T**, **U**, **V**, **W**, and **X** may have similar finger positions or hand shapes.

To improve these results in the future, the project can use:

- more real-world ASL images;
- better lighting variation;
- stronger data augmentation;
- hand detection with MediaPipe or YOLO;
- transfer learning fine-tuning;
- real-time webcam testing.
---

## 11. Classification Report

A classification report was generated for all ASL classes.

The report includes:

- precision;
- recall;
- F1-score;
- support.

This helps analyze the model performance for every individual class.

Some ASL signs are easier to recognize because their hand shapes are visually unique.

Other signs are more difficult because they look similar.

---

## 12. Confusion Matrix

A confusion matrix was created to analyze prediction behavior across all classes.

Generated file:

```text
results/confusion_matrix.png
```

The confusion matrix helped identify which ASL gestures were predicted correctly and which classes were confused with each other.

---

## 13. Error Analysis

The confusion matrix was used to analyze model mistakes.

Some ASL signs are difficult because they look visually similar.

Examples of difficult classes:

- M;
- N;
- S;
- T;
- U;
- V;
- W.

These signs can be confused because they have similar hand shapes or finger positions.

Possible reasons for errors:

- similar hand gestures;
- similar finger positions;
- lighting differences;
- camera angle;
- hand rotation;
- image quality;
- background noise.

To reduce these errors, the project used:

- data augmentation;
- dropout;
- BatchNormalization;
- transfer learning;
- model comparison.

---

## 14. Overfitting Analysis

Training accuracy and validation accuracy were compared to check generalization.

If training accuracy is much higher than validation accuracy, the model may be overfitting.

To reduce overfitting, this project used:

- data augmentation;
- dropout;
- BatchNormalization;
- validation monitoring.

These techniques helped the model perform better on unseen images.

---

## 15. Accuracy and Loss Visualization

Accuracy and loss graphs were generated during evaluation.

Generated files:

```text
results/accuracy_plot.png
results/loss_plot.png
```

These graphs help analyze:

- training progress;
- validation performance;
- learning stability;
- possible overfitting.

---

## 16. Single Image Prediction

The trained model was tested on individual ASL test images.

The prediction pipeline included:

1. image loading;
2. image resizing to 128×128;
3. normalization;
4. prediction;
5. predicted class output;
6. confidence calculation.

Example output:

```text
Predicted Class: A
Confidence: 98.45%
```

---

## 17. Streamlit Web Application

A Streamlit web application was developed to make the project interactive.

Main application file:

```text
app.py
```

The application allows users to:

- upload ASL gesture images;
- run model predictions;
- view the predicted ASL letter;
- see prediction confidence.

The application can be run locally using:

```bash
streamlit run app.py
```

The web application makes the project more practical and closer to a real AI product.

---

## 18. Prediction Helper File

A separate helper file was created:

```text
src/predict.py
```

This file handles:

- model loading;
- image preprocessing;
- prediction logic;
- confidence score generation.

Separating prediction logic improved project organization, readability, and maintainability.

---

## 19. Final Project Structure

Final repository structure:

```text
deep-learning-final-project/
├── data/
├── models/
│   ├── best_asl_model.keras
│   └── class_names.json
├── notebooks/
│   ├── Week_1_Exploratory_Data_Analysis.ipynb
│   ├── Week_2_Image_Preprocessing.ipynb
│   ├── Week_3_CNN_Model_Training.ipynb
│   ├── Week_4_Project_ASL_Recognition.ipynb
│   └── Final Deep Learning Project.ipynb
├── reports/
│   ├── week_01.md
│   ├── week_02.md
│   ├── week_03.md
│   ├── week_04.md
│   └── Final Project Completion.md
├── results/
│   ├── accuracy_plot.png
│   ├── loss_plot.png
│   ├── confusion_matrix.png
│   ├── model_comparison_accuracy.png
│   └── classification_report.csv
├── src/
│   └── predict.py
├── app.py
├── requirements.txt
├── README.md
├── project-proposal.md
└── .gitignore
```

---

## 20. Technologies Used

The project used the following technologies:

- Python;
- Google Colab;
- TensorFlow;
- Keras;
- NumPy;
- Pandas;
- Matplotlib;
- Scikit-learn;
- Pillow;
- Streamlit;
- GitHub;
- VS Code.

---

## 21. Challenges Faced

Several technical challenges were faced during Week 4.

### Model Compile Error

Initially, model training produced an error because the model must be compiled before training.

This was fixed by running:

```python
model.compile()
```

before:

```python
model.fit()
```

### Input Shape Issue

The image size and model input shape had to be consistent.

The final version uses:

```text
128×128 image size
```

and:

```python
input_shape=(128, 128, 3)
```

### Data Leakage Prevention

Validation data was kept clean and was not augmented.

This improved the reliability of validation results.

### GitHub File Organization

The repository structure required proper organization of:

- notebooks;
- reports;
- model files;
- result images;
- Streamlit application files.

---

## 22. Final Result

By the end of Week 4, the project became a complete deep learning application.

Final project components:

- final Google Colab notebook;
- Custom CNN model;
- MobileNetV2 transfer learning model;
- saved best model file;
- evaluation metrics;
- model comparison;
- accuracy graph;
- loss graph;
- confusion matrix;
- classification report;
- error analysis;
- prediction testing;
- Streamlit application;
- organized GitHub repository.

The project demonstrates a practical AI system for recognizing American Sign Language gestures.

---

## 23. Conclusion

This project demonstrated the complete deep learning workflow:

```text
Dataset → Preprocessing → Data Augmentation → Custom CNN → MobileNetV2 → Evaluation → Error Analysis → Prediction → Streamlit App
```

The project improved practical understanding of:

- computer vision;
- image preprocessing;
- CNN architectures;
- transfer learning;
- model training;
- model comparison;
- evaluation metrics;
- prediction systems;
- AI application deployment.

The final result is a functional ASL gesture recognition system based on deep learning.

---

## 24. Defense Summary

This project is not only a simple CNN classification notebook.

It includes a full deep learning workflow:

- dataset preparation;
- image preprocessing;
- data augmentation;
- Custom CNN training;
- transfer learning with MobileNetV2;
- model comparison;
- advanced evaluation;
- confusion matrix;
- error analysis;
- Streamlit deployment.

Because of these components, the project is suitable for an A-level final deep learning project.
