dpi=input("ingresa tu dpi")
cantidad = len(dpi)
if cantidad<13:
    print("dpi no valido")
elif cantidad==13:
    print("dpi valido")
    print("por quien quieres votar?")
    voto1=input("Votar por precidente rojo (A) azul (B)")
    voto2=input("Votar por alcalde rojo (C) azul (D) verde (E) naranja (F)")
    if voto1 =="A":
        print("votaste para presidente rojo (A)")
    elif voto1=="B":
        print("votaste para presidente azul (B)")
    else:
        print("voto invalido hacia presidente")
    if voto2=="C":
        print("votaste para alcalde rojo (C)")
    elif voto2=="D":
        print("votaste para alcalde azul (D)")
    elif voto2=="E":
        print("votaste para alcalde verde (E)")
    elif voto2=="F":
        print("votaste para alcalde naranja (F)")
    else:
        print("voto ivalido hacia alcalde")
    confirmacion=input("desea guardar sus votos? (si)(no)")
    if confirmacion =="si":
        print("votos guardados")
    elif confirmacion =="no":
        print("votos eliminados vuelve a votar")
    


   