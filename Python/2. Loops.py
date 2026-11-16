print("Estructuras Repetitivas")

#For
for i in range(1,11):
    print(f'Número {i}')

for letra in ("Hola Mundo"):
    print(letra)

#While
contador = 1
while contador <= 3:
    print(f'Intento {contador}')
    contador+=1

#Do while
while True:
    numero = int (input('Ingrese Número >0: '))
    if numero > 0:
        break 