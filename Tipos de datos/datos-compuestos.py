#Las listas guardan elementos de cualquier tipo
lista = ["Sebas","Gutierrez",True,1.80]

#Accedemos a un elemento de la lista (Recordar contar desde el 0)
lista[1] = 'actualice el valor del indice'
print(lista[1])

#Las Tuplas guardan elementos de cualquier tipo (no se puede modificar)
tupla = ("Sebas","Gutierrez",True,1.80)

#tupla[1] = 'actualice el valor del indice' -- No es Valido
print(tupla[1])

#Creando un conjunto (set) - (no se puede modificar) - (No permite repetir un valor)
conjunto = {"Sebas","Gutierrez",True,1.80}

#No se puede accer mediante un indice a un conjunto
#print(conjunto[1]) -- No es Valido
print(conjunto)

#Creando un diccionario (dict) {key:value}
diccionario = {
  'nombre': 'Sabo',
  'apellido': 'Gutierrez'
}

#Asi se accede a un valor de un diccionario
print(diccionario["nombre"])