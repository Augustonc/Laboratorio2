
# l = ["Augusto", "Carolina","David","Marita","Marcelo","Daiana","Johana","Araceli","Sofia","Ciro"]
# for i in l:
#     print(i)

# Clase Laboratorio 16-8-2022
# Video 1: Listas

nombres = ["Naty","Osvaldo","Lily","Ariel"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
print("")#Salto de linea

#Video 2: Listas

print(nombres[0:2])
#ir del inicio de la listaal indice (sin incluirlo)
print(nombres[ :3])# Indices a mostrar 0,1,2
# Desde el indice indicado hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[3] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
# Iterar una lista
print("")#Salto de linea
for nombre in nombres:
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")
print("")

# Video 3: Listas

# Preguntamos cuantos elementos tiene

print(len(nombres)) # Le pasamos como parametro la lista

# Agregamos un elemento
nombres.append("Marcelo")
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3,"Debora")
print(nombres)


# Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)

#Eliminar el últmo elemento

nombres.pop()
print(nombres)

# Eliminar un índice específico

del nombres[2]
print(nombres)

# Elinar, borrar o limpiar todos los elementos

nombres.clear()
print(nombres)

# Eliminar la lista

#del nombres # Lo comentamos para evitar el error
#print(nombres)

# Ejercicios de uso de rangos

# Ejercicio 1 rangos
print("Ejercicio 1")

# Imprimir un rango de 0 a 10 e imprimir números divisibles entre 3
# Ejemplo de solución: 0,3,6,9
for i in range(0,11,3): #(desde,hasta,con paso)
    print(i)
print("")

# Ejercicio 2 rangos
print("Ejercicio 2")

# Crear un rango de números de 2 a 6 e imprimirlos
for i in range(2,7):
    print(i)
print("")

# Ejercicio 3 rangos
print("Ejercicio 3")

# Crear un rango de 3 a 10 con un incremento de 2 en 2
for i in range(3,10,2):
    print(i)
print("")

#                                      AQUÍ HACEMOS UN COMMIT