import streamlit as st

st.title('Este es mi segundo app con streamlit')
st.sidebar.markdown("<h1 style='color: red;'>Sidebar</h1>", unsafe_allow_html=True)

name = st.text_input('Escribe tu nombre aquí')
submit_button = st.button('Enviar nombre', key='submit_button', help='Botón para enviar nombre')

if submit_button:
    st.write(f'Bienvenido, {name}!')