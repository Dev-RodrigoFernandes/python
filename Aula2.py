"""
Docstring for Aula2

Aula 2 Explica como funciona a função print.
Além de exibir informações na tela ela ja vem com algumas funções automaticamente como veremos abaixo
"""
#Todas as funções na programação esperam por argumentos para serem executados

print(1)

#É possível passar mais argumentos em 1 único print. Basta adicionar uma "," para separação de cada argumento.

print(1, 2)

#Por padrão os argumentos são separados por espaço, para alterar o separador, utilizamos a função sep

print(3, 4, sep="-")#O espaço será substituido pelo valor de sep

#Para o sep é possível utilizar aspas duplas ou aspas simples
print(5, 6, sep='-')

"""
Existe também uma forma de alterar o final do print com uma qubra de linha ou com um texto. bastante útil par concatenar informações.
Por padrão, o agumento nomeado end vem com \n e \r para pular a linha.
"""


print(7, 8, sep='-', end="Final do print")
print(9, 10, sep='-', end='Final do print')

