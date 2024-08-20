#Elif Se utiliza para agregar varias validaciones (Similar al Switch)
ingresoMensual = 600

if ingresoMensual > 10000:
  print('Puedes vivir en cualquier parte del mundo')

#Realiza otro tipo de validaciones para escenarios identificados antes de entrar al else 
elif ingresoMensual > 1000:
  print('Puedes vivir en latinoamerica')
  
elif ingresoMensual > 500:
  #If Anidados
  if ingresoMensual > 700:
    print('Puedes vivir en argentina')
  else:
    print('Puedes vivir en venezuela')
  
else:
  print('Eres pobre')