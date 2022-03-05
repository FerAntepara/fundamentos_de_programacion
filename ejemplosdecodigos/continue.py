# 1
while True:
    nombre = str(input('Ingrese su nombre: '))
    if nombre != 'Fernanda':
        continue
    print('Hola Fernanda')
    break

# 2
nombre = str(input('Ingrese su nombre: '))
for letra in nombre:
    if letra == 'a' or letra == 'e':
        print("Se encontró la letra")
        continue
    print('Letra: ' + letra)

# 3
oracion = 'la cereza crece en el pico del arbol'
for vocal in oracion:
    if vocal == 'i':
        print('La i fue seleccionada')
        continue
    print(vocal)