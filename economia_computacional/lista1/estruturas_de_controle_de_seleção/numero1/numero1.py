"""
Programa: Numero1
Descrição: Este programa imprime na tela o dobro de um número se ele for menor do que 10. Se o número
for de 10 até 20, ele imprime a sua metade. Em qualquer outro caso, imprime na tela que o
número não é válido.
Autor: Pedro Papini Almeida
Data: 23/06/2023
"""

#Atribuição de dados
x = float(input("Qual o número?"))




#Entrada de dados






#Processamento de dados
if x < 10:
    x = (x*2)
elif 10 <= x <= 20:
        x = (x/2)
else:
    x = "Seu número é inválido"






#Saída de dados
print(x)