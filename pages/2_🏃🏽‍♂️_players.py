import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="FIFA 2023 OFFICIAL DATASET",
    page_icon="🏃🏽‍♂️‍➡️⚽️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Carregar os dados 
df_data = st.session_state["data"]
#df_data

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Club", clubes)

df_players = df_data[df_data["Club"] == club]
players = df_data[df_data["Club"] == club]["Name"].unique()
player = st.sidebar.selectbox("Player", players)

st.markdown("# FIFA 2023 OFFICIAL DATASET!! 🏃🏽‍➡️⚽️")
st.sidebar.markdown("Desenvolvido por **Klayton Ramires**")

player_stats = df_data[df_data["Name"] == player].iloc[0]
st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

coluna1, coluna2, coluna3, coluna4 = st.columns(4)
coluna1.markdown(f"**Idade:** {player_stats['Age']}")
coluna2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100} m")
coluna3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] *0.453:.2f} kg")
coluna4.markdown(f"**Nacionalidade:** {player_stats['Nationality']}")

st.divider()

st.subheader(f"Overall: {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))
         

coluna1, coluna2, coluna3, coluna4 = st.columns(4)
coluna1.metric(label="Valor de Mercado", value=f"£ {player_stats['Value(£)']}")
coluna2.metric(label="Remuneração mensal", value=f"£ {player_stats['Wage(£)']}")
coluna3.metric(label="Potencial", value=player_stats["Potential"])
coluna4.metric(label="Cláusula de recisão", value=player_stats["Release Clause(£)"])
