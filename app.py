# Imports
import streamlit as st

# Main title
st.title('Mi primera app con Streamlit')

# Sidebar
user_name = st.sidebar.text_input('Escribe tu nombre')
if st.sidebar.button('Enviar', key='send_button', help='Enviar el nombre del usuario'):
    st.write(f'Bienvenido, {user_name}')