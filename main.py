import streamlit as st
import pages.cliente.incluir as page_incluir_cliente
import pages.cliente.consultar as page_consultar_clientes
import pages.cliente.listar as page_listar_clientes

st.sidebar.title("Menu")

page_cliente = st.sidebar.selectbox('Cliente', ['Incluir', 'Alterar', 'Consultar', 'Consultar_DF'])

if page_cliente == 'Incluir':

    page_incluir_cliente.incluir()

elif page_cliente == 'Consultar_DF':
    
    page_consultar_clientes.consultar()

elif page_cliente == 'Listar':
    
    page_listar_clientes.listar()