#Estas son las funciones integradas (built-in functions) más importantes de Python.
#No están todas, pero sí las que más usarás al empezar.



# 📘 ¿QUÉ SON LAS BUILT-IN FUNCTIONS EN PYTHON?

"""

Las built-in functions son herramientas que Python ya trae listas.
No tienes que crearlas ni importarlas.

👉 Son como botones del lenguaje: tú les das datos y ellas hacen algo por ti.

Ejemplo simple:

print("Hola")


print() ya existe, tú solo la usas.

    """
# 🧠 CÓMO LEER UNA FUNCIÓN

''' 
funcion(dato)
    ↑      ↑
    |      |
     nombre  argumento
     de la     o dato


funcion → qué va a hacer

(dato) → con qué lo va a hacer

devuelve algo o ejecuta una acción
'''

#🧩 CLASIFICACIÓN CLARA (IMPORTANTE)

""" 
Vamos a dividirlas por PARA QUÉ SIRVEN, no por nombre.

"""
# 1️⃣ FUNCIONES PARA VER / MOSTRAR COSAS


#  print()
"""
👉 Muestra información en pantalla

print("Hola mundo")

"""
input()
"""
👉 Recibe texto del usuario

nombre = input("¿Cómo te llamas? ")


📌 SIEMPRE devuelve texto (str)
 
 """
help()

"""
👉 Explica cualquier cosa de Python

help(str)

"""
# 2️⃣ FUNCIONES PARA SABER QUÉ ES ALGO


type()

"""
👉 Dice qué tipo de dato es

type(10)       # int
type("hola")   # str

"""
isinstance()

"""
👉 Pregunta: “¿esto es de este tipo?”

isinstance(10, int)   # True
"""
id()
"""
👉 Identificador interno del objeto (memoria)
(No se usa mucho al inicio)
"""

#3️⃣ FUNCIONES PARA CAMBIAR TIPOS (MUY IMPORTANTES)

int()

"""
👉 convierte a entero

int("10")  # 10

"""

float()

"""
👉 convierte a decimal

float("3.5")  # 3.5

"""

str()
"""
👉 convierte a texto

str(100)  # "100"
"""
bool()
"""
👉 convierte a verdadero o falso

bool(0)    # False
bool(10)   # True
"""
#4️⃣ FUNCIONES MATEMÁTICAS

abs()

"""
👉 valor absoluto

abs(-5)  # 5

"""

round()

"""

👉 redondear

round(3.6)   # 4
round(3.1416, 2)  # 3.14

"""

pow()

"""
👉 potencia

pow(2, 3)  # 8

"""
sum()

"""
👉 sumar varios números

sum([1, 2, 3])  # 6
"""

max() / min()

"""
👉 mayor / menor valor

max([1, 5, 3])  # 5
min([1, 5, 3])  # 1

"""
#5️⃣ FUNCIONES PARA LISTAS Y COLECCIONES

len()

"""
👉 cantidad de elementos

len([1, 2, 3])  # 3

"""

list()

"""

👉 crea una lista

list("abc")  # ['a','b','c']

"""

tuple()

"""

👉 lista que NO se puede modificar

tuple([1,2])

"""

set()

"""
👉 elimina duplicados

set([1,1,2,3])  # {1,2,3}

"""

sorted()

"""
👉 ordena

sorted([3,1,2])  # [1,2,3]

"""

#6️⃣ FUNCIONES PARA RECORRER DATOS (CLAVE EN PYTHON)

range()

"""
👉 genera números

range(5)  # 0,1,2,3,4

"""

enumerate()

"""
👉 índice + valor

for i, v in enumerate(["a","b"]):
    print(i, v)

"""

zip()

"""
👉 une listas

zip([1,2], ["a","b"])

"""

iter() / next()

"""
👉 recorrido manual (avanzado)

"""

#7️⃣ FUNCIONES LÓGICAS

all()

"""
👉 todo debe ser verdadero

all([True, True])  # True

"""

any()

"""
👉 al menos uno verdadero

any([False, True])  # True

"""

#8️⃣ FUNCIONES DE TEXTO Y CARACTERES

ord()

"""
👉 letra → número

ord("A")  # 65

"""

chr()

"""
👉 número → letra

chr(65)  # "A"

"""

format()

"""
👉 formatear texto/números

format(3.1416, ".2f")  # "3.14"

"""

#9️⃣ FUNCIONES PELIGROSAS (APRENDER PERO NO USAR AÚN)

eval()

"""
👉 ejecuta texto como código ⚠️

"""

exec()

"""
👉 ejecuta bloques de código ⚠️

❌ NO usar con datos del usuario

"""

#🔟 FUNCIONES DE CLASES (OOP)

property()

"""
👉 controla acceso a atributos

"""
staticmethod()

"""
👉 método sin objeto

"""
classmethod()

"""
👉 método de clase

"""

super()

"""
👉 acceder a la clase padre

"""
#📌 Estas se entienden mejor cuando veas clases


#🧠 RESUMEN MENTAL (QUÉ RECORDAR)

"""
print()                         → #mostrar

input()                         → #recibir

int / float / str / bool        → #convertir

len()                           → contar

range()                         → generar

list / tuple / set / dict       → estructuras

sum / max / min                 → cálculos

type / isinstance               → entender datos

"""