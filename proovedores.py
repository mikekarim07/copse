import streamlit as st

st.set_page_config(
    page_title="COPSE - Clientes",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:miguel.karim@karimortega.com'
    }
)

st.image("Logo KalaTax.png", width=120)
st.title("Modulo de Proovedores")

st.write("Bienvenido Carlos")

import streamlit as st
import plotly.graph_objects as go


# Crear gráfico de tipo Gauge
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=30,
    title={'text': "Porcentaje de Cumplimiento"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "green"},
        'steps': [
            {'range': [0, 50], 'color': "lightgray"},
            {'range': [50, 100], 'color': "gray"}
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 80
        }
    }
))

# Mostrar en Streamlit
st.plotly_chart(fig)



