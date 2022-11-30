import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

pipeline=pickle.load(open('model_sentiment_naive.sav','rb'))
loaded_vec=TfidfVectorizer(decode_error="replace",vocabulary=set(pickle.load(open('selected_feature_tf-idf.sav','rb'))))

st.title('Prediksi SMS Penipuan')

clean_teks=st.text_input("Masukan Teks SMS")
fraud_test=''

if st.button('Prediksi SMS'):
  fraud_predict=pipeline.predict(loaded_vec.fit_transform([clean_teks]))
  if fraud_predict==0:
    fraud_test='SMS Normal'
    st.success(fraud_test)
  elif fraud_predict==1:
    fraud_test='SMS Fraud'
    st.warning(fraud_test)
  else:
    fraud_test='SMS Promo'
    st.warning(fraud_test)
