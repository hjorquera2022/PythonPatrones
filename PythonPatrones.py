# Dibuja un tablero de ajedrez de 8x8 con un peón

# Define el tamaño del tablero
filas = 8
columnas = 8

# Define la representación del peón
peon = "♟"

# Define la representación vacía de una casilla
casilla_vacia = "."

# Define el patrón del dibujo del peón
patron_peon = [
    [" ", " ", " ", ".", ".", "."  " ", " "],
    [" ", " ", " ", ".", ".", " ", " ", " "],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."]
]

# Dibuja el tablero con el dibujo del peón
for fila in range(filas):
    for columna in range(columnas):
        if (fila + columna) % 2 == 0:
            # Casilla blanca
            if patron_peon[fila][columna] == ".":
                print(" ", end="")
            else:
                print(peon, end="")
        else:
            # Casilla negra
            print("#", end="")
    
    print()  # Salto de línea entre filas
