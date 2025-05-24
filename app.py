import streamlit as st

# Set page title
st.title('Mi primera app con Streamlit')

# Create sidebar
st.sidebar.title('Datos de Usuario')
user_name = st.sidebar.text_input('Nombre')
submit_button = st.sidebar.button('Enviar')

# Display welcome message
if submit_button:
    st.write(f'Bienvenido, {user_name}!')