import streamlit as st
from supabase import create_client, Client

st.title("Modulo de Clientes 1")

# Conexión con Supabase
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase: Client = create_client(url, key)

st.set_page_config(page_title="Portal Clientes - Copse", layout="centered")

# Estado de sesión
if "user" not in st.session_state:
    st.session_state.user = None

# Formulario de login
if st.session_state.user is None:
    with st.form("login"):
        st.title("Iniciar sesión")
        email = st.text_input("Correo electrónico")
        password = st.text_input("Contraseña", type="password")
        submit = st.form_submit_button("Entrar")

        if submit:
            try:
                user = supabase.auth.sign_in_with_password({"email": email, "password": password})
                st.session_state.user = user
                st.success("Inicio de sesión exitoso.")
                st.rerun()
            except Exception as e:
                st.error("Credenciales incorrectas o usuario no registrado.")
else:
    st.success(f"Sesión iniciada: {st.session_state.user.user.email}")
    if st.button("Cerrar sesión"):
        supabase.auth.sign_out()
        st.session_state.user = None
        st.rerun()
