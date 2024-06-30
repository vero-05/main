import time

def mostrar_mapa(mapa):
    print("Mapa \n")
    for fila in mapa:
        for celda in fila:
            print("|" + celda + "|", end="")
        print("\n")

mapa = [[' ' for _ in range(4)] for _ in range(4)]

# Información
x_explorador, y_explorador = 0, 0
c_explorador = 'E'
x_tesoro, y_tesoro = 3, 3
t_tesoro = 'T'

# Posicionar al explorador y al tesoro
mapa[x_explorador][y_explorador] = c_explorador
mapa[x_tesoro][y_tesoro] = t_tesoro

movimientos = [0, 0, 0, 2, 2, 2]
index_mov = 0

while (x_explorador != x_tesoro) or (y_explorador != y_tesoro):
    mostrar_mapa(mapa)

    mov = movimientos[index_mov]

    mapa[x_explorador][y_explorador] = ' '

    if mov == 0:
        x_explorador += 1
    elif mov == 1:
        x_explorador -= 1
    elif mov == 2:
        y_explorador += 1
    elif mov == 3:
        y_explorador -= 1

    mapa[x_explorador][y_explorador] = c_explorador
    index_mov += 1

    time.sleep(2)

print("Se ha conseguido el tesoro")
mostrar_mapa(mapa)
