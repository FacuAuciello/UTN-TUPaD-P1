#1)Primer ejercicio

#def imprimir_hola_mundo():
#    print("Hola mundo!")

#imprimir_hola_mundo()

#2)Segundo ejercicio

#def saludar_usuario(nombre):
#    print(f"Hola {nombre}!")

#nombre = str (input("Ingresa un nombre: "))

#saludar_usuario(nombre)

#3)Tercer ejercicio

#def informacion_personal(nombre, apellido, edad, residencia):
#    print (f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}")

#nombre = str(input("Ingresa tu nombre: "))
#apellido = str(input("Ingresa tu apellido: "))
#edad = int(input("Ingresa tu edad: "))
#residencia = str(input("Ingresa tu residencia: "))

#informacion_personal(nombre, apellido, edad, residencia)

#4) Cuarto ejercicio

#def calcular_area_circulo(radio):
#    area = 3.14 * radio**2
#    print(f"AREA del circulo: {area}")

#def calcular_perimetro_circulo(radio):
#    perimetro = 2 * 3.14 * radio
#    print (f"PERIMETRO del circulo: {perimetro}") 

#radio = int(input("Ingresa el radio: "))

#calcular_area_circulo(radio)
#calcular_perimetro_circulo(radio)

#5)Quinto ejercicio

#def segundos_a_horas(segundos):
#    horas = segundos // 3600
#    return horas
    
#usuarioSegundos = int(input("Ingresa segundos para convertirlos en horas: "))

#horas = segundos_a_horas(usuarioSegundos)
#print(f"Horas: {horas}")

#6)Sexto ejercicio

#def tabla_multiplicar(numero):
#    for i in range (1,11,1):
#        multiplicar = numero * i
#        print(f"{numero} X {i} = {multiplicar}")

#numero = int(input("Ingresa un numero del 1 al 10: "))

#tabla_multiplicar(numero)

#7)Septimo ejercicio

#def suma (a,b):
#    return a + b

#def resta (a,b):
#    return a - b

#def multiplicacion (a,b):
#    return a * b

#def division (a,b):
#    if b == 0:
#        return "Error. No se puede dividir por cero"
#    return a / b

#def operaciones_basicas(a,b):
#    return (suma(a,b), resta(a,b), multiplicacion(a,b), division(a,b))

#a = int(input("Ingresa el primer numero: "))
#b = int(input("Ingresa el segundo numero: "))

#resultado = operaciones_basicas(a,b)

#print(f"Suma: {resultado[0]}")
#print(f"Resta: {resultado[1]}")
#print(f"Multiplicación: {resultado[2]}")
#print(f"División: {resultado[3]}")

#8)Octavo ejercicio

#def calcular_imc(peso,altura):
#    return peso/(altura * altura)

#peso = float(input("Ingresa tu peso en kilogramos: "))
#altura = float(input("Ingresa tu altura en metros: "))

#imc = calcular_imc(peso,altura)
#print(f"Indice de masa corporal (IMC): {imc}")

#9)Noveno ejercicio

#def celsius_a_fahrenheit(celsius):
#    return (celsius * 9/5) + 32

#celsius = int(input("Ingresa una temperatura en grados celsius: "))

#resultado = celsius_a_fahrenheit(celsius)
#print(resultado)

#10)Decimo ejercicio

#def calcular_promedio(a,b,c):
#    return (a + b + c)/3

#a = int(input("Ingresa la primer nota: "))
#b = int(input("Ingresa la segunda nota: "))
#c = int(input("Ingresa la tercer nota: "))

#promedio = calcular_promedio(a,b,c)
#print(f"Promedio: {promedio}")