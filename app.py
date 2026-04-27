import streamlit as st
import random
import string

st.title("Şifre Oluşturucu")

uzunluk = st.slider("Uzunluk", 6, 32, 12)

if st.button("Üret"):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    st.code(sifre)
