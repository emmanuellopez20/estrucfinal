from re import A


def bubblesort(arr):
    n = len(arr)
    iteraciones_i = 0
    consultas_i = 0
    movimientos_i = 0

    for i in range(n - 1):
        iteraciones_i += 1
        for j in range(0, n - i - 1):
            consultas_i += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                movimientos_i += 1
                print(arr)
    print(f"Iteraciones: {iteraciones_i}")
    print(f"Consultas: {consultas_i}")
    print(f"Movimientos: {movimientos_i}")

    return arr


def cocktail_sort(arr):
    n = len(arr)
    iteraciones_i = 0
    consultas_i = 0
    movimientos_i = 0
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        iteraciones_i += 1
        swapped = False

        for i in range(start, end):
            consultas_i += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                movimientos_i += 1
                print(arr)

        if not swapped:
            break

        swapped = False
        iteraciones_i += 1
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                print(arr)

        start += 1

    print(f"Iteraciones: {iteraciones_i}")
    print(f"Consultas: {consultas_i}")
    print(f"Movimientos: {movimientos_i}")

    return arr


def selection_sort(arr):
    n = len(arr)
    iteraciones_i = 0
    consultas_i = 0
    movimientos_i = 0

    for i in range (n-1):
        iteraciones_i += 1
        minimo = i
        for j in range(i + 1, n):
            consultas_i += 1
            
            if arr[j] < arr[minimo]:
                minimo = j

            print(arr)
                
        
        
        arr[i], arr[minimo] = arr[minimo], arr[i]
        movimientos_i += 1
        
    
    print(f"Iteraciones: {iteraciones_i}")
    print(f"Consultas: {consultas_i}")
    print(f"Movimientos: {movimientos_i}")
    return arr


def counting_sort(arr):


    return arr