import time  # Importa el módulo de tiempo para funciones relacionadas con el tiempo
import os  # Importa el módulo del sistema operativo para interactuar con el sistema operativo
from Arbol import insert, inorder_traversal  # Importa las funciones 'insert' e 'inorder_traversal' del módulo 'Arbol'
import matplotlib.pyplot as plt  # Importa matplotlib.pyplot para crear gráficos
import networkx as nx  # Importa networkx para la creación, manipulación y estudio de la estructura de redes complejas
from avltree import AVLTree
import re

# Inicializa varios diccionarios y listas
usuarios = {i: ' '*8 for i in range(8)}
contrasenas = {i: ' '*8 for i in range(8)}
posicion = 0
end = 0
list2 = []


# Función del menú principal
def menu():
    # Solicita al usuario que elija una opción
    b = input("\nElija una opción\n\n1.Métodos de ordenamiento\n2.Arbol binario\n3. Arbol Avl\n4. salir")
    # Mientras la opción ingresada no sea válida, solicita al usuario que ingrese una opción válida
    while b not in {"1", "2","3","4",}:
        print("\nOPCIÓN INVÁLIDA")
        b = input("\nElija una de las siguientes opciones:\n\n<--1. Métodos de ordenamiento\n<---2. Arboles\n<---3. salir")
    # Dependiendo de la opción elegida, llama a la función correspondiente o sale del programa
    if b == "1":
        os.system('cls')  # Limpia la consola
        menu_ord()  # Llama a la función del menú de ordenamiento
    elif b == "2":
        os.system('cls')  # Limpia la consola
        interactive_binary_tree_sort()  # Llama a la función de ordenamiento de árbol binario interactivo
    elif b == "3":
        os.system('cls')  # Limpia la consola
        interact_with_avl_tree()
    elif b == "4":
        os.system('cls')  # Limpia la consola
        main(0)  # Llama a la función principal con 0 como argumento

# Función del menú de ordenamiento
def menu_ord():
    lista = []
    while True:
        try:
            ele = int(input("Cuantos elementos desea insertar: "))
            break
        except ValueError:
            print("Por favor, ingresa un número entero.")
    while len(lista) < ele:
        elements_input = input("Inserte los elementos de la lista: ")
        elements = elements_input.split()
        for element in elements:
            try:
                num = int(element)
                lista.append(num)
                if len(lista) == ele:
                    break
            except ValueError:
                print(f"Error: '{element}' no es un entero válido. Por favor, ingresa solo números enteros.")
    print('\nLista original', lista)
    eleg=input('\n¿Que metodo deseas utilizar?\n\n1.Burbuja\n2.Burbuja mejorado\n3.selection\n4.Insert\n5.Bucket\n6.Comb\n7.Counting Sort\n8.Shell Sort\n')
    while eleg not in {"1", "2", "3", "4", "5", "6","7", "8", "9"}:
        print("\nOpcion incorrecta")
        eleg=input('\n¿Que metodo deseas utilizar?\n\n1.Burbuja\n2.Burbuja mejorado\n3.De seleccion\n4.De inserseccion\n5.Bucket\n6.Comb\n7.Counting Sort\n8.Shell Sort\n')
    if eleg == "8":
        sorted_arr = shell_sort(lista)
        print("Arreglo organizado:", sorted_arr)
    elif eleg == "7":
        sorted_arr = countingSort(lista)
        print("Arreglo organizado:", sorted_arr)
    # Dependiendo de la opción elegida, llama a la función correspondiente
    elif eleg == "1":
        showResult3(len(lista), lista)  # Llama a la función 'showResult3' con la longitud de la lista y la lista como argumentos
    elif eleg == "2":
        showResult4(len(lista), lista)  # Llama a la función 'showResult4' con la longitud de la lista y la lista como argumentos
    elif eleg == "3":
        showResult6(len(lista), lista)  # Llama a la función 'showResult6' con la longitud de la lista y la lista como argumentos
    elif eleg == "4":
        showResult5(len(lista), lista)  # Llama a la función 'showResult5' con la longitud de la lista y la lista como argumentos
    elif eleg == "5":
        showResult(len(lista), lista)  # Llama a la función 'showResult' con la longitud de la lista y la lista como argumentos
    elif eleg == "6":
        showResult2(len(lista), lista)  # Llama a la función 'showResult2' con la longitud de la lista y la lista como argumentos

# Función de ordenamiento de árbol binario interactivo
def interactive_binary_tree_sort():
    root = None  # Inicializa la raíz del árbol binario
    counter = {'interactions': 0, 'movements': 0}  # Inicializa un contador para las interacciones y los movimientos
    while True:  # Mientras sea verdadero
        value = input("Enter a number to add to the binary tree (or 'q' to quit): ")  # Solicita al usuario que ingrese un número para agregar al árbol binario o 'q' para salir
        if value.lower() == 'q':  # Si el valor ingresado es 'q', rompe el ciclo
            break
        try:
            value = int(value)  # Intenta convertir el valor ingresado en un entero
            root = insert(root, value, counter)  # Inserta el valor en el árbol binario
            result = []  # Inicializa una lista para el resultado
            inorder_traversal(root, result, counter)  # Realiza un recorrido en orden del árbol binario
            print("Sorted tree:", result)  # Imprime el árbol ordenado
            print("Interactions:", counter['interactions'])  # Imprime el número de interacciones
            print("Movements:", counter['movements'])  # Imprime el número de movimientos
            visualize_binary_tree(root)  # Visualiza el árbol binario
        except ValueError:  # Si el valor ingresado no es un entero válido, imprime un mensaje de error
            print("Invalid input. Please enter a valid number.")

# Función para visualizar el árbol binario
def visualize_binary_tree(root):
    G = nx.DiGraph()  # Crea un gráfico dirigido

    # Función para agregar nodos y bordes al gráfico
    def add_nodes_edges(tree, parent=None):
        if tree is not None:  # Si el árbol no es nulo
            if parent is not None:  # Si el padre no es nulo
                G.add_node(tree.value)  # Agrega un nodo al gráfico con el valor del árbol
                G.add_edge(parent.value, tree.value)  # Agrega un borde al gráfico desde el valor del padre hasta el valor del árbol
            add_nodes_edges(tree.left, tree)  # Agrega nodos y bordes para el subárbol izquierdo
            add_nodes_edges(tree.right, tree)  # Agrega nodos y bordes para el subárbol derecho

    add_nodes_edges(root)  # Agrega nodos y bordes para la raíz del árbol

    pos = nx.spring_layout(G)  # Crea una disposición para el gráfico
    plt.figure()  # Crea una nueva figura
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, arrowsize=20)  # Dibuja el gráfico con etiquetas y especifica el color, tamaño y tamaño de las flechas
    plt.ion()  # Habilita el modo interactivo
    plt.show()  # Muestra la figura

def interact_with_avl_tree():
    avl = AVLTree()
    while True:
        print("\nSubmenú del Árbol AVL")
        print("1. Insertar elementos")
        print("2. Eliminar un elemento")
        print("3. Mostrar el árbol")
        print("4. Regresar al menú principal")
        option = input("Elige una opción: ")
        if option == "1":
            elements = input("Ingresa los elementos a insertar separados por espacios: ")
            elements = list(map(int, elements.split()))
            for element in elements:
                avl.insert(element)
                print(avl)
        elif option == "2":
            element = int(input("Ingresa el elemento a eliminar: "))
            avl.delete_value(element)
            print(avl)
        elif option == "3":
            print(avl)
        elif option == "4":
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")


# Función de ordenamiento de burbuja
def bubble(n : int, arr : list2):
    '''
    Documentación completa de cómo funciona el ordenamiento de burbuja
    '''
    
    print('\nOrdenamiento de burbuja\n'
          'Complejidad : O(n^2)\n'
          'Comparaciones: (n-1)^2')  # Imprime información sobre el ordenamiento de burbuja
    
    print('\nLista original:')
    print(arr)  # Imprime la lista original
    print()

    # iteraciones
    iters = 0  # Inicializa el contador de iteraciones
    # consultas (querys)
    query = 0  # Inicializa el contador de consultas
    # comparaciones <, >
    compa = 0  # Inicializa el contador de comparaciones
    # movimientos (swaps)
    swaps = 0  # Inicializa el contador de intercambios
    
    for i in range(n-1):  # Realiza un ciclo desde 0 hasta n-1
        iters += 1  # Incrementa el contador de iteraciones
        for j in range(n-1):  # Realiza un ciclo desde 0 hasta n-1
            query += 2  # Incrementa el contador de consultas
            compa += 1  # Incrementa el contador de comparaciones
            if arr[j] > arr[j+1]:  # Si el elemento actual es mayor que el siguiente
                swaps += 1  # Incrementa el contador de intercambios
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambia los elementos
        print(arr)  # Imprime la lista
    return arr, iters, query, compa, swaps  # Devuelve la lista y los contadores

# Función para mostrar los resultados del ordenamiento de burbuja
def showResult3(n, a):
    res = bubble(n, a[:])  # Llama a la función de ordenamiento de burbuja

    print('\n- - - - -')
    print('\nResultados:')
    print(' iteraciones:', res[1])  # Imprime el número de iteraciones
    print(' Consultas (querys):', res[2])  # Imprime el número de consultas
    print(' Comparaciones:', res[3])  # Imprime el número de comparaciones
    print(' Intercambios (swaps):', res[4])  # Imprime el número de intercambios
    print('\n ¿Correctamente ordenado? ', sorted(a)==res[0])  # Verifica si la lista está correctamente ordenada
    print('\n', res[0])  # Imprime la lista ordenada


# Ordenamiento de burbuja mejorado
def cocktail(n : int, arr : list2):
    '''
    Documentación completa de cómo funciona el ordenamiento de burbuja mejorado
    '''
    
    print('\nMejor ordenamiento de burbuja\n'
          'Complejidad : O(n^2)\n'
          'Comparaciones : (n^2 - n) / 2')
    
    print('\nLista original:')
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
    
    for i in range(n-1):  # Realiza un ciclo desde 0 hasta n-1
        iters += 1  # Incrementa el contador de iteraciones
        for j in range(n-1-i):  # Realiza un ciclo desde 0 hasta n-1-i
            query += 2  # Incrementa el contador de consultas
            compa += 1  # Incrementa el contador de comparaciones
            if arr[j] > arr[j+1]:  # Si el elemento actual es mayor que el siguiente
                swaps += 1  # Incrementa el contador de intercambios
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambia los elementos
        print(arr)  # Imprime la lista

        # Segundo ciclo que recorre la lista de derecha a izquierda
        for j in range(n-2-i, -1, -1):
            query += 2  # Incrementa el contador de consultas
            compa += 1  # Incrementa el contador de comparaciones
            if arr[j] > arr[j+1]:  # Si el elemento actual es mayor que el siguiente
                swaps += 1  # Incrementa el contador de intercambios
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambia los elementos
        print(arr)  # Imprime la lista

    return arr, iters, query, compa, swaps  # Devuelve la lista y los contadores
def showResult4(n, a):
    res = cocktail(n, a[:])  # Llama a la función de ordenamiento de burbuja mejorado

    print('\n- - - - -')
    print('\nResultados:')
    print(' iteraciones:', res[1])  # Imprime el número de iteraciones
    print(' Consultas (querys):', res[2])  # Imprime el número de consultas
    print(' Comparaciones:', res[3])  # Imprime el número de comparaciones
    print(' Intercambios (swaps):', res[4])  # Imprime el número de intercambios
    print('\n ¿Correctamente ordenado? ', sorted(a)==res[0])  # Verifica si la lista está correctamente ordenada
    print('\n', res[0])  # Imprime la lista ordenada

# Ordenamiento por selección
def selection(n : int, arr : list2):
    '''
    Documentación completa de cómo funciona el ordenamiento por selección
    '''
    
    print('\nOrdenamiento por selección\n'
          'Complejidad : O(n^2)\n'
          'Comparaciones : (n^2 - n) / 2')
    
    print('\nLista original:')
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
    
    for i in range(n-1):  # Realiza un ciclo desde 0 hasta n-1
        iters += 1  # Incrementa el contador de iteraciones
        menor = i  # Asume que el elemento actual es el menor
        for j in range(i+1, n):  # Realiza un ciclo desde i+1 hasta n
            query += 2  # Incrementa el contador de consultas
            compa += 1  # Incrementa el contador de comparaciones
            if arr[j] < arr[menor]:  # Si el elemento actual es menor que el menor
                menor = j  # Actualiza el menor
        swaps += 1  # Incrementa el contador de intercambios
        arr[i], arr[menor] = arr[menor], arr[i]  # Intercambia el elemento actual con el menor
        print(arr)  # Imprime la lista
    return arr, iters, query, compa, swaps  # Devuelve la lista y los contadores

def showResult6(n, a):
    res = selection(n, a[:])  # Llama a la función de ordenamiento por selección

    print('\n- - - - -')
    print('\nResultados:')
    print(' iteraciones:', res[1])  # Imprime el número de iteraciones
    print(' Consultas (querys):', res[2])  # Imprime el número de consultas
    print(' Comparaciones:', res[3])  # Imprime el número de comparaciones
    print(' Intercambios (swaps):', res[4])  # Imprime el número de intercambios
    print('\n ¿Correctamente ordenado? ', sorted(a)==res[0])  # Verifica si la lista está correctamente ordenada

    print('\n', res[0])  # Imprime la lista ordenada

# Ordenamiento por inserción
def insertion(n : int, arr : list2):
    '''
    Documentación completa de cómo funciona el ordenamiento por inserción
    '''
    
    print('\nOrdenamiento por inserción\n'
          'Comparaciones, Intercambios (peor caso) : (n^2-n)/2')
    
    print('\nLista original:')
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
    
    for i in range(1, n):  # Realiza un ciclo desde 1 hasta n
        iters += 1  # Incrementa el contador de iteraciones
        j = i  # Inicializa j con el valor de i
        while j>0:  # Mientras j sea mayor que 0
            compa += 1  # Incrementa el contador de comparaciones
            query += 2  # Incrementa el contador de consultas
            if arr[j-1] <= arr[j]: break  # Si el elemento anterior es menor o igual que el elemento actual, rompe el ciclo
            swaps += 1  # Incrementa el contador de intercambios
            arr[j], arr[j-1] = arr[j-1], arr[j]  # Intercambia el elemento actual con el anterior
            j -= 1  # Decrementa j
        print(arr)  # Imprime la lista

    return arr, iters, query, compa, swaps  # Devuelve la lista y los contadores

def showResult5(n, a):
    res = insertion(n, a[:])  # Llama a la función de ordenamiento por inserción

    print('\n- - - - -')
    print('\nResultados:')
    print(' iteraciones:', res[1])  # Imprime el número de iteraciones
    print(' Consultas (querys):', res[2])  # Imprime el número de consultas
    print(' Comparaciones:', res[3])  # Imprime el número de comparaciones
    print(' Intercambios (swaps):', res[4])  # Imprime el número de intercambios
    print('\n ¿Correctamente ordenado? ', sorted(a)==res[0])  # Verifica si la lista está correctamente ordenada

    print('\n', res[0])  # Imprime la lista ordenada


# Ordenamiento por cubetas
def bucket(n : int, arr : list2):
    k = input('k:')  # Solicita al usuario que ingrese un valor para k
    try:
        k = abs(int(k))  # Intenta convertir el valor ingresado en un entero positivo
    except ValueError:  # Si el valor ingresado no es un entero válido
        print('\n! k debe ser entero positivo')  # Informa al usuario que k debe ser un entero positivo
        print('Se asigno k := n')  # Informa al usuario que se asignó k como n
        k = n  # Asigna k como n
    print('\nBucket sort\n'
           'Complexity (worst): O(n+k)')  # Imprime información sobre el ordenamiento por cubetas
    print('\nOriginal list:')  # Imprime 'Original list:'
    print(arr)  # Imprime la lista original
    print()
    # iteraciones
    iters = 0  # Inicializa el contador de iteraciones
    # consultas (querys)
    query = 0  # Inicializa el contador de consultas
    # comparaciones <, >
    compa = 0  # Inicializa el contador de comparaciones
    # movimientos (swaps)
    swaps = 0  # Inicializa el contador de intercambios
    # find the max value in arr
    max_value = arr[0]  # Inicializa el valor máximo con el primer elemento de la lista
    for i in range(1, n):  # Realiza un ciclo desde 1 hasta n
        if max_value < arr[i]: max_value = arr[i]  # Si el valor máximo es menor que el elemento actual, actualiza el valor máximo
    max_value += 1  # Incrementa el valor máximo en 1
    print('max value + 1:', max_value)  # Imprime 'max value + 1:' y el valor máximo
    # k buckets
    buckets = [[] for _ in range(k)]  # Crea k cubetas
    output = []  # Inicializa la lista de salida
    for i in range(n):  # Realiza un ciclo desde 0 hasta n
        iters += 1  # Incrementa el contador de iteraciones
        query += 2  # Incrementa el contador de consultas
        buckets[abs(int(arr[i] * k / max_value))].append(arr[i])  # Agrega el elemento actual a la cubeta correspondiente
    print('\nBuckets:')  # Imprime 'Buckets:'
    print(buckets)  # Imprime las cubetas
    for i in range(k):  # Realiza un ciclo desde 0 hasta k
        iters += 1  # Incrementa el contador de iteraciones
        # sort each bucket
        buckets[i].sort()  # Ordena cada cubeta
        for j in range(len(buckets[i])):  # Realiza un ciclo desde 0 hasta la longitud de la cubeta actual
            output.append(buckets[i][j])  # Agrega cada elemento de la cubeta a la lista de salida
    return output, iters, query, compa, swaps  # Devuelve la lista de salida y los contadores

def showResult(n, a):
    res = bucket(n, a[:])  # Llama a la función de ordenamiento por cubetas

    print('\n- - - - -')
    print('\nResultados:')
    print(' iteraciones:', res[1])  # Imprime el número de iteraciones
    print(' Consultas (querys):', res[2])  # Imprime el número de consultas
    print(' Comparaciones:', res[3])  # Imprime el número de comparaciones
    print(' Intercambios (swaps):', res[4])  # Imprime el número de intercambios
    print('\n Correctamente?', sorted(a) == res[0])  # Verifica si la lista está correctamente ordenada
    print('\n', res[0])  # Imprime la lista ordenada

# Ordenamiento peine
def comb(n : int, arr : list2):
    '''
    Documentación completa de cómo funciona el ordenamiento peine
    '''
    
    print('\nOrdenamiento peine')  # Imprime 'Ordenamiento peine'
    
    print('\nLista original:')  # Imprime 'Lista original:'
    print(arr, '\n')  # Imprime la lista original

    # iteraciones
    iters = 0  # Inicializa el contador de iteraciones
    # consultas (querys)
    query = 0  # Inicializa el contador de consultas
    # comparaciones <, >
    compa = 0  # Inicializa el contador de comparaciones
    # movimientos (swaps)
    swaps = 0  # Inicializa el contador de intercambios
    
    gap = int(n / 1.3)  # Calcula el tamaño del gap
    is_sorted = True  # Inicializa is_sorted como True

    while is_sorted:  # Mientras is_sorted sea True
        iters += 1  # Incrementa el contador de iteraciones
        if gap <= 1:  # Si el gap es menor o igual a 1
            gap = 1  # Establece el gap como 1
            is_sorted = False  # Establece is_sorted como False

        for r in range(gap, n):  # Realiza un ciclo desde gap hasta n
            l = r - gap  # Calcula l
            compa += 1  # Incrementa el contador de comparaciones
            query += 2  # Incrementa el contador de consultas
            if arr[l] > arr[r]:  # Si el elemento en la posición l es mayor que el elemento en la posición r
                swaps += 1  # Incrementa el contador de intercambios
                arr[l], arr[r] = arr[r], arr[l]  # Intercambia los elementos en las posiciones l y r
                is_sorted = True  # Establece is_sorted como True para asegurar que se hará burbuja hasta ordenar
        print(arr, 'gap =', gap, ', is_sorted =', not is_sorted)  # Imprime la lista, el gap y si está ordenada
        gap = int(gap / 1.3)  # Actualiza el gap
    return arr, iters, query, compa, swaps  # Devuelve la lista y los contadores

def showResult2(n, a):
    res = comb(n, a[:])  # Llama a la función de ordenamiento peine

    print('\n- - - - -')
    print('\nResultados:')
    print(' iteraciones:', res[1])  # Imprime el número de iteraciones
    print(' Consultas (querys):', res[2])  # Imprime el número de consultas
    print(' Comparaciones:', res[3])  # Imprime el número de comparaciones
    print(' Intercambios (swaps):', res[4])  # Imprime el número de intercambios
    print('\n ¿Correctamente ordenado? ', sorted(a) == res[0])  # Verifica si la lista está correctamente ordenada

    print('\n', res[0])  # Imprime la lista ordenada

def countingSort(arr):
    size = len(arr)
    max_value = max(arr)
    comparaciones = 0
    movimientos = 0
    iteraciones = 0
    count = [0] * (max_value + 1)
    output = [0] * size
    for m in arr:
        count[m] += 1
        iteraciones += 1
    for m in range(1, max_value + 1):
        count[m] += count[m - 1]
        iteraciones += 1
    for m in range(size - 1, -1, -1):
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        movimientos += 1
        comparaciones += 1
        iteraciones += 1
    print("Iteraciones :", iteraciones)
    print("Movimientos :", movimientos)
    print("Comparaciones :", comparaciones)
    return output

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr



#-------------------------Funcion login-----------------------------------------#    



#Eliminar usuarios del registro#
# Función para eliminar un usuario
def delet():
    print("<--|ELIMINAR REGISTRO|-->")
    u1 = input("Ingrese el usuario que desea eliminar: ")  # Solicita al usuario que ingrese el nombre de usuario que desea eliminar
    u1 = u1.ljust(8)  # Añade espacios al nombre del usuario hasta que tenga una longitud de 8 caracteres
    if u1 in usuarios.values():  # Evalúa si el usuario existe
        C = input("Ingresa la contraseña por favor: ")  # Solicita al usuario que ingrese la contraseña
        posicion = list(usuarios.values()).index(u1)
        if C == contrasenas[posicion]:  # Evalúa si la contraseña es correcta y corresponde
            dlt(posicion)  # Llama a la función "dlt"
        else:
            print("\nCONTRASEÑA INCORRECTA. VUELVA A INTENTARLO")  # Informa al usuario que la contraseña es incorrecta
            delet()  # Llama a la función "delet"
    else:
        print("\nUSUARIO INEXISTENTE")  # Informa al usuario que el usuario no existe

# Función para eliminar un usuario de los diccionarios
def dlt(posicion):
    # Elimina el usuario de los diccionarios
    usuarios[posicion] = ' '*8  # Establece el usuario en el diccionario de usuarios en ' '*8
    contrasenas[posicion] = ' '*8  # Establece el usuario en el diccionario de contraseñas en ' '*8
    os.remove(f"{posicion}_security.txt")  # Elimina el archivo de respuestas de seguridad del usuario
    print("<--|USUARIO ELIMINADO EXITOSAMENTE-->>")  # Informa al usuario que el usuario ha sido eliminado exitosamenteforma al usuario que el usuario ha sido eliminado exitosamente


# Función para iniciar sesión
def login():
    P = input("Ingresa tu usuario ya registrado: ")  # Solicita al usuario que ingrese un usuario ya registrado
    P = P.ljust(8)  # Añade espacios al nombre del usuario hasta que tenga una longitud de 8 caracteres
    if P in usuarios.values():  # Si el usuario existe en el diccionario de usuarios
        C = input("Ingresa su Contraseña: ")  # Solicita al usuario que ingrese la contraseña
        posicion = list(usuarios.values()).index(P)
        if C == contrasenas[posicion]:  # Si la contraseña ingresada coincide con la contraseña almacenada en el diccionario para ese usuario
            print("\nlogin exitoso\n")
            menu()  # Llama a la función del menú
        else:
            print("\nCONTRASEÑA INCORRECTA. VUELVA A INTENTARLO PORFAVOR")  # Informa al usuario que la contraseña es incorrecta
            login()  # Llama a la función de inicio de sesión
    else:
        print("\nUSUARIO INEXISTENTE. VUELVA A INTENTARLO PORFAVOR")  # Informa al usuario que el usuario no existe

# Función para registrar la contraseña
def regC():
    C = input("Ingresa su Contraseña (8 caracteres exactos): ")
    if len(C) != 8 or not re.search("\d", C) or not re.search("\W", C):
        print("\nCONTRASEÑA INVÁLIDA. DEBE TENER EXACTAMENTE 8 CARACTERES, AL MENOS UN NÚMERO Y AL MENOS UN CARÁCTER ESPECIAL.")
        regC()
    else:
        return C


# Función para registrar un usuario
def reg():
    print("\n<--|REGISTRO|-->")
    P = input("Ingresa tu usuario: ")
    P = P.ljust(8)  # Añade espacios al nombre del usuario hasta que tenga una longitud de 8 caracteres
    if not P.strip().isalnum():  # Usa strip() para eliminar los espacios antes de comprobar si el nombre de usuario es alfanumérico
        print("\nUSUARIO INVÁLIDO. SOLO SE PERMITEN LETRAS Y NÚMEROS.")
        reg()
    elif P not in usuarios.values():  # Comprueba si el usuario ya existe en el diccionario de usuarios
        # Busca la primera posición vacía en el diccionario de usuarios
        posicion = list(usuarios.values()).index(' '*8)
        usuarios[posicion] = P
        contrasenas[posicion] = regC()
        SecP(posicion)  # Llama a la función SecP para registrar las respuestas a las preguntas de seguridad
    else:
        print("\nUSUARIO YA REGISTRADO. VUELVA A INTENTARLO PORFAVOR")
        reg()

#funcion para imprimir usuario
def imprimir_diccionarios():
    print("Usuarios:")
    for i in range(8):
        print([char for char in usuarios[i]])

    print("\nContraseñas:")
    for i in range(8):
        print([char for char in contrasenas[i]])

# Función para registrar las respuestas a las preguntas de seguridad
def SecP(posicion):
    Q = input("Primera pregunta: Cual es tu ciudad de nacimiento?")
    Q2 = input("Segunda pregunta: Cual es tu numero favorito?\n")
    with open(f"{posicion}_security.txt", "w") as file:  # Crea un archivo .txt con el nombre del usuario
        file.write(Q + "\n")  # Escribe la primera respuesta en el archivo
        file.write(Q2 + "\n")  # Escribe la segunda respuesta en el archivo
    print("\n<<--REGISTRO COMPLETADO EXITOSAMENTE-->>")
    
# Función para restablecer la contraseña
def reset_password():
    P = input("Ingresa tu usuario: ")
    P = P.ljust(8)  # Añade espacios al nombre del usuario hasta que tenga una longitud de 8 caracteres
    if P in usuarios.values():  # Si el usuario existe en el diccionario de usuarios
        posicion = list(usuarios.values()).index(P)
        with open(f"{posicion}_security.txt", "r") as file:  # Abre el archivo .txt del usuario
            Q = file.readline().strip()  # Lee la primera respuesta del archivo
            Q2 = file.readline().strip()  # Lee la segunda respuesta del archivo
        Q_user = input("Primera pregunta: Cual es tu ciudad de nacimiento?")
        Q2_user = input("Segunda pregunta: Cual es tu numero favorito?\n")
        if Q == Q_user and Q2 == Q2_user:  # Si las respuestas del usuario coinciden con las respuestas guardadas
            new_password = regC()  # Solicita al usuario que ingrese una nueva contraseña
            contrasenas[posicion] = new_password  # Actualiza la contraseña en el diccionario de contraseñas
            print("\n<<--CONTRASEÑA ACTUALIZADA EXITOSAMENTE-->>")
        else:
            print("\nRESPUESTAS INCORRECTAS. INTÉNTALO DE NUEVO.")
    else:
        print("\nUSUARIO INEXISTENTE. VUELVA A INTENTARLO PORFAVOR")  # Informa al usuario que el usuario no existe


# Función principal
def main(end):
    while end == 0:  # Mientras 'end' sea 0, el programa continuará ejecutándose
        a = input("\n<---BIENVENIDO--->\nEscoga una opción.\n \n<---1. Registrar usuario  \n<---2. Iniciar sesión  \n<---3. Eliminar usuario del registro\n<---4.Menu de ordenamientos \n<---5.imprimir diccionarios\n<---6.Restablecer contraseña \n<---7. Salir\n")  # Solicita al usuario que elija una opción
        while a not in {"1", "2", "3", "4", "5","6","7"}:  # Mientras la opción elegida no sea válida
            print("\nOPCIÓN INVÁLIDA")  # Informa al usuario que la opción es inválida
            a = input("\n<---BIENVENIDO--->\nEscoga una opción.\n \n<---1. Registrar usuario  \n<---2. Iniciar sesión  \n<---3. Eliminar usuario del registro\n<---4.Menu de ordenamientos \n<---5.imprimir diccionarios\n<---6.Restablecer contraseña \n<---7. Salir\n")  # Solicita al usuario que elija una opción válida
        if a == "1":  # Si la opción elegida es '1'
            reg()  # Llama a la función 'reg' para registrar un usuario
        elif a == "2":  # Si la opción elegida es '2'
            login()  # Llama a la función 'login' para iniciar sesión
        elif a == "3":  # Si la opción elegida es '3'
            delet()  # Llama a la función 'delet' para eliminar un usuario del registro
        elif a == "4":  # Si la opción elegida es '4'
            menu()  # Llama a la función 'menu' para mostrar el menú de ordenamientos
        elif a == "5":  # Si la opción elegida es '5'
            imprimir_diccionarios()
        elif a == "6":  # Si la opción elegida es '6'
            reset_password()
        elif a == "7":  # Si la opción elegida es '7'
            print("\nTerminando sesion")  # Informa al usuario que la sesión está terminando
            end = 1  # Establece 'end' como 1 para terminar el programa

main(end) 
