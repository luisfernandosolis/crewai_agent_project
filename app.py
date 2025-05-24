import streamlit as st

# Set page title
st.title('Este es mi segundo app con streamlit')
st.markdown("<style>h1{color: blue;}</style>", unsafe_allow_html=True)

# Sidebar with text input and button
user_name = st.sidebar.text_input('Escribe tu nombre')
if st.sidebar.button('Enviar nombre', key='submit_button'):
    pass  # Button action can be defined here

# Main body content
st.write(f'Bienvenido, {user_name}' if user_name else 'Bienvenido')