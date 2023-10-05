# Leer el número de casos de prueba
t = int(input())

for _ in range(t):
    # Leer el número de alumnos y los identificadores
    n = int(input())
    identificadores = list(map(int, input().split()))

    # Algoritmo de ordenamiento de burbuja
    for i in range(n):
        for j in range(0, n-i-1):
            if identificadores[j] > identificadores[j+1]:
                identificadores[j], identificadores[j+1] = identificadores[j+1], identificadores[j]

    # Contar los identificadores únicos
    unique_count = 1
    for i in range(1, n):
        if identificadores[i] != identificadores[i-1]:
            unique_count += 1

    # Imprimir el resultado
    print(unique_count)
