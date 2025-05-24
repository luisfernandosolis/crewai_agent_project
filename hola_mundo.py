import streamlit as st

def main():
    st.title('Mi primera app con Streamlit')

    st.sidebar.header('Sidebar Sencillo')
    user_name = st.sidebar.text_input('Escribe tu nombre', '')
    if st.sidebar.button('Enviar'):
        st.write(f'Bienvenido {user_name}')

if __name__ == '__main__':
    main()