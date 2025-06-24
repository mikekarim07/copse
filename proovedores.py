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
import streamlit as st

# Datos base
documentos = [
    "Contrato de prestación de servicios",
    "Registro REPSE",
    "Comprobantes de pago de cuotas obrero-patronales IMSS, INFONAVIT",
    "Declaraciones del SAT (IVA e ISR)",
    "Comprobantes de retenciones",
    "Acuse del ICSOE y SISUB",
    "CFDI’s de Nómina",
    "Opinión de Cumplimiento SAT / IMSS / INFONAVIT"
]

entregados = [
    "Contrato de prestación de servicios",
    "Registro REPSE",
    "CFDI’s de Nómina",
    "Opinión de Cumplimiento SAT / IMSS / INFONAVIT"
]

# Simulamos links (en producción, usarías una URL real)
fake_links = {
    doc: f"[📄 Ver archivo](#)" for doc in entregados
}

# Calculamos cumplimiento
cumplidos = len(entregados)
total = len(documentos)
porcentaje = round((cumplidos / total) * 100, 2)

# Título y métrica
st.title("Cumplimiento Documental del Proveedor")
st.metric("Porcentaje de cumplimiento", f"{porcentaje}%")

# Mostramos cada documento con estado y link (si aplica)
st.markdown("---")
for doc in documentos:
    entregado = doc in entregados
    icono = "✅" if entregado else "❌"
    link = fake_links.get(doc, "")
    
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.5em 1em; border-bottom: 1px solid #ddd;">
        <div style="font-weight: bold;">{icono} {doc}</div>
        <div>{link}</div>
    </div>
    """, unsafe_allow_html=True)
