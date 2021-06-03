import random

score = 0

print("¡Bienvenido a mi juego de Python! ¿Cómo te llamas?")
miNombre = input()

número = random.randint(1, 20) # Aquí se elige un número aleatorio del 1 al 20, se pueden cambiar valores.
print("Hola, " + miNombre + ", ¿eres capaz de adivinar el número que estoy pensando? Es muy fácil, está entre 1 y 20")

while score < 5:
    print("Escribe el número.")
    elección = input()
    elección = int(elección)

    score = score + 1

    if elección < número:
        print("Demasiado bajo, prueba un número más alto.")
    if elección > número:
        print ("Te has pasado, prueba otro más bajo.")
    if elección == número:
        break

if elección == número:
    score =  str(score)
    print("¡Bien hecho! La verdad tenía duda si podrías hacerlo. Has necesitado " + score + " intentos.")

if elección!= número:
    número = str(número)
    print ("¡Has fallado! El número que pensaba era el " + número + ".")

input("Presiona ENTER para salir")
