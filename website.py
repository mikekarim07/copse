
import streamlit as st
from PIL import Image
import base64

# Configuración de la página
st.set_page_config(page_title="COPSE", page_icon="📄", layout="wide")

# Estilos personalizados
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        .sidebar .sidebar-content {
            background-color: #1f3b57;
            color: white;
        }
        .sidebar .sidebar-content a {
            color: white;
        }
        .sidebar .sidebar-content a:hover {
            color: #ffcc00;
        }
        h1, h2, h3 {
            color: #1f3b57;
        }
    </style>
""", unsafe_allow_html=True)

# Imagen decorativa de encabezado (usando un color de fondo como placeholder)
st.image("https://via.placeholder.com/1200x200/1f3b57/ffffff?text=COPSE+Plataforma+de+Cumplimiento", use_column_width=True)

# Barra lateral de navegación
seccion = st.sidebar.radio("Navegación", ["Inicio", "Proveedores", "Clientes", "Seguridad", "Contacto"])

# Contenido por sección
if seccion == "Inicio":
    st.title("Bienvenido a COPSE")
    st.write("""
    COPSE es una plataforma web diseñada para facilitar el cumplimiento de obligaciones fiscales y laborales
    para proveedores de servicios especializados, conforme a la reforma de subcontratación en México.

    Nuestra misión es simplificar procesos, garantizar la deducibilidad del gasto y el acreditamiento del IVA,
    brindando seguridad y transparencia tanto a proveedores como a clientes.
    """)

elif seccion == "Proveedores":
    st.header("Acceso para Proveedores")
    st.write("""
    Como proveedor, puedes cargar los siguientes documentos de manera segura:
    - Registro REPSE
    - Declaraciones de ISR, IMSS, Infonavit
    - CFDI emitidos
    - Pagos de IVA y retenciones

    La plataforma organiza automáticamente los documentos por periodo y cliente.
    """)

elif seccion == "Clientes":
    st.header("Acceso para Clientes")
    st.write("""
    Los clientes pueden:
    - Consultar y descargar documentos por proveedor y periodo
    - Validar cumplimiento ante el padrón público del REPSE
    - Recibir alertas de vencimientos o documentos faltantes

    Todo desde una interfaz clara y segura.
    """)

elif seccion == "Seguridad":
    st.header("Seguridad y Cumplimiento")
    st.write("""
    COPSE opera sobre infraestructura en la nube de Amazon Web Services (AWS), cumpliendo con estándares internacionales:
    - GDPR (Reglamento General de Protección de Datos)
    - ISO 27001
    - PCI-DSS

    Tus datos están protegidos con cifrado y acceso controlado.
    """)

elif seccion == "Contacto":
    st.header("Contáctanos")
    st.write("""
    ¿Tienes dudas o deseas una demostración?

    - **Nombre:** COPSE
    - **Correo:** contacto@copse.mx
    - **Teléfono:** +52 55 1234 5678
    - **Sitio web:** [www.copse.mx](https://copse.b12sites.com/index)
    """)
