#feedback condicionales taller variables estructuradas
#actividad bucles
#taller bucles try except

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
# si es mayor de edad y tiene mas de 500 de salario paga impuestos
#si es menor no paga impuestos

edad=int(input("ingrese su edad: "))
salario=int(input("ingrese su salario: "))
if edad >=18 and salario >500:
    print("Paga impuestos del 20%")
elif edad >=18 and salario <=500 :
    print("paga impuestos del 0.15%")
else:
    print("no paga impuestos")

if edad >=18 :
    if salario >500:
        print("Paga impuestos del 20%")
    else:
        print("paga impuestos del 0.15%")
else:
    print("no paga impuestos")