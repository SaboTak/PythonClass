#LIST - Crea una lista
lista = list(["hola",19,False])

#LEN - Cuenta la cantidad de elementos de una lista
resultado = len(lista)

#APPEND - Agrega un elemento a la lista
lista.append("probando")

#INSERT - Agrega un elemento a la lista en un indece especifico
lista.insert(0,"probando")

#EXTEND - Agrega varios elementos a la lista
lista.extend([False,2024])

#POP - Elimina un elemento de la lista, pide el indice y devuelve el valor
# haciendo pop con -1 elimina el ultimo
lista.pop(2)

#REMOVE - Remueve un elemento de la lista, pide el valor a eliminar
#Si hay mas de un elemento igual elimina solamente 1 y es el mas cercano al indice 0
lista.remove(False)

#CLEAR - Elimina todos los elemetos de una lista
lista.clear()

#SORT - Ordena una lista de forma ascendente a desescendente
#No puede ejecutarse si hay string en la cadena
#False => o , True => 1
#Si agregamos por parametros reverse = True, lor ordena desescentemente
lista.sort()
lista.sort(reverse=True)

#REVERSE - Invierte los elementos de una lista
lista.reverse()