import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import time
from streamlit_option_menu import option_menu

# Configuracao inicial da pagina
st.header("Introduzindo os Elementos de Streamlit")
menu = option_menu (menu_title="Menu",
                    options=["Início", "Gráficos Estatísticos", "Gráficos Dinâmicos", "Widgets", "Formulario"],
                    icons =["house", "bar-chart", "bar-chart-line", "toggles", "bar-chart"],
                    menu_icon="cast",
                    default_index=0,
                    orientation="horizontal"
                    )
with st.sidebar:
  st.success("**UPLOAD DE DADOS**")
  dados = st.file_uploader(
    "Carregue os dados",
    type=["xlsx", "xls"]
  )     
  if dados: 
    def carregar_dados(dados):
        try:
           df=pd.read_excel(dados)
           return df
        except FileNotFoundError:
            return pd.DataFrame()

    df = carregar_dados(dados)
    st.table(df)

  else:
    st.info("Carregue um ficheiro Excel para começar")
    
# INICIO
if menu == "Início":
    with st.expander("**Sobre o Instituto Nacional de Estatística**"):
        st.write("Acesse o site www.ine.cv")
        st.image("INE.png")  # Certifique-se de que a imagem está na mesma pasta

# Widgets
if menu == "Widgets":
    bt = st.button("Dê um clique!")

    if bt:
        st.info("Clicaste num botão acima!")

    sd = st.slider(
        "Novo ponto do slider!",
        min_value=25,
        max_value=35,
        value=30,
        step=1
    )

    texto = f"Eu tenho {sd} anos!"
    st.success(texto)

     
