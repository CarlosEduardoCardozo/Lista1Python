cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite quantos anos você fumou: "))

total_cigarros = cigarros_por_dia * anos_fumando * 365
tempo_perdido_minutos = total_cigarros * 10
tempo_perdido_dias = tempo_perdido_minutos / (24 * 60)

print("Você perderá aproximadamente", tempo_perdido_dias, "dias de vida.")
