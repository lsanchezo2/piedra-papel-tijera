import random

tijera = '''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

papel = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)   
'''

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

decision_jugador = int(input("seleccione su opción=> 0 (tijeras), 1(piedra), 2(papel): "))
decision_computadora = random.randint(0,2)

opciones_de_juego = [tijera, piedra, papel]

eleccion_jugador = opciones_de_juego[decision_jugador]
eleccion_computadora = opciones_de_juego[decision_computadora]

print(f"Tú elegiste: \n{eleccion_jugador}")
print(f"La computadora eligió: \n{eleccion_computadora}")

if decision_jugador == 0:
    if decision_computadora == 1:
        print("Perdiste")
    elif decision_computadora == 2:
        print("Ganaste")
    else:
        print("Hay empate")
elif decision_jugador == 1:
    if decision_computadora == 0:
        print("Ganaste")
    elif decision_computadora == 2:
        print("Perdiste")
    else:
        print("Hay empate")
else:
    if decision_computadora == 0:
        print("Perdiste")
    if decision_computadora == 1:
        print("Ganaste")
    else:
        print("Hay empate")




