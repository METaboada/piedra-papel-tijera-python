
nombre1 = input("Cual es el nombre del jugador 1?: ")
nombre2 = input("Cual es el nombre del jugador 2?: ")


print ("Hola", nombre1,"!")
print ("Que elijes?")
jugador1 = input("piedra, papel o tijera?: ")

print ("Hola", nombre2,"!")
print ("Que elijes?")
jugador2 = input("piedra, papel o tijera?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print ("Esto fué un empate")
elif condicion1 or condicion2 or condicion3:
    print ("Ganó", nombre1)
else:
    print ("Ganó", nombre2)



