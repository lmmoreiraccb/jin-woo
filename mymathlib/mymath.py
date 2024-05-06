def velocidad(distancia, tiempo):
    result = distancia/tiempo
    print("La velocidad seria de: ", str(result))

def distancia(velocidad, tiempo):
    result = velocidad*tiempo
    print("La distancia es de: ", str(result))

def tiempo(distancia, velocidad):
    result = distancia/velocidad
    print("El tiempo es de: ", str(result))

def vol_cubo(lado):
    result = lado*lado*lado
    print("El volumens en de: ", str(result))

def fuerza(masa, aceleracion):
    result = masa*aceleracion
    print("La fuerza es: ", str(result))

def area(lado1, lado2):
    result = lado1*lado2
    print("El area es de: ", str(result))

def trabajo(fuerza, desplazamiento):
    result = fuerza*desplazamiento
    print("La fuerza es de: ", str(result))

def velf(velin, aceleracion, tiempo):
    result = velin+aceleracion*tiempo
    print("La velocidad final es de: ", str(result))

def velin(velf, aceleracion, tiempo):
    result = velf-aceleracion*tiempo
    print("La velocidad inicial es de: ", str(result))

def aceleracion(velf, velin, tiempo):
    result = (velf-velin)/tiempo

