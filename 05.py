preco = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

desconto = preco * (percentual_desconto / 100)
preco_pagar = preco - desconto

print("O valor do desconto é:", desconto)
print("O preço a pagar é:", preco_pagar)
