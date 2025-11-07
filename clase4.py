#feedback condicionales taller bucles
#actividad variables estructuradas
#taller try except

"""
feedback
condicionales que unicamente es permitir que mi codigo tome decisiones
segun las condiciones que yo le ponga

1. if condicion :
    #codigo o bloque a ejecutar
2. if condicion :
    #codigo o bloque a ejecutar
   else:
3. if condicion :
    #codigo o bloque a ejecutar
   elif condicion2:
    #codigo o bloque a ejecutar
   else:
    #codigo o bloque a ejecutar

4. anidaciones
    if condicion:
        if condicion2:  
            #codigo o bloque a ejecutar
        else:
            #codigo o bloque a ejecutar
"""


#bucles es algo que se repite varias veces en base a una condicion
# WHILE es mientras #! tratar de no entrar en bucles infinitos
#menus, control de errores
# while condicion:
    # codigo o bloque a ejecutar
"""while True: #como romper el blucle CRTL + C
    print("hola")"""

# manejo de errores
clave = input("ingrese una clave de 3 caracteres: ")
while len(clave) < 3 :
    clave = input("Error, ingrese una clave de 3 caracteres: ")
print("clave aceptada") 

# menu
while True:
    print("hola, selecciona una opcion ")
    print("1. para saludar")
    print("2. para despedirte")
    opcion = input("que deseas hacer? :")

    if opcion == "1" :
        print("Hola, que tengas un buen dia")
    elif opcion == "2" :
        print("Adios, vuelve pronto")
        break

#condicional extra es el match case
operacion = int(input("ingrese una operacion (1,2,3): "))
match operacion:
    case 1:
        print("hola")
    case 2:
        print("adios")
    case 3: 
        print("este es el curso de python") 

# for 
