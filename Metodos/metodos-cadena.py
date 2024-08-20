#Metodos por defecto de python para strings
cadena1 = 'Hola soy sabo'
cadena2 = 'y estoy aprendiendo python.'

#DIR - Devuelve la lista de metodos del objeto enviado por parametros
resultado = dir(cadena1)

#UPPER - Convierte el str a mayuscula
resultado = cadena1.upper()

#LOWER - Convierte el str a minuscula
resultado = cadena1.lower()

#CAPITALIZE - Convierta la primera letra en mayuscula
resultado = cadena1.capitalize()

#FIND - Encuentra la primera aparacion del valor enviado por parametro, sino devuelve -1
resultado = cadena1.find("a")

#INDEX - Encuentra la primera aparacion del valor enviado por parametro, sino devuelve una excepcion 
resultado = cadena1.index("a")

#ISNUMERIC - Si es numerico devuelve True
resultado = cadena1.isnumeric()

#ISALPHA - Si es alfa devuelve True
resultado = cadena1.isalpha()

#COUNT - Devuelve el numero de ocurrencias de una subcadena en la cadena enviada 
resultado = cadena1.count('a')

#LEN - Cuenta los caracteres de una cadena
resultado = len(cadena1)

#ENDSWITH - Verifica si la cadena termina con
resultado = cadena1.endswith('Ho')

#STARTWITH - Verifica si la cadena comienza con 
resultado = cadena1.startswith('Ho')

#REPLACE - Remplaza un valor de la cadena por otro valor indicado en el parametro
resultado = cadena1.replace('la','lu')

#SPLIT - Separa una cadena por el parametro indicado
resultado = cadena1.split(',')