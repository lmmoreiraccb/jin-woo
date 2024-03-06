lista = []
for _ in range(50):
    item=input("ingrese un item a la lista")
    if item=="fin":
        print("se cierra la lista")
        break
    else:
        lista.append(item)
print("los items son:", lista)
eliminar=input("desea eliminar alguno?")
if eliminar=="si":
    while True:
        item=input("Que item desea eliminar")
        if item=="fin":
            print("se cierra la lista")
            print("los items de la lista son:", lista)
            break
        else:
            lista.remove(item)
elif eliminar=="no":
    print("los items son", lista)
        

