#Programa feito por mim para teste de como fazer uma senha funcionar
# para que a mensagem de Seja bem Vindo apareça, digite o nome Lucas.
#Caso contrário aparecerá uma mensagem de erro e solicitando que digite novamente.

NOME = str("Lucas")
s = str("Seja bem vindo Lucas!")
ss = str("Correto! Seja bem vindo Lucas!")

pergunta = input("Qual é o seu nome?")
if pergunta == NOME:
    print(s)
else:print("Nome inválido")
if pergunta != NOME: print("Digite novamnte")
while pergunta != NOME:
    pergunta = input("Qual o seu nome corretamente?")
    if pergunta == NOME:
        print(ss)
    else:
        print("Nome inválido")




