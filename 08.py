km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias de aluguel: "))

preco_total = dias_alugados * 60 + km_percorridos * 0.15

print("O preço a pagar é:", preco_total)
