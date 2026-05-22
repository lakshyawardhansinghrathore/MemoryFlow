import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# -----------------------------
# Load Model and Tokenizer
# -----------------------------
model = load_model("lstm_model (1).h5", compile=False)

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("max_len.pkl", "rb") as f:
    max_len = pickle.load(f)

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="MemoryFlow",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }

    .title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        color: #38bdf8;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #cbd5e1;
        margin-bottom: 30px;
    }

    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }

    .stButton button {
        width: 100%;
        background-color: #38bdf8;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        height: 50px;
        font-size: 18px;
    }

    .prediction-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        font-size: 20px;
        color: #f8fafc;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown('<div class="title">🧠 MemoryFlow</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Next Word Prediction using LSTM</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Prediction Function
# -----------------------------
def predict_next_word(text):

    token_list = tokenizer.texts_to_sequences([text])[0]
    token_list = pad_sequences(
        [token_list],
        maxlen=max_len - 1,
        padding='pre'
    )

    predicted = model.predict(token_list, verbose=0)

    predicted_word_index = np.argmax(predicted)

    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word

    return ""


# -----------------------------
# Sentence Generation Function
# -----------------------------
def generate_sentence(seed_text, next_words=10):

    for _ in range(next_words):

        next_word = predict_next_word(seed_text)

        if next_word == "":
            break

        seed_text += " " + next_word

    return seed_text


# -----------------------------
# User Input
# -----------------------------
input_text = st.text_input(
    "Enter a starting sentence:",
    placeholder="Example: deep learning is"
)

num_words = st.slider(
    "Number of words to generate",
    1,
    20,
    5
)

# -----------------------------
# Generate Button
# -----------------------------
if st.button("Generate Sentence"):

    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:

        generated_text = generate_sentence(input_text, num_words)

        st.markdown(
            f"""
            <div class="prediction-box">
            <b>Generated Sentence:</b><br><br>
            {generated_text}
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<br><br>
<center>
Made with ❤️ using LSTM & Streamlit
</center>
""", unsafe_allow_html=True)