"""
Desempacotamento em lista
"""
lista = ['Everton', 'João', 'Anna', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nome1, nome2, nome3 = lista  # Desempacotamento
# print(nome1, nome3)
#######

# Porém se as variaveis não for o mesmo tanto que os elementos na lista, irá dar um erro de valores!
# nome1, nome2 = lista
# print(nome1, nome2)  # retorna erro de valor

# Para corrigir isso se ultiza *, fazendo um empacotamento dos restantes dos elementos!
nome1, nome2, *outra_lista = lista
print(nome1, nome2, outra_lista)  # Retorna elemento1, elemento2 e cria uma nova lista

# Posso pegar o ultimo elemento da lista, mesmo quando á um empacotamento!
nome1, nome2, *outra_lista, ultimo_elemento = lista
print(ultimo_elemento)  # retorna o n°10

# Posso também adquirir os ultimos elementos, e empacotando os outros elementos em uma lista!
*outra_list, antepenultimo, penultimo, ultimo = lista
print(antepenultimo, penultimo, ultimo)  # Retorna os n° 8, 9 e 10
