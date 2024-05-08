'''
TODO
- chechar si bucket sort solo sirve para valores positivos
'''

def solve(n : int, arr : list):
    # find the max value in arr
    max_value = arr[0]
    for i in range(1, n):
        if max_value < arr[i]: max_value = arr[i]
    max_value += 1

    # k buckets
    k = n
    buckets = [[] for i in range(n)]

    output = []

    for i in range(n):
        buckets[abs(int(arr[i] * k / max_value))].append(arr[i])

    for i in range(k):
        # sort each bucket 
        buckets[i].sort()
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])
    return output

def explain(n : int, arr : list):
    '''
    complete documentation of how it works Bucket sort
    '''

    k = input('k:')
    try:
        k = abs(int(k))
    except ValueError:
        print('\n ! k deber ser entero positivo')
        print('Se asigno k := n')
        k = n
    
    print('\nBucket sort\n'
          'Complexity (worst) : O(n+k)')
    
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
    
    # find the max value in arr
    max_value = arr[0]
    for i in range(1, n):
        if max_value < arr[i]: max_value = arr[i]
    max_value += 1
    print(' max value + 1:', max_value)

    # k buckets
    buckets = [[] for i in range(k)]

    output = []

    for i in range(n):
        iters += 1
        query += 2
        buckets[abs(int(arr[i] * k / max_value))].append(arr[i])
    print('\n buckets:')
    print(buckets)

    for i in range(k):
        iters += 1
        # sort each bucket 
        buckets[i].sort()
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])
    print('\n buckets sorted:')
    print(buckets)
            
    return output, iters, query, compa, swaps

def showResult(n, a):
    res = explain(n, a[:])

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
    a = random.sample(range(0, 31), n)
    showResult(n, a)

    # worst case
    print('\nWorst case')
    a = [i for i in range(n, 0, -1)]
    showResult(n, a)

# https://en.wikipedia.org/wiki/Bucket_sort