import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Configuracao inicial da pagina
st.set_page_config(page_title="Dashboard Empresarial", layout="wide")

# Menu lateral com Streamlit Option Menu
menu = option_menu("Menu", ["Inicio", "Visualizar Dados", "Previsao", "Sobre"],
                       icons=["house", "bar-chart", "graph-up", "info-circle"],
                       menu_icon="cast", default_index=0)
