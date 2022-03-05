# 1
diccionario = dict
diccionario = {'mascota' : 'perro', 'raza' : "labrador", 'edad': 10}

print (diccionario['mascota'])  
print (diccionario['raza']) 
print (diccionario['edad'])

# 2 
diccionario2 = dict
diccionario2 = {
    1 : 'iron', 2: 'lk', 
    3 : 'hu', 4 : 'man', 
    5 : 'bat', 6 : 'man'

}

resultado1 = ( diccionario2[1] + diccionario2[6])
resultado2 = ( diccionario2[5] + diccionario2[4])
resultado3 = ( diccionario2[3] + diccionario2[2])

print (resultado1, resultado2, resultado3)

# 3
nombre = str(input('Ingrese su nombre: '))
apellido = str(input('Ingrese su apellido: '))

nombre_apellido = dict
nombre_apellido = {
    'nombre:' : nombre , 'apellido:' : apellido
}

print (nombre_apellido)