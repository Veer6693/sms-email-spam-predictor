import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import  PorterStemmer

### Text Transformation

ps = PorterStemmer()

def transfrom_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    v = []
    for i in text:
        if i.isalnum():
            v.append(i)
    x = []
    for i in v:
        if i not in stopwords.words('english') and i not in string.punctuation:
            x.append(i)
    z = []
    for i in x:
        z.append(ps.stem(i))

    return " ".join(z)

### loading models

tfidf = pickle.load(open('vectiruzer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


### Build application

st.title("SMS/EMAIL SPAM PREDICTOR")

input_txt = st.text_area("Enter thr message")

if st.button("Predict"):
    transform_txt = transfrom_text(input_txt)
    vector_input = tfidf.transform([transform_txt])
    result = model.predict(vector_input)[0]


    if result == 1:
        st.header("Spam")
    else :
        st.header("Not Spam")
