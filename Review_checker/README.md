# 🧠 Review Checker — Custom Bag-of-Words & TF-IDF Model

This is my introductory AI/NLP project where I built a custom **Bag-of-Words (BoW)** and **TF-IDF** engine to explore how text classification and sentiment analysis works under the hood.

Rather than using ready-made libraries, I wanted to manually implement the pipeline to better understand:
- Tokenization
- Frequency counts
- TF-IDF weighting
- Cosine similarity
- Basic sentiment scoring logic

## 🔍 Purpose

This project serves as a self-education tool and a personal AI sandbox. I wanted to lay down some foundation on which i could work to further develope my skills in AI. I wanted to create something functional and expandable while mastering the fundamentals of:

- Language representation using vectors
- NLP feature engineering
- Similarity metrics
- Naive sentiment logic

## 🛠️ What’s Inside?

- A manually built BoW implementation
- Custom TF-IDF score calculation
- Cosine similarity to compare sentences
- Word frequency mapping
- Simple sentiment classification based on word dictionaries
- Beginner-friendly and well-commented code

## 🤖 Use Case Ideas

- Review checker for positive/negative tone
- Query-matching chatbot intro
- Sentence similarity ranking
- Future plug-in for larger ML/NLP models

## 🧰 Tech Stack

- Python 3.x
- numpy
- pandas
- sklearn (used for comparison later)

## 🚧 Next Steps

- Add a small review classification dataset
- Implement evaluation metrics (precision, recall)
- Upgrade to scikit-learn’s `TfidfVectorizer` for comparison
- Optional: deploy a live checker with Streamlit

---