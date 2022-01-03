print(20*"*")
print("   Questão 10")
print(20*"*")

mb=float(input("Qual o tamanho do arquivo em MB para download: "))
Mbps=float(input("Qual a velocidade do link da internet: "))

tempo=mb/Mbps
print(f"O tempo estimado é de: {tempo}")