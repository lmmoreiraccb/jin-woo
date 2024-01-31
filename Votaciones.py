dpi=input("ingresa tu dpi")
kcantidad = len(dpi)
if cantidad==13:
    print("dpi valido")
    print("por quien quieres votar?")
    voto1=input("Votar por precidente rojo (A) azul (B)")
    voto2=input("Votar por alcalde rojo (C) azul (D) verde (E) naranja (F)")
    if voto1 =="A":
        print("votaste para presidente rojo (A)")
    elif voto1=="B":
        print("votaste para presidente azul (B)")
    if voto2=="C":
        print("votaste para alcalde rojo (C)")
    elif voto2=="D":
        print("votaste para alcalde azul (D)")
    elif voto2=="E":
        print("votaste para alcalde verde (E)")
    elif voto2=="F":
        print("votaste para alcalde naranja (F)")


borrar la k de kcantidad de la linea 3