import sqlite3

# Criando uma conexao com o banco de dados escola, se ele nao existir, será criado.
conexao = sqlite3.connect("escola.db")

# Criando um cursor para percorrer todos os registros de um conjunto de dados.
cursorr = conexao.cursor()

# Criando uma tabela usando linguagem sql.
criar = "create table cursos (id integer primary key, titulo varchar(100), categoria varchar(140))"

# Executando a instrucao sql no cursor.
cursorr.execute(criar)