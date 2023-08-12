import random

jugador1 = 0
jugador2 = 0
opciones = ["Piedra", "Papel", "Tijera"]  # 0, 1, 2
def maquina():
  maquina = random.choice(opciones) # selecciona un elemento aleatiorio de opciones
  return opciones.index(maquina) + 1  # obtiene el indice del elemento de la lista sumando 1 para obtener un numero entero (recordar que las listas comienzan con 0)

def volver_a_jugar():
  print()
  print("¿Volver a jugar?:\n")
  repetir = input("1.- Si  2.- No\n")
  if repetir == "1":
    limpiar_marcador()
    iniciar()
  else:
    return

def limpiar_marcador():
  global jugador1
  global jugador2
  jugador1 = 0
  jugador2 = 0

def contador():
  print("+--"*10 + "+")
  print("Jugador 1: " + str(jugador1) + "\r" + "     " + "Jugador 2: " + str(jugador2))
  print("+--"*10 + "+\n")

def iniciar():
  global jugador1, jugador2
  while jugador1 < 3 and jugador2 < 3:
    contador()
    print("Tu turno:\n")
    seleccion = int(input("1.- Piedra  2.- Papel  3.- Tijera\n"))
    print()
    eleccion_maquina = maquina()
    if seleccion < eleccion_maquina:
      print("+--"*5 + "+")
      print("Perdiste")
      print("+--"*5 + "+\n")
      jugador2 += 1
    elif seleccion == eleccion_maquina:
      print("+--"*5 + "+")
      print("Empate")
      print("+--"*5 + "+\n")
    elif seleccion > eleccion_maquina:
      print("+--"*5 + "+")
      print("Ganaste")
      print("+--"*5 + "+\n")
      jugador1 += 1
    elif seleccion == "0":
      print("+--"*5 + "+")
      print("ERROR\n")
      print("+--"*5 + "+\n")
    else:
      return
  if jugador1 == 3:
    print("¡GANASTE!\n")
    volver_a_jugar()
  else:
    print("¡PERDISTE!\n")
    volver_a_jugar()

iniciar()