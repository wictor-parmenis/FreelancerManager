import sqlite3
import front2

dbase = sqlite3.connect('freelancer_manager.db')
c = dbase.cursor()


def create_table():
    try:
        c.execute(''' CREATE TABLE IF NOT EXISTS jobs (
                    ID INT PRIMARY KEY,
                    NAME TEXT NOT NULL,
                    REVENUES FLOAT NOT NULL,
                    SPENDING FLOAT NOT NULL,
                    PROFIT TEXT NOT NULL,
                    PRICE_HOUR TEXT NOT NULL,
                    DATE_CADASTER TEXT NOT NULL
                    )''')
        dbase.commit()
    except Exception as e:
        print(e)
    else:
        print('Tabela criada com sucesso.')


def write(ID, NAME, REVENUES, SPENDING, PROFIT, PRICE_HOUR, DATE_CADASTER):
    try:
        c.execute(''' INSERT INTO jobs (ID, NAME, REVENUES, SPENDING, PROFIT, PRICE_HOUR, DATE_CADASTER) VALUES
         (?, ?, ?, ?, ?, ?, ?)''', (ID, NAME, REVENUES, SPENDING, PROFIT, PRICE_HOUR, DATE_CADASTER))
        dbase.commit()
    except Exception as e:
        print(e)
    else:
        print('Trabalho registrado com sucesso.')


def delete(ID):
    try:
        c.execute('''DELETE from jobs WHERE ID =?''', (ID,))
        dbase.commit()
    except Exception as e:
        print('Falha em deletar registro.')
    else:
        print('Registro deletado com sucesso.')


def alter(NOME, ID):
    try:
        c.execute('''UPDATE jobs SET NAME=? WHERE ID=?''',(NOME, ID))
        dbase.commit()
    except Exception as e:
        print('Falha ao alterar registro.')
    else:
        print('Registro alterado com sucesso.')


def select(ID):
    try:
        row = c.execute('''SELECT * FROM jobs WHERE ID=?''', (ID,)).fetchall()
        print(row)
    except Exception as e:
        print('Falha ao selecionar registro.')


def show_all():
    try:
        c.execute('''  SELECT * FROM jobs''')
        rows = c.fetchall()
        for r in rows:
            print(r)
    except Exception as e:
        print('Falha ao exibir registros.')






