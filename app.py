import streamlit as st
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer

# Emotion mapping
emotion_map = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}

# Load model and vectorizer
with open("emotion_class_model.sav", "rb") as f:
    model_data = pickle.load(f)

# If saved as (vectorizer, model)
vectorizer, model = model_data

# Streamlit UI
st.set_page_config(page_title="Emotion Classifier", layout="centered")
st.title("Emotion Classification from Text 🧠 ")
st.markdown("#### Enter a sentence and the model will predict the **emotion** of you!")

# Text input
text_input = st.text_area("Enter your text here:", height=200)

if st.button("Predict Emotion"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Vectorize the input
        X_input = vectorizer.transform([text_input])

        # Predict
        predicted_label = model.predict(X_input)[0]

        # Map to emotion name
        predicted_emotion = emotion_map.get(predicted_label, "Unknown")

        # Display result
        st.success(f"Predicted Emotion: **{predicted_emotion}**")
