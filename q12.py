
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

url = "https://api.github.com/repos/mwaskom/seaborn-data/contents/"

df = pd.read_json(url)

df_columns= df.columns.tolist()

st.title("Manipulation de données et création de graphiques")

valeur = st.selectbox(f"Quel dataset veux tu utiliser :", df['name'].loc[1:])

for x in df['name'].loc[1:]:
    if x == valeur:
        lign_url = df[df['name'] == valeur]
        # print(x, df['name'].loc[1:], lign_url, lign_url.iloc[0,-3])
        col_url = lign_url.iloc[0,-3]


df_col = pd.read_csv(col_url)
st.dataframe(df_col)


col_x = st.selectbox("Choisissez la colonne X :", df_col.columns.tolist())
col_y = st.selectbox("Choisissez la colonne Y :", df_col.columns.tolist())

graph = st.selectbox("Quel graphique veux tu utiliser ? :", ['bar_chart', 'scatter_chart','line_chart'])

st.text("_\n voici ton graphique : \n_")
if graph == 'bar_chart':
    st.bar_chart(df_col, x=col_x, y=col_y)
elif graph == 'scatter_chart':
    st.scatter_chart(df_col, x=col_x, y=col_y)
elif graph == 'line_chart':
    st.line_chart(df_col, x=col_x, y=col_y)

matrice = st.checkbox(label = "Afficher la matrice de correlation", value = False)

if matrice == True:
    df_corr = df_col.select_dtypes("number").corr()

    fig, ax = plt.subplots()
    sns.heatmap(df_corr, ax=ax)
    st.write(fig)