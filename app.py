import streamlit as st
import pandas as pd
 
st.title("📊 Analyse rapide de ventes")
 
data = {
    "Produit": ["A", "B", "C"],
    "Ventes": [120, 90, 150]
}
 
df = pd.DataFrame(data)
 
st.write(df)
 
st.bar_chart(df.set_index("Produit"))
