import sqlite3

connection = sqlite3.connect('agenda.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE contatos (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
email TEXT NOT NULL,
telefone TEXT NOT NULL
);
""")
print("Tabela criada com sucesso!")
cursor.close()
connection.close()