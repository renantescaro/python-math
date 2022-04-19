import re


entrada = '+x²+6x+13'
lista = re.findall('[+-][0-9]?.X?²?', entrada)

print(lista)
