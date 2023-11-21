from collections import deque

dr = [1, -1, 0, 0]  # Desplazamiento en filas
dc = [0, 0, -1, 1]  # Desplazamiento en columnas
movimientos = ['D', 'U', 'L', 'R']  # Movimientos en el orden de dr y dc

n, m = map(int, input().split())
mapa = [list(input().strip()) for _ in range(n)]

# Busqueda en anchura (BFS)
visited = []  # nodos visitados
queue = []  # cola de nodos a visitar

def bfs(mapa, inicio, final):
    visited.append(inicio)
    queue.append((inicio, ''))
    while queue:
        nodo, camino = queue.pop(0)
        if nodo == final:
            return True, len(camino), camino
        for i in range(4):
            r = nodo[0] + dr[i]
            c = nodo[1] + dc[i]
            if 0 <= r < n and 0 <= c < m and mapa[r][c] != '#' and (r, c) not in visited:
                visited.append((r, c))
                queue.append(((r, c), camino + movimientos[i]))
    return False, 0, ''

for i in range(n):
    for j in range(m):
        if mapa[i][j] == 'A':
            inicio = (i, j)
        elif mapa[i][j] == 'B':
            final = (i, j)

encontrado, num_movimientos, ruta = bfs(mapa, inicio, final)

if encontrado:
    print("SÍ")
    print(num_movimientos)
    print(ruta)
else:
    print("NO")
