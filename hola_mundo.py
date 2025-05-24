import streamlit as st

# Set up the title
st.title('Mi primera app con Streamlit')

# Create a sidebar
st.sidebar.header('Ingrese su nombre')
user_name = st.sidebar.text_input('Nombre')
if st.sidebar.button('Enviar'):
    st.write(f'Bienvenido {user_name}!')

# Main body of the app
if st.button('Mostrar mensaje adicional'):
    st.write('¡Gracias por usar la app!')

comment = st.text_area('Escriba un comentario aquí')