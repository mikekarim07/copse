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
st.title("Modulo de Clientes")

st.write("Carlos Lara")


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

# Documentos requeridos
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

# Documentos entregados y links reales (ejemplo: a google.com)
documentos_entregados = {
    "Contrato de prestación de servicios": "https://google.com/contrato.pdf",
    "Registro REPSE": "https://google.com/repse.pdf",
    "CFDI’s de Nómina": "https://google.com/nomina.pdf",
    "Opinión de Cumplimiento SAT / IMSS / INFONAVIT": "https://google.com/opinion.pdf"
}

# Cálculo del porcentaje
cumplidos = len(documentos_entregados)
total = len(documentos)
porcentaje = round((cumplidos / total) * 100, 2)

# Título y métrica
st.title("PSE Tijuana, S.A. de C.V.")
st.subheader("Periodo: Abril 2025")
st.write("Cumplimiento Documental del Proveedor")
st.metric("Porcentaje de cumplimiento", f"{porcentaje}%")

# Mostramos los documentos con su estado y link si aplica
st.markdown("---")
for doc in documentos:
    entregado = doc in documentos_entregados
    icono = "✅" if entregado else "❌"
    link = documentos_entregados.get(doc)
    texto_link = ""

    if link:
        nombre_archivo = doc.split()[0].replace("’", "").replace("é", "e").replace("ó", "o").capitalize() + ".pdf"
        texto_link = f'<a href="{link}" target="_blank">{nombre_archivo}</a>'

    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.5em 1em; border-bottom: 1px solid #ddd;">
        <div style="font-weight: bold;">{icono} {doc}</div>
        <div>{texto_link}</div>
    </div>
    """, unsafe_allow_html=True)
