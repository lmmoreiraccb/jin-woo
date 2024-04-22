lista = []
def iniciolista():
    for _ in range(50):
        item = input("Ingrese un dato")
        if item =="fin":
            print("Se cierra la lista")
            break
        else:
            lista.append(item)

iniciolista()

def agregar():
    item=input("Agregue un item")
    lista.append(item)

def remover():
    item=input("Que item quiere remover?")
    lista.remove(item)

while True:
    print("Seleccione una opcion")
    print("1. Agregar un item")
    print("2. remover un item")
    print("3. salir")
    opcion = input("Ingre un numero para seleccionar la opcion")

    if opcion == "1":
        agregar()
    elif opcion == "2":
        remover()
    elif opcion == "3":
        print("Se finaliza el programa")
        break
    
    else:
            print("Opcion no valida, seleccione una opcion valida")
print(lista)
