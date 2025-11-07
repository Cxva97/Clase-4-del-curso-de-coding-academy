"""
Saludo Personalizado: Pide al usuario su nombre. Si el nombre comienza con la letra 'A' (en mayúscula o minúscula)
imprime un saludo especial, por ejemplo: "¡Hola {Nombre}, tienes un nombre genial!".
Si no, simplemente saluda con "Hola {Nombre}". Pista: Usa lower() y la indexación [0].
"""
nombre = input("ingrese su nombre: ")
if nombre.lower()[0] == 'a' or nombre.upper()[0] == 'A' :
    print("Hola " + nombre.capitalize() + " tienes un nombre genial!!")
else:
    print("Hola "+ nombre.capitalize())

"""
Contraseña Segura: Pide al usuario que ingrese una contraseña.
Si la contraseña tiene una longitud menor a 8 caracteres, imprime "Contraseña débil".
Si tiene 8 o más, imprime "Contraseña aceptada".
"""

password = input("ingrese una clave:")
if len(password) < 8:
    print("clave debil")
else:
    print("clave aceptada ")

"""Clasificador de Frutas: Pide al usuario el nombre de una fruta.
Si la fruta es "manzana", imprime "Es una fruta de otoño ".
Si la fruta es "plátano" o "banana", imprime "Fuente de potasio ".
Para cualquier otra, imprime "Fruta exótica o desconocida ". (Ignora mayúsculas/minúsculas).
"""
fruta =input("ingresa el nombre de la fruta: ")
if fruta == "manzana" :
    print ( fruta + " es una fruta de otoño")
elif fruta == "banana" or fruta == "platano" :
    print( fruta + " es una fuente de potasio")
else:
    print(fruta + " es una fruta exotica o desconocida")
"""
Aprobación de Crédito: Pide al usuario su ingreso anual (como número entero) y su historial
crediticio ("bueno", "regular", "malo", como cadena de texto).
El crédito es APROBADO si:
El ingreso es mayor o igual a 5000 Y el historial es "bueno".
En cualquier otro caso, el crédito es RECHAZADO.
Asegúrate de limpiar el historial crediticio con strip() y lower().
"""
ingreso = int(input("ingrese su salario anual: "))
historial = input("ingrese su historial crediticio: ").strip().lower()
if ingreso >=5000 and historial == "bueno":
    print("credito APROBADO")
else:
    print("credito RECHAZADO")   

"""
Verificador de Archivo: Pide al usuario el nombre de un archivo. Imprime:
Si el nombre del archivo termina con .py, imprime "Es un archivo Python".
Si contiene la palabra "reporte" (en cualquier parte), imprime "Es un documento importante".
Si no cumple ninguna de las anteriores, imprime "Archivo estándar".
"""

nombreDeArchivo = input("ingrese el nombre del archivo: ")
if nombreDeArchivo.endswith(".py") :
    print("es un archivo de python")
elif "reporte" in nombreDeArchivo :
    print("es documento de reporte importante")
else:
    print("archivo estandar")

"""Formateador de Título y URL:
Pide al usuario que ingrese un título (ej: "Mi Primer post") y una URL base (ej: "www.blog.com/&quot;).
El programa debe generar un slug (parte de la URL) limpio a partir del título, siguiendo estas reglas:
Convertir el título a minúsculas.
Reemplazar todos los espacios por un guion (-).
Eliminar el carácter punto (.).
Finalmente, imprime la URL completa, por ejemplo: www.blog.blog.com/mi-primer-post.
"""

titulo = input("ingrese el titulo:")
url = input("ingresa una url: ")
slug = titulo.lower().replace(" ", "-") .replace (".","")
urlcompleta = url.strip() + "/" + slug
print("la url completa es: " + urlcompleta)