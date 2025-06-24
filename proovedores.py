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


# # Crear gráfico de tipo Gauge
# fig = go.Figure(go.Indicator(
#     mode="gauge+number",
#     value=30,
#     title={'text': "Porcentaje de Cumplimiento"},
#     gauge={
#         'axis': {'range': [0, 100]},
#         'bar': {'color': "green"},
#         'steps': [
#             {'range': [0, 50], 'color': "lightgray"},
#             {'range': [50, 100], 'color': "gray"}
#         ],
#         'threshold': {
#             'line': {'color': "red", 'width': 4},
#             'thickness': 0.75,
#             'value': 80
#         }
#     }
# ))

# # Mostrar en Streamlit
# st.plotly_chart(fig)

import streamlit as st
import pandas as pd

# Lista de documentos requeridos
documentos_requeridos = [
    "Contrato de prestación de servicios",
    "Registro REPSE",
    "Comprobantes de pago de cuotas obrero-patronales IMSS, INFONAVIT",
    "Declaraciones del SAT (IVA e ISR)",
    "Comprobantes de retenciones",
    "Acuse del ICSOE y SISUB",
    "CFDI’s de Nómina",
    "Opinión de Cumplimiento SAT / IMSS / INFONAVIT"
]

# Simulamos los documentos entregados por el proveedor (puedes cambiarlo por tu fuente real de datos)
documentos_entregados = [
    "Contrato de prestación de servicios",
    "Registro REPSE",
    "CFDI’s de Nómina",
    "Opinión de Cumplimiento SAT / IMSS / INFONAVIT"
]

# Creamos el DataFrame con estado de cumplimiento
df = pd.DataFrame({
    "Documento": documentos_requeridos,
    "Entregado": [doc in documentos_entregados for doc in documentos_requeridos]
})

# Calculamos porcentaje de cumplimiento
cumplidos = df["Entregado"].sum()
total = len(df)
porcentaje_cumplimiento = round((cumplidos / total) * 100, 2)

# Interfaz Streamlit
st.title("Cumplimiento Documental del Proveedor")
st.metric("Porcentaje de cumplimiento", f"{porcentaje_cumplimiento}%")
st.dataframe(df.replace({True: "✅", False: "❌"}), use_container_width=True)


