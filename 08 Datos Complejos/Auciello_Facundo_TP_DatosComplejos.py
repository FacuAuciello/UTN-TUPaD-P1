#Ejercicio 1

#precios_frutas = {
#    'Banana': 1200,
#    'Anana': 2500,
#    'Melon': 3000,
#    'Uva': 1450
#}

#precios_frutas['Naranja'] = 1200
#precios_frutas['Manzana'] = 1500
#precios_frutas['Pera'] = 2300

#Ejercicio 2

#precios_frutas['Banana'] = 1330
#precios_frutas['Manzana'] = 1700
#precios_frutas['Melon'] = 2800

#Ejercicio 3

#listaFrutas = list(precios_frutas.keys())

#print("Frutas disponibles: ", listaFrutas)

#Ejercicio 4
#agenda = {}

#for i in range(5):
#    nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
#    numero = input(f"Ingresa el numero de {nombre}: ")
#    agenda[nombre] = numero

#consulta = input("Ingresa el nombre del contacto: ")

#if consulta in agenda:
#    print(f"El numero de {consulta} es: {agenda[consulta]}")
#else:
#    print("El contacto no esta en la agenda")

#Ejercicio 5
#frase = input("Ingresa una frase: ")
#palabras = frase.lower().split()

#palabras_unicas = set(palabras)
#print("Palabras unicas:", palabras_unicas)

#frecuencia = {}
#for palabra in palabras:
#    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

#print("Frecuencia de palabras:", frecuencia)

#Ejercicio 6
#alumnos = {}

#for i in range(3):
#    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
#    notas = []
#    for j in range(3):
#        nota = float(input(f"Ingresa la nota {j+1} de {nombre}: "))
#        notas.append(nota)
#    alumnos[nombre] = notas

#for nombre, notas in alumnos.items():
#    promedio = sum(notas) / len(notas)
#    print(f"{nombre}: promedio = {promedio:.2f}")

#Ejercicio 7
#parcial1 = {"Ana", "Florencia", "Carlos", "Felipe"}
#parcial2 = {"Luis", "Felipe", "Pedro", "Lucia"}

#ambos = parcial1 and parcial2
#soloUno = parcial1 ^ parcial2
#alMenosUno = parcial1 | parcial2

#print("Aprobaron ambos:", ambos)
#print("Aprobaron solo uno:", soloUno)
#print("Aprobaron al menos uno:", alMenosUno)

#Ejercicio 8
#stock = {
#    "leche": 10,
#    "pan": 20,
#    "huevos": 30
#}

#producto = input("Ingresa el nombre del producto: ").lower()

#if producto in stock:
#    print(f"Stock actual de {producto}: {stock[producto]}")
#    agregar = int(input("Cuantas unidades queres agregar? "))
#    stock[producto] += agregar
#else:
#    nuevoStock = int(input(f"{producto} stock no disponible. Cuántas unidades queres agregar? "))
#    stock[producto] = nuevoStock

#print("Stock actualizado:", stock)

#Ejercicio 9
#agenda = {
#    ("lunes", "10:00"): "Desayuno",
#    ("martes", "14:00"): "Clase Python",
#    ("viernes", "18:00"): "Padel"
#}

#dia = input("Ingresa el dia: ").lower()
#hora = input("Ingresa la hora (ej: 10:00): ")

#actividad = agenda.get((dia, hora), "No hay actividad programada.")
#print("Actividad:", actividad)

#Ejercicio 10
#paises = {
#    "Argentina": "Buenos Aires",
#    "Brasil": "Brasilia",
#    "Francia": "Paris",
#    "Japon": "Tokio"
#}

#capitales = {capital: pais for pais, capital in paises.items()}

#print("Diccionario invertido:")
#print(capitales)




