import streamlit as st
import controllers.ClienteController as ClienteController

def consultar():
    df = ClienteController.exibir()
    st.table(df)