def insertion_sort(lista):
    comparaciones = 0
    movimientos = 0
    consultas = 0
    iteraciones = 0
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while j >= 0 and temp < lista[j]:
            comparaciones += 1
            consultas += 1  # Contar la consulta realizada
            lista[j + 1] = lista[j]
            j -= 1
            movimientos += 1
            iteraciones += 1
        lista[j + 1] = temp
        movimientos += 1
        consultas += 1  # Contar la consulta realizada al asignar temp
        iteraciones += 1
    return comparaciones, movimientos, consultas, iteraciones

def bucket_sort(num_buckets=5):
    minimo = min(arreglo)
    maximo = max(arreglo)
    rango = maximo - minimo + 1

    tamaño_buckets = rango // num_buckets
    buckets = [[] for _ in range(num_buckets)]

    consultas_buckets = 0
    comparaciones_buckets = 0
    movimientos_buckets = 0
    iteraciones_buckets = 0

    for num in arreglo:
        consultas_buckets += 1
        if num < 0:
            indice = 0
        else:
            indice = min((num - minimo) // tamaño_buckets, num_buckets - 1)
        buckets[indice].append(num)

    print("Buckets desordenados:")
    for i, bucket in enumerate(buckets):
        print(f"Bucket {i}: {bucket}")

    for i in range(num_buckets):
        comparaciones_i, movimientos_i, consultas_i, iteraciones_i = insertion_sort(buckets[i])
        comparaciones_buckets += comparaciones_i
        movimientos_buckets += movimientos_i
        consultas_buckets += consultas_i
        iteraciones_buckets += iteraciones_i

    print("\nBuckets ordenados:")
    for i, bucket in enumerate(buckets):
        print(f"Bucket {i}: {bucket}")

    # Concatenando buckets ordenados
    arreglo_ordenado = []
    for bucket in buckets:
        arreglo_ordenado.extend(bucket)

    return arreglo_ordenado, consultas_buckets, comparaciones_buckets, movimientos_buckets, iteraciones_buckets

# Ejemplo:
arreglo = [29, -13, 22, -37, 52, 49, -46, 71, -56, 34]
comparaciones_insertion, movimientos_insertion, consultas_insertion, iteraciones_insertion = insertion_sort(arreglo)

# Insertion Sort en Buckets
print("\nComparaciones realizadas (Insertion Sort en Buckets):", comparaciones_insertion)
print("Movimientos realizados (Insertion Sort en Buckets):", movimientos_insertion)
print("Consultas realizadas (Insertion Sort en Buckets):", consultas_insertion)
print("Iteraciones realizadas (Insertion Sort en Buckets):", iteraciones_insertion)
