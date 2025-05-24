import streamlit as st

# Set title
st.title('Este es mi segundo app con streamlit')
st.markdown('<style>h1{color: blue;}</style>', unsafe_allow_html=True)

# Create a sidebar with a red background
st.sidebar.markdown('<style>div{background-color: red;}</style>', unsafe_allow_html=True)

# Add text input for user's name
user_name = st.text_input('Escribe tu nombre aquí')

# Add button to submit the name
submit_btn = st.button('Enviar', key='submit_btn')

# Display welcome message with user's name
if submit_btn:
    st.write(f'Bienvenido, {user_name}!')