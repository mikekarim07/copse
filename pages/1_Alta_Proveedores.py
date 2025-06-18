import streamlit as st
from supabase import create_client

url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase = create_client(url, key)

st.title("Alta de Proveedores")

if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Debes iniciar sesión primero.")
    st.stop()

with st.form("alta_proveedor"):
    nombre = st.text_input("Nombre del proveedor")
    rfc = st.text_input("RFC del proveedor")
    submit = st.form_submit_button("Registrar")

    if submit:
        if not nombre or not rfc:
            st.error("Todos los campos son obligatorios.")
        else:
            try:
                supabase.table("proveedores").insert({"nombre": nombre, "rfc": rfc}).execute()
                st.success(f"Proveedor '{nombre}' registrado correctamente.")
            except Exception as e:
                st.error(f"Error al registrar proveedor: {e}")
