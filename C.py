
t = int(input())

for _ in range(t):
   
    n = int(input())
    horarios = [tuple(map(int, input().split())) for _ in range(n)]
    horarios.sort(key=lambda x: x[1])
    peliculas_vistas = 0
    tiempo_actual = 0
    for inicio, fin in horarios:
        if inicio >= tiempo_actual:
            peliculas_vistas += 1
            tiempo_actual = fin

    print(peliculas_vistas)
