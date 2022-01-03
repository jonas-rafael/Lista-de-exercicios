print (20*"*")
print ("     Questão 3")
print (20*"*")
cacho=0
bsim=1.30
bovo=1.50
hamb=1.20
chee=1.30
refri=1.00
list=[]
while True:
    print("Cachorro quente | 100 | R$ 1,20")
    print(" Bauru simples  | 101 | R$ 1,30")
    print(" Bauru com ovo  | 102 | R$ 1,50")
    print("  Hambúrguer    | 103 | R$ 1,20")
    print(" Cheeseburguer  | 104 | R$ 1,30")
    print(" Refrigerante   | 105 | R$ 1,00")

    opção=int(input("Digite o código do produto, ou Digite 0 (zero) para sair: "))

    if opção==0:
        break
    else:
        quant = int(input("Insira a quantidade desejada: "))
        if opção == 100:

            list.append(1.20 * quant)
        elif opção == 101:
            list.append(1.30 * quant)
        elif opção==102:
            list.append(1.50*quant)
        elif opção== 103:
            list.append(1.20*quant)
        elif opção == 104:
            list.append(1.30*quant)
        elif opção == 105:
            list.append(1.00*quant)
soma=0
for j in list:
    soma=j+soma

print(f"O valor total da compra é {soma}R$")







