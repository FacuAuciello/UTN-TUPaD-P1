#1) Ejercicio 1.

#print ("Hola mundo!")

#2) Ejercicio 2.

#nombre = input ("Ingresa tu nombre")
#print (f"Hola{nombre}!")

#3) Ejercicio 3

#nombre = input ("Ingresa tu nombre")
#apellido = input ("Ingresa tu apellido")
#edad = input ("Ingresa tu edad")
#residencia = input ("Ingresa tu lugar de residencia")

#print (f"Soy{nombre}{apellido}, tengo{edad} años y vivo en{residencia}!")

#4) Ejercicio 4

#radio = float (input ("Ingresa el radio de tu circulo"))

#area = 3.14 * radio ** 2
#perimetro = 2 * 3.14 * radio

#print (f"Area ={area} y Perimetro = {perimetro}")

#5) Ejercicio 5

#segundos = int (input ("Ingresa segundos"))

#horas = segundos / 3600

#print (f"Los segundos ingresados equivalan a: {horas} horas")

#6) Ejercicio 6.

#numero = int (input ("Ingresa un numero"))

#uno = numero * 1
#dos = numero * 2
#tres = numero * 3
#cuatro = numero * 4
#cinco = numero * 5
#seis= numero * 6
#siete = numero * 7
#ocho = numero * 8
#nueve = numero * 9
#diez = numero * 10

#print (f"{numero} X 1 = {uno}")
#print (f"{numero} X 2 = {dos}")
#print (f"{numero} X 3 = {tres}")
#print (f"{numero} X 4 = {cuatro}")
#print (f"{numero} X 5 = {cinco}")
#print (f"{numero} X 6 = {seis}")
#print (f"{numero} X 7 = {siete}")
#print (f"{numero} X 8 = {ocho}")
#print (f"{numero} X 9 = {nueve}")
#print (f"{numero} X 10 = {diez}")

#7) Ejercicio 7

#numero_uno = int (input("Ingresa el primer numero"))
#numero_dos = int (input("Ingresa el segundo numero"))

#suma = numero_uno + numero_dos
#division = numero_uno / numero_dos
#multiplicacion = numero_uno * numero_dos
#resta = numero_uno - numero_dos

#print (f"Suma = {suma} Division = {division} Multiplicacion = {multiplicacion} Resta = {resta}")

#8) Ejercicio 8

#altura = float (input("Ingresa tu altura"))
#peso = int (input("Ingresa tu peso"))

#imc = peso / altura **2

#print (f"Tu IMC (Indice de masa corporal) es de: {imc}")

#9) Ejercicio 9

#celsius = int (input("Ingresa una temperatura en grados celsius"))

#conversion = (celsius * 9/5) + 32 

#print (f"Su equivalente en grados Fahrenheit es de: {conversion}")

#10) Ejercicio 10

#numero_uno = int (input("Ingresa el primer numero"))
#numero_dos = int (input("Ingresa el segundo numero"))
#numero_tres = int (input("Ingresa el tercer numero"))

#promedio = (numero_uno + numero_dos + numero_tres) /3

#print (f"Promedio = {promedio} ")


a = 1
b = 2
c = 4

A = False
B = False
C = True

r1= (2*b-1) / (2*a) > 3
r2= a * (b*c) >= 30 and not ((a+b) * c >= (350 * c))
r3= A and r1 or B == r2
r4= A and B and r3 and C != r1

print (f"{r2}, {r3}, {r1}, {r4}")








