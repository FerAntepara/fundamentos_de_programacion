# 1
x = 2
while True:
    x += 1
    print(x)
    if x == 10:
        print('fin del ciclo')
        break

# 2
oracion = 'la cereza crece en el pico del arbol'
for vocal in oracion:
    if vocal == 'i':
        print('La i fue seleccionada')
        break
    print(vocal)

# 3
nombre = str(input('Ingrese su nombre: '))
for letra in nombre:
    if letra == 'a' or letra == 'e':
        print("Se encontró la letra")
        break
    print(letra)