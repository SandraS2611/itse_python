# Primer programa
print("Hola Mundo!")

# Variable y Tipos de Variable
saludo = "Hola"
print(f"mensaje : {saludo}")
print(f"tipo de dato: {type(saludo)}")

# Tipos de Dato Nulo
saludo = None
print(
    f"El valor de la variable saludo es: {saludo} y su tipo de dato es: {type(saludo)}"
)

# Tipos de Dato Booleano
es_cierto = True
print(
    f"El valor da lo variable es_cierto es: {es_cierto} y"
    + f"su tipo de datos es: {type(es_cierto)}"
)

es_cierto = False
print(
    f"El valor da lo variable es_cierto es: {es_cierto} y"
    + f"su tipo de datos es: {type(es_cierto)}"
)

# Tipo de Dato Numérico
print(2 + 2)
print(50 - 5 * 6)
print((50 - 5 * 6) / 4)
print(8 / 5)  # la operación división retorna un número decimal

print(17 / 3)  # la operación división retorna un tipo float
print(17 // 3)  # la división retorna sólo la parte entera
print(17 % 3)  # la división retorna sólo el resto
print(
    5 * 3 + 2
)  # la multiplicación retorna un número perteneciente al mayor conjunto numérico

print(5**2)  # 5 al cuadrado
print(2**7)  # 2 elevado a la 7

base = 20
altura = 5 * 9
print(base * altura)

# print(numero) # variable no está «definida»
# Traceback (most recent call last):
# File "c:\Users\solss\Desktop\ITSE\Programaci�n\python\prueba.py", line 38, in <module>
#  print(numero) # variable no est� �definida�
#       ^^^^^^
# NameError: name 'numero' is not defined

print(4 * 3.75 - 1)

#Tipo de Dato Alfanumérico, Cadena de caracteres o String
print('hola mundo')
print("hola mundo")
print('"Maria" es su nombre.')
print("'Maria' es su nombre.")

print('C:\Windows\nombre')  # ejecuta el \n (nueva línea)
print(r'C:\Windows\nombre')  # imprime sin analizar la cadena

print("""\
 usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
 Options and arguments (and corresponding environment variables):-V     : print the Python version number and exit (also --version)
         when given twice, print more information about the build""")

print(3 * '1er' + ' dos')  # multiplica la 1er cadena y concatena la siguiente

saludo = "hola"
print(saludo + ' mundo')

texto = "Python"
print(texto[0])  # primer caracter
print(texto[1])  # segundo caracter
print(texto[2])  # tercer caracter
print(texto[3])  # cuarto caracter
print(texto[-0])  # igual al indice 0
print(texto[-1])  # último caracter
print(texto[-2])  # ante último caracter
print(texto[-3])  # primer caracter

texto='Python'
print(texto[:2]) # desde el 1er caracter hasta la posición 2 (excluida)
print(texto[4:]) # desde la posición 4 (incluida) hasta la última
print(texto[-2:]) # desde la posición -2 (incluida) hasta la última
print(texto[:2] + texto[2:])
print(texto[:4] + texto[4:])

print(texto[2:13]) # desde la posición 2 (incluida) hasta la última

#texto = 'Python'
#texto[5] = 's'
#
#ERROR!
# Traceback (most recent call last):
#  File "<main.py>", line 2, in <module>
# TypeError: 'str' object does not support item assignment

texto = "Python"
print("la longitud del texto es: ", end="")  # no imprime el caracter fin de línea
print(len(texto))  # a continuación imprime la longitud
print(f"la longitud del texto es: {len(texto)}")  # nueva forma de imprimir