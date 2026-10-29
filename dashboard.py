
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

tabela = pd.read_excel(r"C:\Users\David Cardona\Desktop\codigos\PETR4_evolucao.xlsx")

# Separar os dados
lucro = tabela[tabela["conta"] == "lucro"]
receita = tabela[tabela["conta"] == "receita"]

# Criar as abas
tab1, tab2 = st.tabs(["Lucro", "Receita"])

with tab1:
    st.title("Lucro da PETR4")

    fig, ax = plt.subplots()
    sns.lineplot(data=lucro, x="trimestre", y="valor", ax=ax)

    plt.xticks(rotation=90)
    st.pyplot(fig)
    st.dataframe(lucro)

with tab2:
    st.title("Receita da PETR4")

    fig, ax = plt.subplots()
    sns.lineplot(data=receita, x="trimestre", y="valor", ax=ax)

    plt.xticks(rotation=90)
    st.pyplot(fig)
    st.dataframe(receita)
