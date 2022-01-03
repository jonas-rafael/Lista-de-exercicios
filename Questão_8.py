print(20*"*")
print("   Questão 8")
print(20*"*")

vhora=float(input("quanto você ganha por hora: "))
qhora=float(input("quantas horas trabalhadas no mês: "))


salario=vhora*qhora

inss= (8/100)* salario
sindicato=(5/100)*salario
imposto=(11/100)*salario
liquido=salario-inss-sindicato-imposto
print(f"Salário bruto: {salario}")
print(f"Quanto pagou ao INSS:{inss}")
print(f"Quanto pagou ao sindicato:{sindicato}")
print(f"Valor do imposto:{imposto}")
print(f"Valor líquido do salário:{liquido}")
