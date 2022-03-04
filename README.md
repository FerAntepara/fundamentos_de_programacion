# ¿Qué es Python? 👩‍💻  
En términos técnicos, Python es un lenguaje de programación de alto nivel, orientado a objetos, con una semántica dinámica integrada, principalmente para el desarrollo web y de aplicaciones informáticas.
# ¿Qué es una variable? 📁  
Una variable está formada por un espacio en el sistema de almacenaje (memoria principal de un ordenador) y un nombre simbólico (un identificador) que está asociado a dicho espacio.
## Nombrando una variable 📂
```Python 
dato
```
## Asignando valores a una variable 📂
```Python
dato = 40  
dato = "buenos dias"
# lo que se encuentra despues del "=" es el valor que tomo la variable
```
## Operadores básicos 📂
```Python
suma : +  
resta : -  
módulo : %  
potenciación : **  
multiplicación : *  
división : /  
```
### Suma ⌨️
```Python
operacion = 12 + 43  
    print (operacion)
```
### Resta ⌨️
```Python  
operacion = 43 - 12  
    print (operacion)
```
### Multiplicación ⌨️
```Python
operacion = 43 * 2  
    print (operacion)
```
### División ⌨️
```Python
operacion = 50 / 2  
    print (operacion)
```
### Módulo ⌨️
```Python
operacion = 100 % 2  
    print (operacion)
```
### Potencia ⌨️
```Python
operacion = 50 ** 2  
    print (operacion)
```
# Tipos de datos en Python 📁
## Integer 📂
Se define por la palabra int. En el se almacenan todos lod numeros con un valor entero.

ejemplo:
```Python
num1 = 143  
num2 = 43
```
## Float 📂
Float es un tipo de dato donde se almacenan los decimales. Tambien se incluyen los numeros en notación cientifica.

ejemplo:
```Python
num1 = 53.2  
num2 = 54e2
```
## String 📂
Se representa a traves de str. String funciona para almacenar cadenas de palabras.

ejemplo:  
```Python
mensaje = str(input("Escriba un mensaje: "))
print(mensaje)
```
## Casting en Python 📂
El casting nos sirve para transformar un tipo de dato en otro(int, str, float).

ejemplo:
```Python
num1 = 8   #int 
num2 = 102.4 #float 
num1 = num1 + num2  
print(num1)       
print(type(num1)) #float
```
## List 📂
Una lista nos permite almacenar datos de todo tipo(int, float, str), para posteriormente utilizarlos ya sea imprimiendo los datos pedidos o haciendo operaciones donde se necesiten datos predeterminados.

ejemplo:
```Python
factura = ['pan', 'huevos', 100, 1234]
print (factura[2])
```
## Tuple 📂
Un tuple es una colección de datos cuyo orden es inalterable, en otras palabras un tuple esta ordenado por importancia.

ejemplo:
```Python
valores = ("Python", True, 10)
print (valores.index(True))
```
## Dictionary 📂
Asi como tuple un diccionario nos permite almacenar datos ya sean, int, float, str para posteriormente ser utilizados segun se necesite.

ejemplo:
```Python
diccionario = dict
diccionario = {'mascota' : 'perro', 'raza' : "labrador", 'edad': 10}

print (diccionario['mascota'])  
print (diccionario['raza']) 
print (diccionario['edad'])
```
# Tomando decisiones 📁
## Sentencia if 📂
If solo permite que el programa ejecute cuando su condicion se cumple

ejemplo:
```Python
num1 = 23  
if num1 == 23:  
    print('bien hecho')  
```
## Ciclo For 📂
El bucle for es una estructura de control en programación en la que se puede indicar de antemano el número máximo de iteraciones

ejemplo:
```Python
num1 = [43, 78.4, 92, 32]  
for n in num1:  
    print(n)
```
## Ciclo While 📂
Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición.

ejemplo:
```Python
i=0  
while i < 10:      
    i += 1  
    print (i)
  ```
## Break 📂:  
Debe poner la instrucción break dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una instrucción if condicional.

ejemplo:
```Python
i = 0  
while i < 20:  
    i += 2  
    if i == 8:  
        break  
    print(i)
```
## Continue 📂
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa.

ejemplo:
```Python
i = 0  
while i < 20:  
    i += 2  
    if i == 7:  
        continue  
    print(i)
```