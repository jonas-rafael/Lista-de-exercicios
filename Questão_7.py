print(20*"*")
print("   Questão 7")
print(20*"*")

quant=float(input("Digite a quantidade em kg de peixes capturados: "))


if quant>50:
    multa= quant-50
    multa=multa*4
    print(f"A multa será de {multa}")
else:
    print("Não a multa gerada")


