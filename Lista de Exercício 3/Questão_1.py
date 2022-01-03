print(20*"*")
print("   Questão 01")
print(20*"*")
while True:
    nome=input("Digite o nome desejado, maior que 3 caracteres:")

    Idade=float(input("Insirá sua idade entre 0 e 150"))
    Salario=float(input("Insirá o salário maior que zero"))
    sexo=str(input("seu sexo, insirá apenas: “f” ou “m”").lower())
    Estado=input("Seu estado civil, insirá uma das opções:“s”, “c”, “v”, “d”:").lower()

    if len(nome) < 3:
        break
    elif Idade > 150 and Idade < 0:
        break
    elif Salario < 0:
        break
    elif sexo != "s" or sexo != "n":
        break
    elif Estado != "s" or "c" or "v" or "d":
        break
    else:
        print(f"O nome é {nome}")
        print(f" A idade é {Idade}")
        print(f"O salário é de {Salario}")
        print(f"O Sexo é {sexo}")
        print(f"O estado é {Estado}")