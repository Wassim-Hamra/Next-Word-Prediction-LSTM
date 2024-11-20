# **Next Word Prediction Using LSTM Architecture**

## This project aims to develop a deep learning model for predicting the next word in a given sequence of words. The model is built using Long Short-Term Memory (LSTM) networks, which are well-suited for sequence prediction tasks and it is trained on shakespeare's hamlet dataset.

## ***Steps:***

### ***1- Data Collection:*** I used the text of Shakespeare's \"Hamlet\" as my dataset. This complex text provides a good challenge for the LSTM model given its length.

### ***2- Data Preprocessing:*** The text data is tokenized, converted into sequences, and padded to ensure uniform input lengths. The sequences are then split into training and testing sets.

### ***3- Model Building:*** The LSTM model is constructed with an embedding layer, two LSTM layers, and a dense output layer with a softmax activation function to predict the probability of the next word.

  ### ***4- Model Training:*** The model is trained using the prepared sequences, with dropout implemented to prevent overfitting.
  
  ### ***5- Model Evaluation:*** The model is then evaluated using a set of example sentences to test its ability to predict the next word accurately.
  
  ### ***6- Deployment:*** Deployed using Streamlit to allow real-time predictions given an input.
  *  ***Web App link: [next-word-wassim-hamra.streamlit.app](https://next-word-prediction-wassim-hamraapp.streamlit.app/)***
  * **⚠️ Wake the Streamlit Application if it's sleeping**