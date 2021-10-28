import sqlite3

# Criando uma conexao com o banco de dados escola, se ele nao existir, será criado.
conexao = sqlite3.connect("escola.db")

# Criando um cursor para percorrer todos os registros de um conjunto de dados.
cursorr = conexao.cursor()

# Criando uma tabela usando linguagem sql.
criar = "create table cursos (id integer primary key, titulo varchar(100), categoria varchar(140))"

# Executando a instrucao sql no cursor.
cursorr.execute(criar)

# Criando uma variavel que recebe uma instrucao sql para inserir dados na tabela criada.
inserir = "insert into cursos values (?, ?, ?)"

# Criando uma variavel com os dados que serao inseridos na tabela criada.
registrar = [(1, "Ana", "Beatriz"),
(2, "Justin", "Bieber"),
(3, "Paula", "Vitoria")]

# Para cada dado que está na variavel registrar, execute no cursor a instrucao sql que está na variavel inserir passando cada dado como parametro.
for c in registrar:
    cursorr.execute(inserir, c)

# Salvando o que foi feito.
conexao.commit()

# Variavel que recebe uma instrucao sql para selecionar tudo que estiver na tabela cursos.
selecionar = "select * from cursos"

# Executando a instrucao da variavel selecionar.
cursorr.execute(selecionar)

# Colocando todos os dados que foram selecionados na variavel dados.
dados = cursorr.fetchall()

# Mostrando o que está em dados.
for c in dados:
    print("ID: %d NOME: %s SOBRENOME: %s \n" % c)

# Variavel que contem mais dois dados.
registrar = [(4, "Ana", "Oliveira"),
(5, "Vitoria", "Calixto")]

# Coloque os dados na tabela da mesma forma que foi feito na linha 23.
for c in registrar:
    cursorr.execute(inserir, c)

# Salve o que foi feito.
conexao.commit()

# Executando uma instrucao sql sem usar variavel.
cursorr.execute("select * from cursos")

# Colocando todos os dados que foram selecionados na variavel registrarr.
registrarr = cursorr.fetchall()

# Mostre os dados que estao na variavel registrarr.
for c in registrarr:
    print("ID: %d NOME: %s SOBRENOME: %s \n" % c)

# Feche a conexao com o banco de dados.
conexao.close()