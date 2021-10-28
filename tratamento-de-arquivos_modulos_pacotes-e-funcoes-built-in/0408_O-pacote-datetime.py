import datetime

agora = datetime.datetime.now()
      # Pacote   Metodo   Funcao

print(agora)
# O now nos mostra a data atual comecando do ano e indo até os milisegundos

tempo = datetime.time(7, 10, 20)
print(tempo)
# O time permite a criacao de um horario quando escrevemos horas, minutos e segundos nos parenteses

print("Hora: ", tempo.hour)
print("Minuto: ", tempo.minute)
print("Segundo: ", tempo.second)
print("Microsegundo: ", tempo.microsecond)
# Repartindo o horario criado em horas, minutos, segundos e microsegundos

print(datetime.time.min)
# Mostrando o minuto do horario

hoje = datetime.date.today()
print(hoje)
print("Data completa: ", hoje.ctime())
print("Ano: ", hoje.year)
print("Mês: ", hoje.month)
print("Dia: ", hoje.day)
# Repartindo o horario atual

data1 = datetime.date(2015, 4, 28)
                    # Ano, Mês, Dia
print("Primeira data: ", data1)
# Resultado: 2015-4-28

data2 = data1.replace(year=2016)
# Substituindo 2015 por 2016
# Resultado: 2016-4-28

print("Segunda data: ", data2)
# Resultado: 2016-4-28

print(data1 - data2)
# É mostrada a diferenca em dias entre as duas datas