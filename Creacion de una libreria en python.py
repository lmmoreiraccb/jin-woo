def velocidad():
    distancia = int(input("Ingrese la distancia en metros: "))
    tiempo = int(input("Ingrese el tiempo en segundos "))
    velocidad = distancia/tiempo
    print(f"La velocidad es de: {velocidad} ")

velocidad()

def distancia():
    velocidad = int(input("Ingrese la velocidad en m/s: "))
    tiempo = int(input("Ingrese el tiempo en segundos "))
    distancia = velocidad*tiempo
    print(f"La distancia es de: {distancia} ")

distancia()

def tiempo():
    distancia = int(input("Ingrese la distancia en metros: "))
    velocidad = int(input("Ingrese la velocidad en m/s "))
    tiempo = distancia/velocidad
    print(f"El tiempo es de: {tiempo} ")

tiempo()

def vol_cubo():
    lado = int(input("Ingrese el largo de uno de los lados del cubo: "))
    volumen = lado*lado*lado
    print(f"El volumen es de: {volumen} ")

vol_cubo()

def fuerza():
   masa = int(input("Ingresa la masa "))
   aceleracion = int(input("Ingresa la aceleracion en m/s "))
   fuerza = masa*aceleracion
   print(f"La fuerza es: {fuerza} ")

fuerza()

#ejemplos

def velocidad1(distancia, tiempo):
    result = distancia/tiempo
    print("la velocidad seria de: "), str(result)

int_velocidad=float(input("ingrese la distancia: "))
int_tiempo=float(input("Ingrese el tiempo: "))
found_vel(int_velocidad, int_tiempo)
#esto va en el menu

    
