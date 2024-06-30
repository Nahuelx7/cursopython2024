#Longitud de string
# Funcion LEN

esto_es_un_string = "Hola soy un string"
print(len(esto_es_un_string))


string1= "    "
print(len(string1))


#Rebanar un string
# Funcion SLICING [inicio:fin:paso]
#Incio va a ser el indice del primer caracter de la cadena que queremos seleccionar (rebanar o slicing)
#Fin va a ser el indice del ultimo caracter no incluido de la cadena que queremos seleccionar (rebanar o slicing)
#Paso: indica cada cuanto caracteres seleccionamos entre las posiciones de inicio y fin

saludo = "hola, como estan?"
print(len(saludo))
saludo[0:3:1]
print(saludo[0:3:1])

print(saludo[0:17:2])


palabra = "Pithon"
print(palabra)

print(palabra[1])

#Como hacer para reemplazar una letra en un string (Conocido como slicing(rabanar))
palabra = palabra[0:1] + "y" + palabra[2:]
print(palabra)

### LISTA Y TUPLAS

mi_lista = [-11,20,3,41]
print(mi_lista)

otra_lista = ["hola", "Como", "Estas", "?"]

variable_1 = "Una variable"

listita = [1, -10, 132.5, "Un string", "Otro string", variable_1]

print(listita)


print(listita[0])
print(listita[-1])

print(listita[-2:1])



numeros = [1,2,3,4,5,6]
print(numeros+[7,8,9,10])

numeros = [99999,2,4,5,10,15,20]


















#FUNCION APPEND
#Nos permite agregar un nuevo item al final de una lista
numeros = [1,2,3,4,5,6]
numeros.append(7)
print(numeros)

#Tambien podemos utilizar la funcion LEN aca
print(len(numeros))


print(numeros)


#FUNCION POP
#La funcion POP es todo lo contario a append, porque va a eliminar el ultimo item de una lista. -pop.()

equipos = ["Moron", "River", "Boca", "Independiente"]
equipos.pop()
print(equipos)
########Si ingreso dentro del parentesis una posicion segun indice, POP eliminara el indice correspondiente
equipos = [1,2,3,4]
equipos.pop(2)
print(equipos)

# FUNCION COUNT
# La funcion COUNT cuenta el numero de veces que nuestro item se repite en una lista. -  SE ESCRIBE la_lista_a_contar.count()(el item a contar)
numeros_varios = [1,2,3,4,4,4,5]
#En este caso el item 4 se repite 3 veces
print(numeros_varios.count(4))

#INDEX
#Busca el item y nos devuelve en que indice está. - SE ESCRIBE la_lista.index()(lo que queremos buscar)

numeros_varios = [1,2,3,4,4,4,5]
numeros_varios.index(3)
print(numeros_varios.index(3))

##___________ TUPLAS
#Las tuplas son similares a las listas, La GRAN diferencia es que las tuplas son INMUTABLES
# Se declaran con parentesis - mi_tupla(1,2,3,4)

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

otra_tupla = (1,5,-100, "Cadena", "Otra cadena/string", mi_tupla)
print(otra_tupla)

otra_tupla[0] = 5000
#la funcion de arriba no funciona porque la tupla no se puede modificar