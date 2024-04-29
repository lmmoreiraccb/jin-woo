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

while True:
    print("selleccione la conversion que desea realizar: ")
    print("1. velocidad")
    print("2. distancia")
    print("3. tiempo")
    print("4. volumen del cubo")
    print("5. fuerza")
    print("6. area")
    print("7. trabajo")
    print("8. velocidad final")
    print("9. velocidad inicial")
    print("10. aceleracion")

    opcion = input("Ingrese en numero de la opcion deseada: ")

    if opcion == "1":
        int_velocidad=float(input("ingrese la distancia: "))
        int_tiempo=float(input("Ingrese el tiempo: "))
        velocidad(int_velocidad, int_tiempo)
    
    elif opcion == "2":
        int_distancia=float(input("ingrese la distancia: "))
        int_tiempo=float(input("Ingrese el tiempo: "))
        distancia(int_distancia, int_tiempo)

    elif opcion == "3":
        int_tiempo=float(input("Ingrese la distancia: "))
        int_velocidad=float(input("Ingrese la velocidad: "))
        tiempo(int_tiempo, int_velocidad)

    elif opcion == "4":
        int_vol_cubo = float(input("Ingrese la medida del lado: "))
        vol_cubo(int_vol_cubo)




