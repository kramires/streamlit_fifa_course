import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="FIFA 2023 OFFICIAL DATASET",
    page_icon="⚽️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Carregar os dados
if "data"not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    # Adicionando uma coluna com o ano atual
    #df_data["Current Year"] = datetime.today().year
    # # Adicionando uma coluna com o ano de nascimento
    # df_data["Year of Birth"] = pd.to_datetime(df_data["Date of Birth"]).dt.year
    # # Adicionando uma coluna com a idade
    # df_data["Age"] = df_data["Current Year"] - df_data["Year of Birth"]
    st.session_state["data"] = df_data

st.markdown("# FIFA 2023 OFFICIAL DATASET!! 🏃🏽‍➡️⚽️")
st.sidebar.markdown("Desenvolvido por **Klayton Ramires**")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
    
st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)


