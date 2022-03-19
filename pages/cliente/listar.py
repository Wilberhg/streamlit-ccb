import controllers.ClienteController as ClienteController
import streamlit as st

def listar():
    colms = st.columns((1,2,1,2))
    campos = ['Nº', 'Nome', 'Idade', 'Profissão']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for item in ClienteController.SelecionarTodos()