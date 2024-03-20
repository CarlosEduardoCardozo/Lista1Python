salario = float(input("Digite o valor do salário: "))
aumento_percentual = float(input("Digite a porcentagem do aumento: "))

aumento = salario * (aumento_percentual / 100)
novo_salario = salario + aumento

print("O aumento foi de:", aumento)
print("O novo salário é:", novo_salario)
