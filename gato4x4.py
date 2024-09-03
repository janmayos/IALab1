
def crear_tablero():
    tablero = [[" ", " ", " "," "],
            [" "," "," "," "], 
            [" "," "," "," "],
            [" "," "," "," "]]
    print_tablero(tablero)
    return tablero

def print_tablero(tablero):
    matrix_length = len(tablero)
    for i in range(matrix_length):
        print(tablero[i])

def solicitar_coordenadas():
    while True:
        fila = int(input("Ingresa la fila:"))
        if fila >= 0 and fila <=3:
            break
        else:
            print("Favor de ingresar un valor del 0-3")

    while True:
        columna = int(input("Ingresa la columna:"))
        if columna >= 0 and columna <=3:
            break
        else:
            print("Favor de ingresar un valor del 0-3")
    
    return fila,columna

def rellenar_casilla(tablero,fila,columna,valor):
    if tablero[fila][columna] == " ":
        tablero[fila][columna]= valor
        print_tablero(tablero)
    else:
        print("Casilla ocupada volver a seleccionar coordenadas")
        fila,columna = solicitar_coordenadas()
        rellenar_casilla(tablero,fila,columna,valor)

if __name__ == "__main__": 
    tablero = crear_tablero()
    fila,columna = solicitar_coordenadas()
    print(fila,columna)
    rellenar_casilla(tablero,fila,columna,"X")
    rellenar_casilla(tablero,fila,columna,"O")