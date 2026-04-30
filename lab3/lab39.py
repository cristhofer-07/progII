# Usando format(), format_map() y encode()
texto = "Hola {}"
print(texto.format("Mundo"))
datos = {"nombre": "Juan"}
print("Mi nombre es {nombre}".format_map(datos))
print("Python".encode())