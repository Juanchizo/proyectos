#Ejercicio A).

#Recopilamos los datos en forma de variables.

MaximoCurso = 7
PromedioCurso = 4.5
MinimoCurso = 2.5
CursoDeDalto = 1.5

#Despues calculamos la diferencias de porcentaje de el curso de dalto entre los demas cursos, usando las variables.

DifMaximo = 100 - CursoDeDalto / MaximoCurso * 100
DifPromedio = 100 - CursoDeDalto / PromedioCurso * 100
DifMinimo = 100 - CursoDeDalto / MinimoCurso * 100

#Redondeamos los porcentajes

DifPromedio = int(DifPromedio)
DifMaximo = int(DifMaximo)
DifMinimo = int(DifMinimo)

#Ahora hacemos que escriba las diferencias

print(f"""Diferencia
      
El Curso Actual Dura {DifMaximo}% menos que El Curso Lento
{DifPromedio}% Menos que El Curso Promedio
Y {DifMinimo}% Menos que El Curso Rapido
""")

#Y Lito

#Ejercicio C).

#Actualizamos una variable cambiando su dato

CursoDeDalto = 10

CantMaximo = CursoDeDalto / MaximoCurso
CantPromedio = CursoDeDalto / PromedioCurso
CantMinimo = CursoDeDalto / MinimoCurso

print(f"""10 Horas del Curso de Dalto equivaleria a:

{CantMaximo} Cursos de El Lento
{CantMinimo} Cursos de El Rapido
{CantPromedio} Cursos de El Promedio""")