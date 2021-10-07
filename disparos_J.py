def disparos_jugador():
    bandera = True
    while bandera:
        x=int(input("Coordenada X"))
        y=int(input("Coordenada Y"))
    
        if Tablero_maquina[x][y] == "B":
            Tablero_agua_J[x][y] = "X"
            Tablero_maquina[x][y] = "X"
            print("Tablero_agua_Jugador")
            print(Tablero_agua_J)
            print("-------------------------------------------")
            #print("Tablero_maquina")
            #print(Tablero_maquina)
        elif Tablero_maquina[x][y] == "X" or Tablero_maquina[x][y] == "A":
            print("Esta coordenada ya está usada, pierdes turno")
            bandera = False
        else: 
            Tablero_agua_J[x][y] = "A"
            print("Tablero_agua_Jugador") 
            print(Tablero_agua_J)
            bandera = False