#SQL
""" Structure Query Language (SQL) o Lenguaje de consulta estructurado son bases de datos relacionales donde la informacion se encuentra almacenada en un conjunto de tablas, desde donde podemos acceder a dichos datos almacenados sin necesidad de modificar o manipular las tablas. Se debe tener en cuenta que primero se debe determinar la estructura de los SQL ya que si se modifica algun dato interno se puede perjudicar todo el sistema al estar compuesto por tablas relacionadas.

Un ejemplo para entender este concepto es un restaurante (tabla), este restaurante posee informacion como sus empleados: meseros, cocineros, porteros. Ademas los empleados poseen elementos como edad, nacionalidad o idioma. El restaurante funcionaria como la tabla y los empleados es la informacion que esta relacionada a ella, si a futuro cambiamos un elemento de los porteros como el idioma se generaria un problema puesto que se esta cambiando un atributo no relacional con el resto. |Sentencia basica: SELECT * FROM people|

Bases de datos relacinonales: MySQL, Oracle, PostgreSQL.
"""

#NoSQL
"""Not only SQL (NoSQL) No solo SQL son bases de datos no relacionales, tal como su nombre lo indica los datos no se almacenan en tablas sino que poseen un esquema dinamico por lo tanto cada elemento posee su propia estructura sin afectar los demas, solucionando el gran inconveniente de los SQL. |Sentencia basica: find()|

Bases de datos no relacionales: MongoDB; Redis, Apache CouchDB.
"""

#Algoritmo
"""Es una serie de pasos definidos, que van secuencialmente y logran un objetivo de la mejor forma. La construccion de un algoritmo requiere que tengas en cuenta 3 elementos escenciales: Analizar el problema, Crear un paso a paso (Generalmente representado como un diagrama de flujo) y buscar la forma de optimizar el algoritmo.

Ejemplo de algoritmo de un combate por turnos: 1. Seleccion de ataque jugador 1 (J1) --> |Fuego - Agua - Tierra| --> Seleccion de ataque jugador 2 (J2) --> |Fuego - Agua - Tierra| --> Ejecucion de ataques --> Daño realizado a J1 --> Daño realizado a J2 --> Continua vivo J1 --> Si --> Continua vivo J2 --> Si --> Seleccion de ataque jugador 1 (J1)... (Se repite ciclo) --> Continua vivo J1 --> No --> Pierde J1 --> Fin del combate
"""

#Paradigmas
"""Es la forma en que se clasifica un lenguaje de programacion por sus caracteristicas o un estilo de programacion basado en la forma en que aborda un programa y las herramientas que utiliza.
Existen mas de 100 paragdimas distintos, pero hay 3 que son los mas populares e implementados: Imperativo (Por procedimiento, orientado a objetos), Declarativo (Funcional, logico, matematico, reactivo), Dirigido por eventos.

Imperativo: Se dan ordenes directas y enfocadas al "como realizar algo" en el lenguaje de programacion, por lo tanto las instrucciones son paso a paso. Ej: Fortran, Java, C, Python, Ruby, PHP
Declarativo: Es contrario al imperativo enfocandose al "resultado" pasando el como a un segundo plano lo cual es util para reducir o eliminar efectos secundarios o colaterales en la programacion. Ej: Prolog, LISP, Haskell, SQL, Elixir.
Dirigido por eventos: No controla la secuencia de ejecuciones sino que reacciona a los sucesos ocurridos, tambien es considerado como una mezcla de Imperativo y Declarativo. Ej: Java, JavaScript, C#
"""

#Python
#While - Bucle indefinido
"""cicloWhile = 1

while cicloWhile <= 100:
    print(cicloWhile)
    cicloWhile += 1
"""

#for - bucle definido
"""numeros = ['1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 ,23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100']
for cicloFor in numeros:
    print(cicloFor)
"""

#Diccionario

nombre = input('Cual es tu nombre: ')
edad = int(input('Cual es tu edad: '))
direccion = input('Cual es tu direccion: ')
telefono = int(input('Cual es tu numero de telefono: '))

diccionario = { 'Name' : nombre, 'Age' : edad, 'Address' : direccion, 'PhoneNum' : telefono}

print(f'Futuro programador {nombre}, tienes {edad} años, vives en {direccion} (Chimba de lugar) y tu numero de telefono es {telefono}. :)')

for valor in diccionario.values():
    print(valor)