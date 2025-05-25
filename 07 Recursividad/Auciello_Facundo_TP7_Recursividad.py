#Ejercicio 1

#def factorialNumero (num):
#    if num == 0:
#        return 1
#    else:
#        return num * factorialNumero(num - 1)

#tengo que ingresar un numero y imprimir los factoriales hasta ese num
#usuario = int(input("Ingresa un numero: "))

#for i in range (1,usuario + 1):
#    print(f"Factorial de {i}: {factorialNumero(i)}")

#Ejercicio 2

#def fibonacci(pos):
#    if pos == 0:
#        return 0
#    elif pos == 1:
#        return 1
#    else:
#        return fibonacci(pos - 1) + fibonacci (pos - 2)
    
#numero = int(input("Ingresa un numero: "))

#for i in range (numero + 1):
#    print(f"Fibonacci({i}) = {fibonacci(i)}")

#Ejercicio 3

#def potencia(base, exponente):
#    if exponente == 0:
#        return 1
#    else:
#        return base * potencia(base, exponente - 1)
    
#b = int(input("Ingresa el numero base: "))
#e = int(input("Ingresa el numero exponente: "))

#print (f"{b} elevado a la {e} = {potencia(b, e)}")

#Ejercicio 4

#def decimalAbinario(n):
#    if n == 0:
#        return ""
#    else:
#        return decimalAbinario(n // 2) + str(n % 2)
    
#numero = int(input("Ingresa un numero decimal: "))

#if numero == 0:
#    print("0")
#else:
#    print(f"Binario = {decimalAbinario(numero)}")

#Ejercicio 5

#def esPalindromo(palabra):
#    if len(palabra) <= 1:
#        return True
#    elif palabra[0] != palabra[-1]:
#        return False
#    else:
#        return esPalindromo(palabra[1:-1])

#ingresoPalabra = input("Ingresa una palabra sin espacios ni tildes: ")
#print(esPalindromo(ingresoPalabra))

#Ejercicio 6

#def sumaDigitos(n):
#    if n < 10:
#        return n
#    else:
#        return(n % 10) + sumaDigitos(n // 10)
    
#numero = int(input("Ingresa un numero: "))
#print(f"Suma de digitos: {sumaDigitos(numero)}")

#Ejercicio 7

#def contarBloques(numero):
#    if numero == 1:
#        return 1
#    else:
#        return numero + contarBloques(numero - 1)

#bloques = int(input("Bloques en el nivel de abajo: "))
#print(f"Total de bloques necesarios: {contarBloques(bloques)}")

#Ejercicio 8

#def contarDigito(numero, digito):
#    if numero == 0:
#        return 0
#    elif numero % 10 == digito:
#        return 1 + contarDigito(numero // 10, digito)
#    else:
#        return contarDigito(numero // 10, digito)
    
#num = int(input("Ingresa un numero: "))
#dig = int(input("Ingresa un digito entre 0 y 9: "))
#print(f"El digito {dig} aparece {contarDigito(num, dig)} veces")