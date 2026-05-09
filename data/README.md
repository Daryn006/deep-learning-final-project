# IMDB Sentiment Analysis Dataset Guide

## Overview

This directory contains the dataset used for the **IMDB Sentiment Analysis Project**. The dataset consists of movie reviews collected from IMDB and labeled according to their sentiment.

The main goal of this project is to train machine learning and deep learning models that can automatically classify movie reviews as **positive** or **negative**.

This dataset is commonly used in:

- Natural Language Processing (NLP)
- Sentiment Analysis
- Text Classification
- Deep Learning research

---

## Dataset Source

**Name:** IMDB Dataset of 50K Movie Reviews  
**Source:** Kaggle  
**Dataset Link:** https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews  
**Original Source:** Stanford Large Movie Review Dataset  
**Size:** 50,000 reviews  
**License:** Kaggle Dataset License  

---

## Dataset Description

The dataset contains **50,000 movie reviews** written by real users on IMDB.

Each review belongs to one of two sentiment categories:

| Sentiment | Meaning |
|---|---|
| positive | The reviewer liked the movie |
| negative | The reviewer disliked the movie |

The dataset is balanced:

- 25,000 positive reviews
- 25,000 negative reviews

This balance is important because it helps prevent model bias toward one class.

---

## Dataset Structure

The dataset contains two main columns:

| Column | Description |
|---|---|
| review | Text content of the movie review |
| sentiment | Sentiment label: positive or negative |

---

## Example Data

| Review | Sentiment |
|---|---|
| This movie was absolutely fantastic and emotional. | positive |
| The storyline was boring and too predictable. | negative |

---

## Directory Structure

```plaintext
imdb-sentiment-analysis/
│
├── data/
│   ├── README.md
│   └── IMDB Dataset.csv
│
├── notebooks/
│   ├── week1_eda.ipynb
│   ├── preprocessing.ipynb
│   └── lstm_model.ipynb
│
├── reports/
│   ├── weekly_report_1.docx
│   ├── weekly_report_2.docx
│   ├── weekly_report_3.docx
│   └── final_report.docx
│
├── models/
│   ├── logistic_regression.pkl
│   └── lstm_model.h5
│
├── results/
│   ├── accuracy_plot.png
│   ├── confusion_matrix.png
│   └── loss_curve.png
│
├── requirements.txt
├── README.md
└── main.py
```

---

## Download Instructions

### Option 1: Manual Download

1. Open the Kaggle dataset page:  
   https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

2. Click **Download**.

3. Extract the ZIP file.

4. Place the CSV file into the `data/` folder.

Expected file path:

```plaintext
data/IMDB Dataset.csv
```

---

### Option 2: Kaggle API

Install Kaggle package:

```bash
pip install kaggle
```

Download the dataset:

```bash
cd data
kaggle datasets download -d lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
unzip imdb-dataset-of-50k-movie-reviews.zip
```

---

## Data Loading Example

```python
import pandas as pd

# Load dataset
df = pd.read_csv("data/IMDB Dataset.csv")

# Show first rows
print(df.head())
```

---

## Basic Dataset Information

```python
print(df.shape)
print(df.columns)
print(df["sentiment"].value_counts())
```

Expected output:

```text
(50000, 2)

Index(['review', 'sentiment'], dtype='object')

positive    25000
negative    25000
Name: sentiment, dtype: int64
```

---

## Data Preprocessing

Before training machine learning models, the text data needs preprocessing because models cannot directly understand raw text.

The preprocessing steps may include:

- Converting text to lowercase
- Removing punctuation
- Removing HTML tags
- Removing stopwords
- Tokenization
- Padding sequences
- Converting words into numerical vectors

Example:

```python
import re

text = "This MOVIE was AMAZING!!!"

text = text.lower()
text = re.sub(r"[^a-zA-Z\s]", "", text)

print(text)
```

Output:

```text
this movie was amazing
```

---

## Planned Models

### 1. Baseline Model: TF-IDF + Logistic Regression

This model converts movie reviews into numerical vectors using TF-IDF and then classifies the sentiment using Logistic Regression.

Advantages:

- Fast training
- Simple implementation
- Easy to understand
- Good baseline performance

---

### 2. Deep Learning Model: LSTM

LSTM stands for Long Short-Term Memory. It is a type of Recurrent Neural Network designed for sequential data such as text.

Advantages:

- Understands word order
- Learns context
- Works well with text data
- Suitable for sentiment analysis

---

## LSTM Workflow

```plaintext
Movie Review
      ↓
Tokenization
      ↓
Word Embeddings
      ↓
LSTM Layer
      ↓
Dense Layer
      ↓
Prediction: positive or negative
```

---

## Evaluation Metrics

The following metrics will be used to evaluate the models:

| Metric | Description |
|---|---|
| Accuracy | Measures overall correct predictions |
| Precision | Measures how many predicted positive reviews are actually positive |
| Recall | Measures how many actual positive reviews were correctly detected |
| F1-score | Balance between precision and recall |

---

## Research Questions

This project aims to answer the following questions:

1. How accurately can machine learning models classify movie review sentiments?
2. Does LSTM perform better than Logistic Regression?
3. How does preprocessing affect model performance?
4. Which words are most common in positive and negative reviews?
5. What are the main limitations of sentiment analysis models?

---

## Possible Challenges

Some challenges that may appear during the project:

- Large vocabulary size
- Long training time
- Overfitting
- Text preprocessing complexity
- GPU limitations

---

## Future Improvements

Possible future improvements include:

- Trying GRU model
- Using BERT or other transformer models
- Hyperparameter tuning
- Adding attention mechanism
- Deploying the model as a web application

---

## Ethical Considerations

Important notes:

- The reviews are written by real users.
- The dataset should be used only for educational and research purposes.
- The Kaggle dataset license should be respected.
- The model should not be used to manipulate or harm users.


---

## Next Steps

After downloading and preparing the dataset:

1. Perform Exploratory Data Analysis.
2. Clean and preprocess the text.
3. Train the baseline model.
4. Train the LSTM model.
5. Compare model performance.
6. Visualize results.
7. Write final conclusions.

---

## Conclusion

The IMDB Dataset of 50K Movie Reviews is a suitable dataset for learning Natural Language Processing and sentiment analysis. It contains real-world text data and balanced sentiment labels.

This project will help me improve my understanding of:

- Text preprocessing
- NLP workflows
- Machine learning classification
- Deep learning models
- Sentiment analysis
- Model evaluation

Overall, this dataset is a strong choice for building a practical sentiment classification project.
