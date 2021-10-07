def disparos_maquina():
    bandera = True
    while bandera:
        x = np.random.randint(10)
        y = np.random.randint(10)
    
        if Tablero_jugador[x][y] == "B":
            Tablero_agua_M[x][y] = "X"
            Tablero_jugador[x][y] = "X"
            print("Tablero_agua_Máquina")
            print(Tablero_agua_M)
            print("-------------------------------------------")
            print("Tablero_jugador")
            print(Tablero_jugador)
        elif Tablero_jugador[x][y] == "X" or Tablero_jugador[x][y] == "A":
            print("Esta coordenada ya está usada, pierdes turno")
            bandera = False
        else: 
            Tablero_agua_M[x][y] = "A"
            print("Tablero_agua_Máquina") 
            print(Tablero_agua_M)
            bandera = False