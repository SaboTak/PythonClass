# EJERCICIO 1
# a) Diferencia en porcentaje entre el curso actual y:
#   -El mas rapido de otros cursos
#   -El mas lento de otros cursos
#   -El promedio de otros cursos
  
# b) Porcentaje de material inservible que se reduce en:
#   -El promedio de los cursos
#   -El curso actual
  
# c) Ver 10 hrs de este curso a cuantas horas de otros cursos equivale? y al reves.

esteCursoFinal = 1.5
esteCursoCrudo = 3.5
otrosCursosMinimo = 2.5
otrosCursosPromedio = 4
otrosCursosMaximo = 7
otrosCursosCrudo = 5

# Desarrollo a)
#   -El más rápido de otros cursos
cursoActualVsMasRapido = 100 - esteCursoFinal / otrosCursosMinimo * 100
print(f'El % de diferencia con el curso más rápido es del: {cursoActualVsMasRapido}')

#   -El más lento de otros cursos
cursoActualVsMasLento = 100 - esteCursoFinal * 1000 // otrosCursosMaximo / 10
print(f'El % de diferencia con el curso más lento es del: {cursoActualVsMasLento}')

#   -El promedio de otros cursos
cursoActualVsPromedio = 100 - esteCursoFinal / otrosCursosPromedio * 100
print(f'El % de diferencia con el curso promedio es del: {cursoActualVsPromedio}')

# Desarrollo b)
#   -El promedio de los cursos
materialInserviblePromedio = 100 - otrosCursosPromedio * 1000 // otrosCursosCrudo / 10
print(f'El % de material inservible reducido en el promedio de los cursos es del: {materialInserviblePromedio}')

#   -El curso actual
materialInservibleActual = 100 - esteCursoFinal * 1000 // esteCursoCrudo / 10
print(f'El % de material inservible reducido en el curso actual es del: {materialInservibleActual}')

# Desarrollo c)
#   -Ver 10 hrs de este curso a cuantas horas de otros cursos equivale? y al reves.
equivalencia = otrosCursosPromedio * 100 // esteCursoFinal / 10

print(f'Ver 10hrs del curso actual equivale ver : {equivalencia}')

#Al reves
equivalencia = esteCursoFinal * 100 // otrosCursosPromedio / 10

print(f'Ver 10hrs de otros cursos equivale ver : {equivalencia}')