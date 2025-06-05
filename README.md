# Emotion Classification from Text

This project is a web-based application that predicts the emotion expressed in a given text. It uses a machine learning model (SVM) trained on labeled emotional text data and is deployed using Streamlit for a simple and interactive user interface.

You can check the webpage through this link - https://emotion-classification-from-text.streamlit.app/

--- 

## 📊 Dataset Used

I take a dataset from Huggingface that is used for training of the model. And it includes sentences labeled with one of the following six emotions:

- Joy
- Sadness
- Anger
- Fear
- Love
- Surprise

This dataset enables the model to learn how different emotions are expressed through texts.

---

## 🧠 Approach Summary

1. **Text Preprocessing**: The input text is converted into numerical form using `TfidfVectorizer`, which captures important word-level features.

2. **Model Training**: I use SVM classifier to train the model using this vectorized text and corresponding emotion labels.

3. **Model Deployment**:
   - The trained model and vectorizer are serialized using `pickle`.
   - These are loaded in a `Streamlit` app and create a webpage where users can enter their text and receive a predicted emotion in real-time.

---

## 📦 Dependencies

Install the required libraries using:
- streamlit
- scikit-learn
- pandas
- numpy
- seaborn
- matplotlib

```bash
pip install streamlit scikit-learn pandas numpy matplotlib seaborn
```

---

## 🖥️ User Interface

