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

The project was extended from a trained CNN model into a full AI prototype with:

- a final Google Colab notebook;
- model training and evaluation;
- advanced metrics;
- visual result analysis;
- a Streamlit web application;
- clean GitHub project structure.

The final system can classify ASL gesture images into 29 classes and display predictions through an interactive web interface.

---

## Key Week 4 Deliverables

| Deliverable | Status |
|---|---|
| Final Google Colab notebook | Completed |
| CNN model training | Completed |
| Model evaluation metrics | Completed |
| Accuracy/loss visualizations | Completed |
| Confusion matrix | Completed |
| Classification report | Completed |
| Streamlit application | Completed |
| GitHub project organization | Completed |

---

## 1. Final Notebook Completion

The final notebook was created in Google Colab.

Notebook file:

```text
notebooks/Final_Project_ASL_Recognition.ipynb
```

The notebook includes the full project pipeline:

- project overview;
- dataset information;
- Kaggle dataset download;
- image preprocessing;
- data augmentation;
- CNN architecture;
- model training;
- model evaluation;
- prediction testing;
- visualization;
- Streamlit explanation;
- final conclusion.

Each code block contains comments using `#`, making the notebook easier to understand and explain during project defense.

---

## 2. Dataset Information

The project uses the ASL Alphabet Dataset from Kaggle.

Dataset link:

```text
https://www.kaggle.com/datasets/grassknoted/asl-alphabet
```

The dataset contains images representing:

- letters A–Z;
- `del`;
- `nothing`;
- `space`.

Total number of classes:

```text
29 classes
```

This dataset was used for a multi-class image classification task.

---

## 3. Image Preprocessing

Several preprocessing techniques were applied before training:

- image resizing to 64×64;
- normalization of pixel values;
- RGB image conversion;
- train-validation split;
- batch generation.

Image preprocessing helped standardize the input data and improve model training stability.

---

## 4. Data Augmentation

Data augmentation was used to improve model generalization and reduce overfitting.

The following augmentation techniques were applied:

- rotation;
- zoom;
- width shifting;
- height shifting;
- brightness adjustment.

These techniques helped the CNN model learn more robust ASL gesture patterns under different visual conditions.

---

## 5. CNN Model Architecture

A Convolutional Neural Network was built for ASL image classification.

The architecture contains:

- Conv2D layers;
- MaxPooling2D layers;
- Flatten layer;
- Dense layer;
- Dropout layer;
- Softmax output layer.

The model was compiled using:

```python
optimizer="adam"
loss="categorical_crossentropy"
metrics=["accuracy"]
```

CNN was selected because it is effective for image classification and can automatically learn visual features such as hand shapes, finger positions, and gesture patterns.

---

## 6. Model Training

The CNN model was trained using augmented ASL hand gesture images.

Training process:

```python
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=5
)
```

During training, the model learned:

- finger positions;
- hand shapes;
- gesture structures;
- visual differences between ASL classes.

The trained model was saved as:

```text
models/asl_cnn_final_model.h5
```

---

## 7. Model Evaluation Metrics

The final model was evaluated using both general and class-level metrics.

| Metric | Meaning | Result |
|---|---|---|
| Training Accuracy | Accuracy on training images | 97%+ |
| Validation Accuracy | Accuracy on unseen validation images | 87%+ |
| Training Loss | Model error during training | Low |
| Validation Loss | Model error on validation data | Low |
| Precision | Correctness of predicted classes | High |
| Recall | Ability to find real class examples | High |
| F1-score | Balance between precision and recall | High |
| Confusion Matrix | Class-by-class error analysis | Generated |

The metric results show that the CNN model learned meaningful ASL gesture patterns and performed well on validation data.

### Metrics Code Used in Notebook

```python
val_loss, val_accuracy = model.evaluate(validation_generator)

print(f"Validation Accuracy: {val_accuracy:.4f}")
print(f"Validation Loss: {val_loss:.4f}")

print(classification_report(
    y_true,
    y_pred,
    target_names=class_names
))
```

---

## 8. Performance Interpretation

The validation accuracy shows that the model can generalize to unseen ASL images.

The use of data augmentation and dropout helped reduce overfitting.

The classification report provides:

- precision;
- recall;
- F1-score;
- support.

The confusion matrix helps identify:

- correctly classified gestures;
- visually similar classes;
- possible prediction weaknesses.

Overall, the model demonstrates strong performance for an ASL image classification task.

---

## 9. Accuracy and Loss Visualization

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

## 10. Confusion Matrix

A confusion matrix was created to analyze prediction behavior across all classes.

Generated file:

```text
results/confusion_matrix.png
```

The confusion matrix helped identify which ASL gestures were predicted correctly and which classes may be visually similar.

---

## 11. Real Prediction Testing

The trained CNN model was tested on a real ASL gesture image.

The prediction pipeline included:

- image loading;
- resizing;
- normalization;
- prediction;
- confidence calculation.

Example output:

```text
Predicted Class: A
Confidence: 100%
```

The model showed high confidence when the input image clearly matched one ASL gesture class.

---

## 12. Top Prediction Analysis

Top prediction probabilities were analyzed to better understand model confidence.

For a clear ASL gesture image, the model predicted the correct class with very high confidence, while other class probabilities were close to zero.

This indicates that the CNN learned strong visual features from the dataset.

---

## 13. Streamlit Web Application

A Streamlit web application was developed to make the project interactive.

Main application file:

```text
app.py
```

The application allows users to:

- upload ASL gesture images;
- run CNN predictions;
- view the predicted ASL letter;
- see prediction confidence.

The application was tested locally using:

```bash
streamlit run app.py
```

The web application successfully opened at:

```text
http://localhost:8501
```

This made the project more practical and closer to a real AI product.

---

## 14. Prediction Helper File

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

## 15. Final Project Structure

Final repository structure:

```text
deep-learning-final-project/
├── data/
├── models/
│   └── asl_cnn_final_model.h5
├── notebooks/
│   ├── Week_1_Exploratory_Data_Analysis.ipynb
│   ├── Week_2_Image_Preprocessing.ipynb
│   ├── Week_3_CNN_Model_Training.ipynb
│   └── Week_4_Final_Project_ASL_Recognition.ipynb
├── reports/
│   ├── week_01.md
│   ├── week_02.md
│   ├── week_03.md
│   └── week_04.md
├── results/
│   ├── accuracy_plot.png
│   ├── loss_plot.png
│   └── confusion_matrix.png
├── src/
│   └── predict.py
├── app.py
├── requirements.txt
├── README.md
├── project-proposal.md
└── .gitignore
```

---

## 16. Technologies Used

The project used the following technologies:

- Python
- Google Colab
- TensorFlow
- Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Pillow
- Streamlit
- GitHub
- VS Code

---

## 17. Challenges Faced

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

### Model File Loading

The `.h5` model file initially produced loading issues.

The model was verified successfully using:

```python
model.summary()
```

### GitHub File Organization

The repository structure required proper organization of:

- notebooks;
- reports;
- model files;
- result images;
- Streamlit application files.

---

## 18. Final Result

By the end of Week 4, the project became a complete deep learning application.

Final project components:

- final Google Colab notebook;
- trained CNN model;
- saved `.h5` model file;
- evaluation metrics;
- accuracy graph;
- loss graph;
- confusion matrix;
- classification report;
- prediction testing;
- Streamlit application;
- organized GitHub repository.

The project demonstrates a practical AI system for recognizing American Sign Language gestures.

---

## 19. Conclusion

This project demonstrated the complete deep learning workflow:

```text
Dataset → Preprocessing → CNN Training → Evaluation → Prediction → Streamlit App
```

The project improved practical understanding of:

- computer vision;
- image preprocessing;
- CNN architectures;
- model training;
- evaluation metrics;
- prediction systems;
- AI application deployment.

The final result is a functional ASL gesture recognition system based on deep learning.
