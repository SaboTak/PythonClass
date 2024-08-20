#Las variables se utilizan para almacenar informacion
nombre = "Sabo"
#Puedo re definir variables para cambiar la informacion
nombre = 'Pedrito'

numero = 10
#La expresion singnifica: el valor que tienes ya en la variable + lo que este despues del =
numero +=1

#Concatenar strings de forma clasica
bienvenida = 'Hola ' + nombre + ', ¿como estas?'

#Concatenar strings de forma optima
bienvenida = f'Hola {nombre}, ¿como estas?'

#Borrar datos de una variable
del nombre

#Operadores de pertenencia (Case sensitive)
incluye = 'ola' in bienvenida
incluye = 'ola' not in bienvenida

print(bienvenida)