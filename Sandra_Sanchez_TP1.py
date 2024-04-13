# #DESAFÍO 1
# n_cliente = int(input("Ingrese el número de cliente: "))

# if n_cliente == 1000:
#   print("Ganaste un premio")


# #DESAFÍO 2
# nro1 = int(input("Ingrese un número: "))
# nro2 = int(input("Ingrese un número: "))

# if nro1 > nro2:
#  print(nro2)

# else:
#  nro1 < nro2
#  print(nro1)


# #DESAFÍO 3
# nro1 = int(input("Ingrese un número: "))
# nro2 = int(input("Ingrese un número: "))

# if nro1 > nro2:
#  print(nro2)

# elif nro1 < nro2:
#  print(nro1)

# else:
#  print("Los números son iguales: " + str(nro1))


# DESAFÍO 4
semana = ["lunes", "martes", "miercoles", "jueves", "viernes"]
fin_de_semana = ["sabado", "domingo"]


dia = input("Ingrese un día de la semana: ")

if dia == "lunes":
  print("Hoy es: " + semana[0])
if dia == "martes":
  print("Hoy es: " + semana[1])
if dia == "miercoles":
  print("Hoy es: " + semana[2])
if dia == "jueves":
  print("Hoy es: " + semana[3])
if dia == "viernes":
  print("Hoy es: " + semana[4] + " y es el último día hábil.")  
elif dia != semana and dia in fin_de_semana:
  print("Es fin de semana.")
