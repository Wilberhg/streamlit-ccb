import services.database as db


def incluir(cliente):
    db.cursor.execute(
        "INSERT INTO TB_Cliente (cliNome, cliIdade, cliProfissao) VALUES (?,?,?)",
        (cliente.nome, cliente.idade, cliente.profissao)
        )
    db.cnxn.commit()