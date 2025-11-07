nombre = input("ingrese su nombre: ")
if nombre.lower()[0] == 'a' or nombre.upper()[0] == 'A' :
    print("Hola " + nombre.capitalize() + " tienes un nombre genial!!")
else:
    print("Hola "+ nombre.capitalize())

