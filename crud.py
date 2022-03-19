from cProfile import label
import streamlit as st

st.title("Incluir cliente")

with st.form(key='include_cliente'):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira sus idade", format="%d", step=1)
    input_occupation = st.selectbox(label="Selecione sua profissão", options=["Desenvolvedor", "Músico", "Designer", "Professor"])
    input_button_submit = st.form_submit_button("Enviar")

if input_button_submit:
    st.write(f"Nome: {input_name}")
    st.write(f"Idade: {input_age}")
    st.write(f"Profissão: {input_occupation}")