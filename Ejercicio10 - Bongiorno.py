nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#inciso A
def relacionar_notas() :
  """Generar una estructura con todas las notas relacionando el nombre del estudiante con las notas. 
  Utilizar esta estructura para la resolución de los siguientes items."""
  lista_nombres = nombres.split(',')
  i = 0
  alumnos = {}
  todas_las_notas = list(zip(notas_1,notas_2))
  for elem in lista_nombres :
    alumnos[elem] = todas_las_notas[i]
    i += 1
  return alumnos

#inciso B
def calcular_promedios (alumnos) :
  """Calcular el promedio de notas de cada estudiante."""
  promedios = {}
  for elem in alumnos :
    promedios [elem] = sum(alumnos[elem]) / 2
  return promedios

#inciso C
def promedio_general (promedios) :
  """Calcular e impirmir el promedio general del curso."""
  promedio_general = (sum(promedios.values()) / len(promedios))
  print (f'Promedio general del curso es {promedio_general} ')

#inciso D
def promedio_mas_alto (promedios):
  """Identificar e imprimir al estudiante con la nota promedio más alta."""
  promedio_max = max(promedios.values())
  for elem in promedios :
    if promedios[elem] == promedio_max :
      alumno = elem
  print (f'Promedio mas alto es {promedio_max} del alumno/a {alumno}')

#inciso E
def nota_mas_baja (alumnos) :
  """Identificar e imprimir al estudiante con la nota más baja."""
  nota_min = min(alumnos.values())
  for elem in alumnos :
    if alumnos[elem] == nota_min :
      alu = elem
  print (f'Nota mas baja es {min(nota_min)} del alumno/a {alu}')

alumnos = relacionar_notas()
print (alumnos)
promedios = calcular_promedios (alumnos)
print (f'Promedios: {promedios}')
promedio_general (promedios)
promedio_mas_alto (promedios)
nota_mas_baja (alumnos)