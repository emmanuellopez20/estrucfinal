def solve(n : int, arr : list):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def cocktail(n : int, arr : list):
    '''
    complete documentation of how it works better Burbble sort
    '''
    
    print('\nbetter Bubble sort\n'
          'Complexity : O(n^2)\n'
          'Comparisons : (n^2 - n) / 2')
    
    print('\nOriginal list:')
    print(arr)
    print()

    # iteraciones
    iters = 0
    # consultas (querys)
    query = 0
    # comparaciones <, >
    compa = 0
    # movimientos (swaps)
    swaps = 0
    
    for i in range(n-1):
        iters += 1
        for j in range(n-1-i):
            query += 2
            compa += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr, iters, query, compa, swaps

def showResult4(n, a):
    res = cocktail(n, a[:])

    print('\n- - - - -')
    print('\nResultados:')
    print(' iteraciones:', res[1])
    print(' Consultas (querys):', res[2])
    print(' Comparaciones:', res[3])
    print(' Intercambios (swaps):', res[4])
    print('\n Correctamente? ', sorted(a)==res[0])

    print('\n', res[0])

if __name__ == '__main__':
    import random

    n = 8

    # average case
    print('Average case')
    a = random.sample(range(-20, 21), n)
    showResult(n, a)

    # worst case
    print('\nWorst case')
    a = [i for i in range(n, 0, -1)]
    showResult(n, a)