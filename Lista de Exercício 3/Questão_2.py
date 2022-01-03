print (20*"*")
print ("     Questão 2")
print (20*"*")
listaj=[]
listaad=[]
listai=[]
while True:
    controle=float(input("Digite 1 para adcionar uma idade\nDigite 2 para finalizar: "))
    if controle == 2 or controle != 1:
        break
    else:
        idade=int(input("Digite a idade de pessoa : "))
        listaj.append(idade)
soma=0
for j in listaj:
    soma = j + soma


x=len(listaj)
media= soma / x
print(media)
if media>0 and media<=25:
    print(f"O grupo é jovem com média de {media} ")
elif media>=26 and media<60:
    print(f"O grupo é adulto com média de {media} ")
elif media>60:
    print(f"O grupo é idoso com média de {media} ")



