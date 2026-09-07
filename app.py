import streamlit as st
 
st.title("🚀 Mon premier outil en ligne")
 
st.write("Entre ton prénom :")
 
prenom = st.text_input("Prénom")
 
if st.button("Valider"):
    if prenom:
        st.success(f"Bonjour {prenom} 👋")
    else:
        st.warning("Entre d'abord ton prénom.")
