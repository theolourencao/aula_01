
input_1 = input('Digite um valor: ')
input_2 = input('Digite outro valor: ')

list = [input_1, input_2]

lista_numeros = []

for n in list:
     numero = int(n)
     lista_numeros.append(numero)

def soma_numero(lista):
    total = sum(lista_numeros)
    return total

total = soma_numero(lista_numeros)
     
print('O total é: '+str(total))    

     