import pandas as pd
import services.database as db


def incluir(cliente):
    db.cursor.execute(
        "INSERT INTO TB_Cliente (cliNome, cliIdade, cliProfissao) VALUES (?,?,?)",
        (cliente.nome, cliente.idade, cliente.profissao)
        )
    db.cnxn.commit()

def exibir():
    df = pd.read_sql("SELECT * FROM TB_Cliente", db.cnxn)
    return df