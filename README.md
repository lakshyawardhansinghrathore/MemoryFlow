# 🧠 MemoryFlow

## Meaning of the Name

**MemoryFlow** combines two important ideas behind the project:

- **Memory** → Inspired by **LSTM (Long Short-Term Memory)** networks, which remember previous words and context while predicting the next word.
- **Flow** → Represents the smooth flow of language and sentence generation.

Together, **MemoryFlow** means:

> *"A system that intelligently remembers context and generates the natural flow of words."*

---

# 📖 About the Project

MemoryFlow is a **Next Word Prediction System** built using **LSTM (Long Short-Term Memory)** neural networks and deployed with **Streamlit**.

The model predicts the next probable word based on user input and can generate complete sentences word-by-word using learned language patterns.

This project demonstrates the use of:
- Deep Learning
- Natural Language Processing (NLP)
- Sequence Modeling
- LSTM Networks
- Streamlit UI Deployment

---

# 🚀 Features

- Predicts the next word using LSTM
- Generates complete sentences
- Interactive Streamlit UI
- Uses trained tokenizer and sequence padding
- Clean and responsive interface
- Real-time text generation

---

# 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pickle

---

# 📂 Project Structure

```bash
MemoryFlow/
│
├── app.py                 # Streamlit application
├── lstm_model (1).h5      # Trained LSTM model
├── tokenizer.pkl          # Saved tokenizer
├── max_len.pkl            # Maximum sequence length
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/lakshyawardhansinghrathore/MemoryFlow.git
cd MemoryFlow
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install streamlit tensorflow numpy
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

If Streamlit command is not recognized:

```bash
python -m streamlit run app.py
```

---

# 🧪 How It Works

1. User enters a starting sentence.
2. The tokenizer converts text into sequences.
3. The sequence is padded to the required length.
4. The LSTM model predicts the next word.
5. The predicted word is appended to the sentence.
6. The process repeats until the desired sentence length is generated.

---

# 🧠 Model Architecture

The project uses:
- Embedding Layer
- LSTM Layer
- Dense Output Layer with Softmax Activation

LSTM helps retain contextual memory from previous words, making predictions more meaningful and sequentially accurate.

---

# 📸 UI Preview

The Streamlit interface allows users to:
- Enter custom text
- Select number of words to generate
- Generate intelligent sentence predictions instantly

---

# 📌 Future Improvements

- Add Transformer-based prediction models
- Improve dataset quality
- Add beam search text generation
- Deploy using Streamlit Cloud or Hugging Face
- Add speech-to-text input
- Add dark/light mode toggle

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository and submit pull requests for improvements.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed by Lakshyawardhan Singh Rathore

```
