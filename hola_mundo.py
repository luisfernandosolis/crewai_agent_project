import streamlit as st

# Title
st.title('Mi primera app con Streamlit')

# Sidebar
user_name = st.sidebar.text_input('Escribe tu nombre')
submit_button = st.sidebar.button('Enviar nombre')

# Main body
if submit_button:
    st.write(f"Bienvenido, {user_name}!")

    if st.button('¡Gracias por usar la app!'):
        st.write('¡Gracias por usar la app!')
    
    st.text_area('Escribe un comentario')