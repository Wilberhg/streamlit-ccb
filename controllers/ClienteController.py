import pandas as pd
import services.database as db
import models.Cliente as cliente


def incluir(cliente):
    db.cursor.execute(
        "INSERT INTO TB_Cliente (cliNome, cliIdade, cliProfissao) VALUES (?,?,?)",
        (cliente.nome, cliente.idade, cliente.profissao)
        )
    db.cnxn.commit()

def excluir(id):
    db.cursor.execute(
        "DELETE FROM TB_Cliente WHERE id = (?)",
        (id,)
        )
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM TB_Cliente")
    customer_list = []
    for row in db.cursor.fetchall():
        customer_list.append(cliente.Cliente(row[0], row[1], row[2], row[3]))

    return customer_list

def exibir():
    df = pd.read_sql("SELECT * FROM TB_Cliente", db.cnxn)
    return df