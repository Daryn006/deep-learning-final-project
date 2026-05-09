# IMDB Sentiment Analysis Project  
## Week 1 Report — Exploratory Data Analysis

---

# 🌍 Introduction

Artificial Intelligence and Natural Language Processing are becoming increasingly important in modern technology. Every day, people leave millions of reviews on websites such as IMDB, Amazon, YouTube, Reddit, and social media platforms. These reviews contain emotions, opinions, recommendations, criticism, and personal experiences.

However, computers cannot naturally understand human emotions from text. Because of this, sentiment analysis became one of the most important tasks in Natural Language Processing (NLP).

The purpose of this project is to build a machine learning and deep learning system capable of automatically classifying movie reviews as:

- positive
- negative

For this project, I selected the **IMDB Dataset of 50K Movie Reviews** from Kaggle.

Dataset link:  
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

---

# 🎯 Week 1 Objective

The main objective of Week 1 was to perform Exploratory Data Analysis (EDA) on the IMDB movie review dataset.

This week focused on:

- understanding the dataset structure;
- exploring review patterns;
- analyzing sentiment distribution;
- checking missing values;
- visualizing review lengths;
- identifying possible preprocessing challenges;
- preparing the dataset for future machine learning models.

---

# 📦 Dataset Description

The dataset contains:

- 50,000 movie reviews;
- sentiment labels;
- balanced classes;
- real user-written reviews from IMDB.

The dataset contains two main columns:

| Column | Description |
|---|---|
| review | Text of the movie review |
| sentiment | Sentiment label: positive or negative |

The dataset is balanced:

- 25,000 positive reviews
- 25,000 negative reviews

Balanced datasets are important because they help prevent model bias toward one class.

---

# 🛠️ Work Completed During Week 1

During this week, I completed several important tasks related to dataset exploration and understanding.

The completed tasks include:

- importing required libraries;
- loading the dataset;
- checking dataset shape;
- analyzing dataset columns;
- checking missing values;
- analyzing sentiment distribution;
- visualizing dataset statistics;
- displaying example reviews;
- creating review length analysis;
- identifying possible NLP challenges.

---

# 📖 Loading and Exploring the Dataset

The dataset was loaded using the pandas library.

After loading the dataset, I checked:

- the number of rows and columns;
- column names;
- data types;
- missing values.

The dataset shape was:

```text
(50000, 2)
```

This means the dataset contains 50,000 rows and 2 columns.

The dataset was clean and contained no missing values.

This is useful because missing data can negatively affect preprocessing and model training.

---

# 😊😡 Sentiment Distribution Analysis

One of the first tasks was analyzing sentiment distribution.

The results showed that the dataset is perfectly balanced:

| Sentiment | Count |
|---|---|
| positive | 25,000 |
| negative | 25,000 |

A visualization of sentiment distribution was also created using seaborn and matplotlib.

The graph confirmed that both classes contain the same number of reviews.

This is important because balanced datasets usually produce more stable and reliable machine learning models.

---

# 🌟 Positive Review Analysis

Several positive reviews were explored manually.

Positive reviews often contained words such as:

- amazing
- fantastic
- emotional
- excellent
- brilliant
- masterpiece

These reviews usually expressed:
- excitement,
- satisfaction,
- emotional attachment,
- strong recommendations.

This showed that emotional vocabulary plays an important role in sentiment analysis.

---

# 💀 Negative Review Analysis

Negative reviews were also explored manually.

Negative reviews often contained words such as:

- boring
- terrible
- disappointing
- worst
- waste
- bad

These reviews usually expressed:
- frustration,
- criticism,
- dissatisfaction,
- disappointment.

This demonstrated that positive and negative reviews use different emotional language patterns.

---

# 📐 Review Length Analysis

Another important part of Week 1 was analyzing review lengths.

A new column called `review_length` was created to calculate the number of characters in each review.

The analysis showed that:

- some reviews are short;
- some reviews are extremely long;
- most reviews are medium-length.

Histograms and visualizations were created to better understand the distribution of review lengths.

This is important because deep learning models often require fixed-length sequences.

In future preprocessing stages, techniques such as:
- padding,
- truncation,
- maximum sequence limits

may be required.

---

# 🧠 Challenges Identified During EDA

After analyzing the dataset, several possible challenges became visible.

## 1. Large Vocabulary Size

The dataset contains thousands of unique words.

This may:
- increase memory usage,
- increase preprocessing complexity,
- slow down training.

---

## 2. Informal Language

Movie reviews contain:
- slang,
- abbreviations,
- emotional expressions,
- internet language.

This makes Natural Language Processing more difficult.

---

## 3. Long Reviews

Some reviews are extremely long.

This may create problems for:
- tokenization,
- embeddings,
- sequence models.

---

## 4. Emotional Context

People express emotions differently.

For example:

- “This movie destroyed me emotionally.”
- “Absolutely mind-blowing.”
- “I regret wasting my time.”

The model must learn these emotional patterns automatically.

---

# 📊 Key Findings

The main findings from Week 1 are:

- the dataset is balanced;
- there are no missing values;
- reviews contain emotional vocabulary;
- review lengths vary significantly;
- preprocessing will be an important stage;
- the dataset is highly suitable for sentiment analysis tasks.

---

# 🚀 Plan for Week 2

In Week 2, I plan to focus on preprocessing and baseline machine learning models.

Planned tasks include:

- text cleaning;
- removing punctuation;
- removing HTML tags;
- lowercasing;
- tokenization;
- TF-IDF vectorization;
- Logistic Regression baseline model;
- model evaluation.

---

# 💭 Personal Reflection

Week 1 helped me understand how complex human language actually is.

At first, sentiment analysis seemed simple, but after exploring the dataset, I realized that reviews contain:
- emotions,
- different writing styles,
- slang,
- contextual meanings,
- long explanations.

I also learned that Exploratory Data Analysis is extremely important because understanding the data before modeling helps identify possible problems early.

---

# ✅ Conclusion

Week 1 focused on understanding and exploring the IMDB movie review dataset.

The dataset is:
- clean;
- balanced;
- realistic;
- suitable for NLP tasks;
- appropriate for machine learning and deep learning experiments.

The Exploratory Data Analysis stage created a strong foundation for the future stages of the project involving preprocessing, TF-IDF vectorization, and deep learning sentiment classification models.
