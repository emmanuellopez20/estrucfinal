def solve(n : int, arr : list):
    for i in range(1, n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

def insertion(n : int, arr : list):
    '''
    complete documentation of how it works Insertion sort
    '''
    
    print('\nInsertion sort\n'
          'Comparisons, Swaps (worst) : (n^2-n)/2')
    
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
    
    for i in range(1, n):
        iters += 1
        #compa += 1
        j = i
        while j>0:
            '''
            compa += 1
            if arr[j-1]>arr[j]:
                swaps += 1
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            else:
                break
            '''
            compa += 1
            query += 2
            if arr[j-1] <= arr[j]: break
            swaps += 1
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        print(arr)

    return arr, iters, query, compa, swaps

def showResult5(n, a):
    res = insertion(n, a[:])

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