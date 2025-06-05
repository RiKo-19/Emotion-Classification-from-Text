# Emotion Classification from Text 🧠

This project is a web-based application that predicts the emotion expressed in a given piece of text. It uses a machine learning model trained on labeled emotional text data and is deployed using Streamlit for a simple and interactive user interface.

---

## 📊 Dataset Used

The dataset used for training includes sentences labeled with one of the following six emotions:

- Joy
- Sadness
- Anger
- Fear
- Love
- Surprise

This dataset enables the model to learn how different emotions are expressed through language.

---

## 🧠 Approach Summary

1. **Text Preprocessing**: The input text is converted into numerical form using `TfidfVectorizer`, which captures important word-level features.

2. **Model Training**: A supervised classification algorithm (like Logistic Regression) is trained on the vectorized text and corresponding emotion labels.

3. **Model Deployment**:
   - The trained model and vectorizer are serialized using `pickle`.
   - These are loaded in a `Streamlit` app where users can enter their text and receive a predicted emotion in real-time.

---

## 📦 Dependencies

Install the required libraries using:

```bash
pip install streamlit scikit-learn
