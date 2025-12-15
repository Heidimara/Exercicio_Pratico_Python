import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
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
                    
