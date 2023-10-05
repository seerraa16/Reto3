
n, x = map(int, input().split())
pesos = list(map(int, input().split()))
# Ordenar los pesos de los niños de forma ascendente
pesos.sort()

num_gondolas = 0
i = 0
j = n - 1

while i <= j:
    if pesos[i] + pesos[j] <= x:
        i += 1
    j -= 1
    num_gondolas += 1

print(num_gondolas)
