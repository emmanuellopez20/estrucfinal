def mergeSort(arr):
    iterations = 0  # Contador de iteraciones
    comparisons = 0  # Contador de comparaciones
    swaps = 0  # Contador de movimientos

    if len(arr) > 1:
        mid = len(arr) // 2
        izquierda = arr[:mid]
        derecha = arr[mid:]

        # Llamadas recursivas para ordenar las sublistas
        mergeSort(izquierda)
        mergeSort(derecha)

        i = j = k = 0

        # Mezcla las sublistas ordenadas
        while i < len(izquierda) and j < len(derecha):
            iterations += 1
            if izquierda[i] <= derecha[j]:
                arr[k] = izquierda[i]
                i += 1
                comparisons +=1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1
            comparisons +=1
            swaps += 1
            
        # Copia los elementos restantes de L (si los hay)
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1
            swaps += 1

            
        # Copia los elementos restantes de R (si los hay)
        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1
            swaps += 1

            
    return iterations, comparisons, swaps

# Solicita al usuario la cantidad de caracteres en el arreglo
num = int(input("Ingrese la cantidad de caracteres en el arreglo:\t"))
arr = []

# Solicita al usuario ingresar los caracteres y los agrega al arreglo
for _ in range(num):
    caracteres = int(input("Ingresa los caracteres:\t"))
    arr.append(caracteres)

# Ejecuta el algoritmo de Merge Sort y obtiene los resultados
iterations, comparisons, swaps = mergeSort(arr)

# Muestra el arreglo ordenado
print("\nArreglo ordenado:", arr)

# Muestra el número de iteraciones, comparaciones y movimientos realizados
print("\nNúmero de iteraciones:", iterations)
print("Número de comparaciones:", comparisons)
print("Número de movimientos:", swaps)