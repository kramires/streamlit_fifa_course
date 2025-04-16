import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="FIFA 2023 OFFICIAL DATASET",
    page_icon="🏃🏽‍♂️⚽️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Carregar os dados 
df_data = st.session_state["data"]
#df_data

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Club", clubes)

st.markdown("# FIFA 2023 OFFICIAL DATASET!! 🏃🏽‍➡️⚽️")
st.sidebar.markdown("Desenvolvido por **Klayton Ramires**")

df_filtrados = df_data[df_data["Club"] == club].set_index("Name")

st.image(df_filtrados.iloc[0]["Club Logo"])
st.markdown(f"## **Clube:** {club}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtrados[columns], 
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", 
                        format="%d",
                        help="Overall rating of the player",
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                     "Weekly Wage(£)", 
                     format="£%f",
                     min_value=0,
                     max_value=df_filtrados["Wage(£)"].max(),
                     help="Monthly wage of the player",
                 ),
                 "Value(£)": st.column_config.NumberColumn(
                     "Value(£)", 
                     format="%f",
                     help="Market value of the player",
                 ),
                 "Contract Valid Until": st.column_config.DateColumn(
                     "Contract Valid Until", 
                     help="Contract expiration date",
                 ),
                 "Photo": st.column_config.ImageColumn(
                     "Photo", 
                     help="Player photo",
                 ),
                 "Flag": st.column_config.ImageColumn('Country',
                     help="Country flag",
                 ),
             })