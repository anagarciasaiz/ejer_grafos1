#Te dan un mapa de un edificio y tu tarea es contar el número de sus habitaciones. El
#tamaño del mapa es 𝑛 × 𝑚 cuadrados, y cada cuadrado es suelo o pared. Puedes caminar
#hacia la izquierda, derecha, arriba y abajo a través de los cuadrados del suelo.
#La primera línea de entrada tiene dos números enteros 𝑛 y 𝑚: la altura y el ancho del mapa.
#Le siguen 𝑛 líneas de 𝑚 caracteres que describen el mapa. Cada carácter es .(suelo) o #(pared)

n,m = map(int,input().split())
mapa = [input() for _ in range(n)]

seen = [[False]*m for _ in range(n)]

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m or seen[x][y] or mapa[x][y] == '#':
        return
    seen[x][y] = True
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

habitaciones = 0
for i in range(n):
    for j in range(m):
        if not seen[i][j] and mapa[i][j] == '.':
            dfs(i,j)
            habitaciones += 1
print(habitaciones)


