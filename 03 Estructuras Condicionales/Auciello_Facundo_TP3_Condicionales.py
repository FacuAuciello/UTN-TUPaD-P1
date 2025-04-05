#Ejercicio 1
#edad = int (input("Ingresa tu edad:"))

#if edad >= 18:
#    print ("Es mayor de edad")
#else:
#    print ("No es mayor de edad")

#Ejercicio 2
#nota = int (input("Ingresa tu nota:"))

#if nota >= 6:
#    print ("Aprobado")
#else:
#    print ("Desaprobado")

#Ejercicio 3
#numero = int (input("Ingrese un numero:"))

#if (numero % 2 == 0):
#    print("Ha ingresado un numero par")
#else:
#    print("Por favor, ingrese un numero par")

#Ejercicio 4
#edad_usuario = int (input("Ingresa tu edad:"))
#print (edad_usuario)

#if edad_usuario < 12:
#    print ("Niño/a")
#elif edad_usuario >= 12 and edad_usuario < 18:
#    print ("Adolescente")
#elif edad_usuario >= 18 and edad_usuario < 30:
#    print ("Adulto/a joven")
#else:
#    print ("Adulto/a")

#Ejercicio 5
#contrasenia = input ("Ingrese su contraseña")

#if  len(contrasenia) >=8 and len(contrasenia) <=14:
#    print ("Ha ingresado una contraseña correcta")
#else:
#    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
#from statistics import mode, median, mean
#import random

#numeros_aleatorios = [random.randint (1,100) for i in range (50)]
#media = mean (numeros_aleatorios)
#mediana = median (numeros_aleatorios)
#moda = mode (numeros_aleatorios)

#print (f"media {media}")
#print (f"mediana {mediana}")
#print (f"moda {moda}")

#if media > mediana > moda:
#    print ("Sesgo positivo")
#elif media < mediana < moda:
#    print ("Sesgo negativo")
#else:
#    print ("Sin sesgo")     

#Ejercicio 7
#vocales = "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"
#frase_palabra = input ("Ingresa una frase o palabra:")

#if (frase_palabra [-1] in vocales):
#    print (f"{frase_palabra} !")
#else:
#    print (f"{frase_palabra}")

#Ejercicio 8
#nombre = input ("Ingresa tu nombre:")
#print ("1. Si queres tu nombre en mayusculas.")
#print ("2. Si queres tu nombre en minusculas.")
#print ("3. Si queres que tu nombre tenga la primer letra con mayuscula.")
#opcion_deseada = input("Marca el numero de la opcion deseada:")

#if opcion_deseada == "1":
#    print (nombre.upper())
#elif opcion_deseada == "2":
#    print (nombre.lower())
#elif opcion_deseada == "3":
#    print (nombre.title())
#else:
#    print ("Ingresa una opcion valida")

#Ejercicio 9
#magnitud_terremoto = int (input("Ingresa el numero de la magnitud del terremoto segun la escala de Richter:"))

#if magnitud_terremoto < 3:
#    print ("Muy leve (imperceptible)")
#elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
#    print ("Leve (ligeramente perceptible)")
#elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
#    print ("Moderado (sentido por personas, pero generalmente no causa daños)")
#elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
#    print ("Fuerte (puede causar daños en estructuras debiles)")
#elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
#    print ("Muy fuerte (puede causar daños significativos)")
#elif magnitud_terremoto >= 7:
#    print ("Extremo (puede causar daños a gran escala)")
#else:
#    print ("Ingrese un numero valido")

#Ejercicio 10
#inputs para saber la info del usuario
#usuario_hemisferio = input ("Ingrese en cual hemisferio se encuentra (norte/sur):")
#usuario_mes = int (input ("Ingrese el mes actual en numero:"))
#usuario_dia = int (input ("Ingrese dia actual en numero:"))

#en que mes se encuentra
#enero = "1"
#febrero = "2"
#marzo = "3"
#abril = "4"
#mayo = "5"
#junio = "6"
#julio = "7"
#agosto = "8"
#septiembre = "9"
#octubre = "10"
#noviembre = "11"
#diciembre = "12"

#HEMISFERIO SUR. CLAVE AGREGAR IF ELSE DENTRO DE LA LOGICA SINO ME MUESTRA AMBOS HEMISFERIOS POR FUERA.
#if usuario_hemisferio == "sur":
#   print ("Hemisferio sur")

#    if (usuario_mes == 12 and usuario_dia >= 21) or (usuario_mes == 1) or (usuario_mes == 2) or (usuario_mes == 3 and usuario_dia <= 20):
#        print ("Estas en verano")
#    elif (usuario_mes == 3 and usuario_dia >= 21) or (usuario_mes == 4) or (usuario_mes == 5) or (usuario_mes == 6 and usuario_dia <= 20):
#        print ("Estas en otoño")
#    elif (usuario_mes == 6 and usuario_dia >= 21) or (usuario_mes == 7) or (usuario_mes == 8) or (usuario_mes == 9 and usuario_dia <= 20):
#        print ("Estas en invierno")
#    elif (usuario_mes == 9 and usuario_dia >= 21) or (usuario_mes == 10) or (usuario_mes == 11) or (usuario_mes == 12 and usuario_dia <= 20):
#        print ("Estas en primavera")
#    else:
#        print ("Ingresa un numero valido")

#HEMISFERIO NORTE
#elif usuario_hemisferio == "norte":
#    print ("Hemisferio norte")

#    if (usuario_mes == 12 and usuario_dia >= 21) or (usuario_mes == 1) or (usuario_mes == 2) or (usuario_mes == 3 and usuario_dia <= 20):
#        print ("Estas en invierno")
#    elif (usuario_mes == 3 and usuario_dia >= 21) or (usuario_mes == 4) or (usuario_mes == 5) or (usuario_mes == 6 and usuario_dia <= 20):
#        print ("Estas en primavera")
#    elif (usuario_mes == 6 and usuario_dia >= 21) or (usuario_mes == 7) or (usuario_mes == 8) or (usuario_mes == 9 and usuario_dia <= 20):
#        print ("Estas en verano")
#    elif (usuario_mes == 9 and usuario_dia >= 21) or (usuario_mes == 10) or (usuario_mes == 11) or (usuario_mes == 12 and usuario_dia <= 20):
#        print ("Estas en otoño")
#    else:
#        print ("Ingresa un numero valido")

#else:
#    print ("Ingresa un hemisferio valido")











