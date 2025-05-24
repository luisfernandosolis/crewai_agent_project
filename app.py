import streamlit as st

# Set page title
st.title('Este es mi segundo app con streamil')
st.markdown('<style>h1 {color: blue;}</style>', unsafe_allow_html=True)

# Sidebar with red background
st.sidebar.markdown('<style>h1 {color: red;}</style>', unsafe_allow_html=True)

# Text input for user's name
user_name = st.text_input('Escribe tu nombre')

# Button to submit name
if st.button('Enviar', key='submit_button'):
    st.write(f'Bienvenido, {user_name}!')