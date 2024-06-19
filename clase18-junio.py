#Clase Martes 18/06

## Numero ENTEROS = INT o LONG (Siendo el INT el mas utilizado)
## Pueden ser Positivo, negativos o enteros
## Ejemplo de LONG "454544467744L"

## Numero FLOAT = Numero con decimales
## Ejmeplo de FLOAT 0,32
## Tambien pueden ser negativos como por ejemplo: "-33,895"

## Numeros COMPLEX = Numeros complejos
## Se utilizan almacenando numeros reales y tambien se represtan con el LONG al final
## Por ejemplo: "33,8j"

## OPERADORES ARITMETICOS
## SUMA: +
## RESTA: -
## MULTIPLICACION: *
## POTENCIA: **
## DIVISION: (Cociente) /
## DIVISION (parte entera) //
## PROMEDIO: %


## PROCEDENCIA DE LOS OPERADORES
## 1- TERMINOS ENTRE PARENTESIS
## 2- POTENCIACION Y RAICES
## 3- MULTIPLICACION Y DIVISION
## 4- SUMA Y RESTA


print (15+8)


print(10+5)


print(110+10)



#_____________________________STRING = STR (CADENA DE TEXTO)_________________
## COMILLAS DOBLES """
## COMILLAS SIMPLES ''

print("hola mundo")

print(3)

print("Un string \t con tabulacion")

print("Otro string \n salto de linea")


#_________VARIABLES________

## LAS VARIABLES EN PYTHON SON COMO ETIQUETAS QUE NOS PERMITEN HACER REFERENCIAS A LOS DATOS
## POR CADA DATO QUE APARECE EN MI PROGRAMA, PYTHON VA A CREAR UN OBJETO QUE LO CONTIENE
## CADA OBJETO VA A TENER:
#1- UN INDENTIFICADOR UNICO (id)
#2- UN TIPO DE DATO (entero, decimal, string, etc)
#3- UN VALOR (el propio dato dentro del objeto)
#LAS VARIABLES EN PYTHON NO GUARDAN LOS DATOS

dni = 38155991
print(dni)


#######EL NOMBRE DE UNA VARIABLE SIEMPRE DEBE EMPEZAR POR UNA LETRA O UN GUION BAJO(_) snake case
######## LOS NOMBRES DE LAS VARIBLES NO PUEDEN INCLUIR ESPACIOS EN BLANCO#####

mi_fecha_de_nacimiento ="03 de mayo"
print(mi_fecha_de_nacimiento)

dni = 16908886
print(dni)

dni=38155991
print(dni)

mi_variable = 1994
print(mi_variable)


#METODO DE SALIDA ES = PRINT()
#METODO DE ENTRADA ES = INPUT()

nombre = input("Hola escribi tu nombre:")
print(nombre) 


#LA FUNCION INPUT POR DEFECTO CONVIERTE LOS DATOS DE ENTRADA EN UN STRING(CADENA DE CARACTERES) AUNQUE LE ESTEMOS ESCRIBIENDO UN NUMERO

a = 20
b = 20
resultado = a+b

print(resultado) 

#LOS DATOS DE ENTRADA SE PODRIAN CONVERTIR EN STR(STRING) 

e = 30
""" f = input("Cual es tu edad?")""" #Este es un ejemplo de un dato de entrada que lo toma como cadena de texto
        
f = int(input("cual es tu edad?"))

print(e+f)
      
#A LA SUMA DE LOS STRING LO VAMOS A LLAMAR CONCATENACION

cadena_de_texto = "python"
anio_del_curso = "2024"

print(cadena_de_texto+anio_del_curso)

#LOS INDICES VIENEN: 0 (primer caracter),  1(segundo caracter), etc..
#LOS INDICES INVERSOS: -1(ultimo caracter), -2(anteultimo), etc..
# P  Y  T  H  O  N
# 0 1 2 3 4 5 INDICE 
#-6 -5 -4 -3 -2 -1  