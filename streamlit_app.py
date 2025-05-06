import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the LSTM model
model = load_model('next_word_lstm.keras')

# Load Tokenizer
with open('tokenizer.pickle','rb') as handle:
    tokenizer = pickle.load(handle)

def predict_next_word(model, tokenizer, text, max_sequence_len):
  token_list = tokenizer.texts_to_sequences([text])[0]
  if len(token_list) >= max_sequence_len:
    token_list = token_list[-(max_sequence_len-1):]  # Ensure the sequence length matches max_sequence_len-1\n",
  token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
  predicted = model.predict(token_list, verbose=0)
  predicted_word_index = np.argmax(predicted, axis=1)
  for word, index in tokenizer.word_index.items():
    if index == predicted_word_index:
      return word
  return None

# Streamlit app
st.markdown(
    f"""
    <style>
    .box {{
        padding: 1.5em 0.5em 0em 1em;
        margin: 0em;
        background-color:rgba(79, 227, 94, 0.3);
        border-radius: 10px;
        border: 0.5px solid #d3d3d3;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.title('💻 Projet Tech.Multimedia : ')
st.title('----------------')
st.title('✨ Prédiction du mot suivant avec RNN')
input_text = st.text_input('Entrez votre séquence 💬','Hello there')
if st.button("Prédire le mot suivant"):
    next_word = predict_next_word(model,tokenizer,input_text,14)
    st.markdown(f'<div class="box"><h5>{input_text}</h5><h4 style="color:red; font-weight:bold">{next_word}</h4></div>', unsafe_allow_html=True)
