#CLASE 25/6: TENIENDO DOS LISTA LA CUAL LLAMAREMOS lista_1 y lista_2 hay que hacer los siguientes ejercicios

#Añadir a la lista_1 el entero 4567 y despues el string "UNAHUR"

#Añadir a la lista_2 el string "EDUCACION" y despues el entero 789

#Crear una lista_3 con todos los elementos de la lista_1 MENOS el último

#Crear una lista_4 con todos los elementos de la lista_2 MENOS el primero y último

#Crear una lista_5 con todos los elementos de la lista_3 y de la lista_4


#                              AHORA CON TUPLAS
#Crear una variable llamada tupla con más de 15 items y printear lo siguiente:

# El ultimo item de la tupla creada, el numero de items de la misma, la posicion donde se encuentra algun item que haya dentro, una lista con los ultimos cuatro items de la tupla, un item que haya en la posicion 8, el numero de veces que se repite algún item dentro de la misma.

#############################################################################################################################



lista_1 = []
lista_2 = []

lista_1.append(4567)
lista_1.append("UNAHUR")

print(lista_1)

lista_2.append("EDUCACION")
lista_2.append(789)

print(lista_2)

lista_3 = (lista_1[:-1])

print(lista_3)


lista_4 = (lista_2[1:-1])

print(lista_4)

lista_5 = (lista_3+lista_4)

print(lista_5)

#########################################################################################################################

tupla = (1,2,3,4,5,6,7,"UNAHUR","UNAHUR",10,11,12,12,12,15)

# El ultimo item de la tupla creada
print(tupla[-1])
# El numero de items de la misma
print(len(tupla))
# La posicion donde se encuentra algun item que haya dentro
print(tupla[3])
# Una lista con los ultimos cuatro items de la tupla
print(tupla[-4:])
# Un item que haya en la posicion 8
print(tupla[8])
# El numero de veces que se repite algún item dentro de la misma
print(tupla.count("UNAHUR"))
print(tupla.count(12))
