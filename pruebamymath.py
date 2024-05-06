import mymathlib
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
    print("11. Salir")

    opcion = input("Ingrese en numero de la opcion deseada: ")

    if opcion == "1":
        int_velocidad=float(input("ingrese la distancia: "))
        int_tiempo=float(input("Ingrese el tiempo: "))
        mymathlib.velocidad(int_velocidad, int_tiempo)
    
    elif opcion == "2":
        int_distancia=float(input("ingrese la distancia: "))
        int_tiempo=float(input("Ingrese el tiempo: "))
        mymathlib.distancia(int_distancia, int_tiempo)

    elif opcion == "3":
        int_tiempo=float(input("Ingrese la distancia: "))
        int_velocidad=float(input("Ingrese la velocidad: "))
        mymathlib.tiempo(int_tiempo, int_velocidad)

    elif opcion == "4":
        int_vol_cubo = float(input("Ingrese la medida del lado: "))
        mymathlib.vol_cubo(int_vol_cubo)
    elif opcion == "5":
        int_fuerza=float(input("Ingrese la masa: "))
        int_aceleracion=float(input("Ingrese la aceleracion: "))
        mymathlib.fuerza(int_fuerza, int_aceleracion)
    elif opcion == "6":
        int_area = float(input("Ingresa el area de un lado del cubo: "))
        mymathlib.area(int_area)
    elif opcion == "7":
        int_trabajo = float(input("Ingrese la fuerza: "))
        int_desplazamiento = float(input("Ingrese el desplazamiento: "))
        mymathlib.trabajo(int_trabajo, int_desplazamiento)
    elif opcion == "8":
        int_velf = float(input("ingrese la velocidad inicial: "))
        int_aceleracion = float(input("Ingrese la aceleracion: "))
        int_tiempo = float(input("Ingrese el tiempo: "))
        mymathlib.velf(int_velf, int_aceleracion, int_tiempo)
    elif opcion == "9":
        int_velin = float(input("Ingrese la velocidad final: "))
        int_aceleracion = float(input("Ingrese la aceleracion: "))
        int_tiempo = float(input("Ingrese el tiempo: "))
        mymathlib.velin(int_velin, int_aceleracion, int_tiempo)
    elif opcion == "10":
        int_aceleracion = float(input("Ingrese la velocidad final: "))
        int_velin = float(input("Ingrese la velocidad inicial: "))
        int_tiempo = float(input("Ingrese el tiempo: "))
        mymathlib.aceleracion(int_aceleracion, int_velin, int_tiempo)
    elif opcion == "11":
        print("!Hasta luego¡")
        break
    else:
        print("Opcion no valida. por favor, seleccione una opcion valida. ")
