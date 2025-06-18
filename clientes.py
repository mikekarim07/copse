# import streamlit as st
# from supabase import create_client, Client

# st.set_page_config(
#     page_title="COPSE - Clientes",
#     page_icon="📈",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'mailto:miguel.karim@karimortega.com'
#     }
# )




# st.title("Modulo de Clientes 1")

# # Conexión con Supabase
# url = st.secrets["supabase"]["url"]
# key = st.secrets["supabase"]["key"]
# supabase: Client = create_client(url, key)

# st.set_page_config(page_title="Portal Clientes - Copse", layout="centered")

# # Estado de sesión
# if "user" not in st.session_state:
#     st.session_state.user = None

# # Formulario de login
# if st.session_state.user is None:
#     with st.form("login"):
#         st.title("Iniciar sesión")
#         email = st.text_input("Correo electrónico")
#         password = st.text_input("Contraseña", type="password")
#         submit = st.form_submit_button("Entrar")

#         if submit:
#             try:
#                 user = supabase.auth.sign_in_with_password({"email": email, "password": password})
#                 st.session_state.user = user
#                 st.success("Inicio de sesión exitoso.")
#                 st.rerun()
#             except Exception as e:
#                 st.error("Credenciales incorrectas o usuario no registrado.")
# else:
#     st.success(f"Sesión iniciada: {st.session_state.user.user.email}")
#     if st.button("Cerrar sesión"):
#         supabase.auth.sign_out()
#         st.session_state.user = None
#         st.rerun()

# # import streamlit as st
# # from supabase import create_client, Client

# # # Conexión a Supabase
# # url = st.secrets["supabase"]["url"]
# # key = st.secrets["supabase"]["key"]
# # supabase: Client = create_client(url, key)

# # Verifica que haya usuario logueado
# if "user" not in st.session_state or st.session_state.user is None:
#     st.warning("Inicia sesión para acceder al dashboard.")
#     st.stop()

# # Obtener ID del usuario logueado
# user_id = st.session_state.user.user.id

# # Obtener su perfil en la tabla usuarios
# perfil_resp = supabase.table("usuarios").select("*").eq("id", user_id).single().execute()
# perfil = perfil_resp.data

# # Validar rol
# if not perfil["es_admin"] or perfil["tipo_usuario"] != "cliente":
#     st.error("Acceso restringido a usuarios administradores de clientes.")
#     st.stop()

# st.title("Dashboard del Cliente Administrador")

# # Obtener los permisos del usuario para determinar acceso a entidades
# permisos_resp = supabase.table("permisos_usuario").select("entidad_legal_id").eq("usuario_id", user_id).execute()
# entidades_ids = [p["entidad_legal_id"] for p in permisos_resp.data]

# # Obtener las entidades legales visibles
# entidades_resp = supabase.table("entidades_legales").select("id, nombre, rfc, activo").in_("id", entidades_ids).execute()
# entidades = entidades_resp.data

# st.subheader("Entidades Legales Asignadas")
# if not entidades:
#     st.info("No tienes entidades legales asignadas.")
# else:
#     for entidad in entidades:
#         st.markdown(f"**{entidad['nombre']}** - RFC: {entidad['rfc']} {'✅' if entidad['activo'] else '❌'}")

# # Obtener proveedores relacionados a esas entidades
# proveedores_resp = supabase.rpc("get_proveedores_por_entidades", {"entidades_ids": entidades_ids}).execute()
# proveedores = proveedores_resp.data if proveedores_resp.data else []

# st.subheader("Proveedores Relacionados")
# if not proveedores:
#     st.info("No hay proveedores registrados para tus entidades.")
# else:
#     for p in proveedores:
#         st.markdown(f"- **{p['nombre']}** (RFC: {p['rfc']})")


import streamlit as st
from supabase import create_client, Client

# --- Conexión a Supabase ---
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase: Client = create_client(url, key)

# st.set_page_config(page_title="Copse Clientes", layout="centered")
st.set_page_config(
    page_title="COPSE - Clientes",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:miguel.karim@karimortega.com'
    }
)


# --- Estado de sesión ---
if "user" not in st.session_state:
    st.session_state.user = None

def login():
    st.title("Iniciar sesión - Copse Clientes")
    with st.form("login_form"):
        email = st.text_input("Correo electrónico")
        password = st.text_input("Contraseña", type="password")
        submit = st.form_submit_button("Entrar")

        if submit:
            try:
                response = supabase.auth.sign_in_with_password({"email": email, "password": password})
                if response.user is not None:
                    st.session_state.user = response
                    st.success(f"Bienvenido {email}")
                    st.experimental_rerun()
                else:
                    st.error("No se pudo iniciar sesión.")
            except Exception:
                st.error("Credenciales incorrectas o usuario no registrado.")

def logout():
    supabase.auth.sign_out()
    st.session_state.user = None
    st.experimental_rerun()

def dashboard():
    user_id = st.session_state.user.user.id

    # Obtener perfil del usuario
    perfil_resp = supabase.table("usuarios").select("*").eq("id", user_id).single().execute()
    perfil = perfil_resp.data

    if perfil is None:
        st.error("No se encontró el perfil del usuario.")
        return

    if not perfil["es_admin"] or perfil["tipo_usuario"] != "cliente":
        st.error("Acceso restringido a usuarios administradores de clientes.")
        return

    st.title("Dashboard Cliente Administrador")
    st.markdown(f"**Usuario:** {perfil['nombre_completo']} - {perfil['email']}")

    if st.button("Cerrar sesión"):
        logout()

    # Obtener permisos del usuario
    permisos_resp = supabase.table("permisos_usuario").select("entidad_legal_id").eq("usuario_id", user_id).execute()
    entidades_ids = [p["entidad_legal_id"] for p in permisos_resp.data]

    # Obtener entidades legales
    entidades_resp = supabase.table("entidades_legales").select("id, nombre, rfc, activo").in_("id", entidades_ids).execute()
    entidades = entidades_resp.data

    st.subheader("Entidades Legales Asignadas")
    if not entidades:
        st.info("No tienes entidades legales asignadas.")
    else:
        for entidad in entidades:
            st.markdown(f"- **{entidad['nombre']}** (RFC: {entidad['rfc']}) {'✅' if entidad['activo'] else '❌'}")

    # Obtener proveedores relacionados (aquí simplificado)
    proveedores_resp = supabase.table("proveedores").select("id, nombre, rfc").execute()
    proveedores = proveedores_resp.data

    st.subheader("Proveedores")
    if not proveedores:
        st.info("No hay proveedores registrados.")
    else:
        for prov in proveedores:
            st.markdown(f"- **{prov['nombre']}** (RFC: {prov['rfc']})")

# --- Lógica principal ---

if st.session_state.user is None:
    login()
else:
    dashboard()


