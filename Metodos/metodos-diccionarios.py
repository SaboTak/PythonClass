#Diccionario
diccionario = {
  'Nombre' : 'Sebastian',
  'Apellido': 'Gutierrez',
  'Edad' : 24
}

#Key - Devuelve las claves del diccionario
claves = diccionario.key()

#Get - Devuelve el valor de una clave
claves = diccionario.get('Nombre')
claves = diccionario[0] #Podemos usar el nombre de la key o la posicion del index

#Pop - Elimina el elemento
diccionario.pop('Nombre')

#Items - Para iterar el Diccionario
diccionarioIterable = diccionario.items()

#Clear - Elimina todos los elementos
diccionario.clear()