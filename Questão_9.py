print(20*"*")
print("   Questão 9")
print(20*"*")

square=float(input("Digite a area em metros quadrados a ser pintada: "))
tin=square/3

preço=80
quantidade=18

latas=tin/quantidade
preçofinal=latas*preço

print(f"A quantidade de latas é: {latas}")
print(f"O preço total a ser gasto é: {preçofinal}")