import time  # Importa el módulo de tiempo para funciones relacionadas con el tiempo
import os  # Importa el módulo del sistema operativo para interactuar con el sistema operativo
from Arbol import insert, inorder_traversal  # Importa las funciones 'insert' e 'inorder_traversal' del módulo 'Arbol'
import matplotlib.pyplot as plt  # Importa matplotlib.pyplot para crear gráficos
import networkx as nx  # Importa networkx para la creación, manipulación y estudio de la estructura de redes complejas
from avltree import AVLTree

# Inicializa varios diccionarios y listas
usuarios = {}
contrasenas = {}
biblio = {}
end = 0
list2 = []
passwrd = []

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
    lista = []  # Declara la lista a utilizar
    ele = int(input("Cuantos elementos desea insertar: "))  # Solicita al usuario el número de elementos a insertar
    elements_input = input("Inserte los elementos de la lista: ")  # Solicita al usuario los elementos de la lista
    elements = elements_input.split()  # Divide la cadena de entrada en elementos individuales usando espacios como delimitador
    for element in elements:
        try:
            num = int(element)  # Convierte cada elemento en un entero
            lista.append(num)  # Agrega el elemento a la lista
        except ValueError:  # Si el elemento no es un entero válido, imprime un mensaje de error y sale de la función
            print(f"Error: '{element}' no es un entero válido")
            return
    print('\nLista original', lista)  # Imprime la lista original

    # Solicita al usuario que elija un método de ordenamiento
    eleg=input('\n¿Que metodo deseas utilizar?\n\n1.Burbuja\n2.Burbuja mejorado\n3.selection\n4.Insert\n5.Merge\n6.Bucket\n7.Comb\n')
    # Mientras la opción ingresada no sea válida, solicita al usuario que ingrese una opción válida
    while eleg not in {"1", "2", "3", "4", "5", "6","7", "8"}:
        print("\nOpcion incorrecta")
        eleg=input('\n¿Que metodo deseas utilizar?\n\n1.Burbuja\n2.Burbuja mejorado\n3.De seleccion\n4.De inserseccion\n5.Por mezcla\n7.Bucket\n8.Comb\n')
    # Dependiendo de la opción elegida, llama a la función correspondiente
    if eleg == "1":
        showResult3(len(lista), lista)  # Llama a la función 'showResult3' con la longitud de la lista y la lista como argumentos
    if eleg == "2":
         showResult4(len(lista), lista)  # Llama a la función 'showResult4' con la longitud de la lista y la lista como argumentos
    if eleg == "3":
        showResult6(len(lista), lista)  # Llama a la función 'showResult6' con la longitud de la lista y la lista como argumentos
    if eleg == "4":
        showResult5(len(lista), lista)  # Llama a la función 'showResult5' con la longitud de la lista y la lista como argumentos
    if eleg == "5":
        ordenada, iteracio, compar, movimient = merge_sort(lista)  # Llama a la función de ordenamiento de mezcla
        print("Lista ordenada: ", ordenada)  # Imprime la lista ordenada
        print(f'\nAqui esta tu lista ordenada en {iteracio} iteraciones, {movimient} movimientos y {compar} consultas de manera ascendente:\n ')
    elif eleg == "6":
        showResult(len(lista), lista)  # Llama a la función 'showResult' con la longitud de la lista y la lista como argumentos
    elif eleg == "7":
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

# Ordenamiento por mezcla
def merge_sort(lista):
    iteracio = 0  # Contador de iteraciones
    compar = 0  # Contador de comparaciones
    movimient = 0  # Contador de movimientos
    if len(lista) > 1:  # Si la longitud de la lista es mayor que 1
        mid = len(lista) // 2  # Calcula el punto medio de la lista
        left_half = lista[:mid]  # Divide la lista en la mitad izquierda
        right_half = lista[mid:]  # Divide la lista en la mitad derecha
        left_half, left_iter, left_comp, left_mov = merge_sort(left_half)  # Llama recursivamente a la función de ordenamiento por mezcla para la mitad izquierda
        right_half, right_iter, right_comp, right_mov = merge_sort(right_half)  # Llama recursivamente a la función de ordenamiento por mezcla para la mitad derecha
        iteracio += left_iter + right_iter  # Suma las iteraciones de las mitades izquierda y derecha
        compar += left_comp + right_comp  # Suma las comparaciones de las mitades izquierda y derecha
        movimient += left_mov + right_mov  # Suma los movimientos de las mitades izquierda y derecha
        i = j = k = 0  # Inicializa los contadores i, j y k
        while i < len(left_half) and j < len(right_half):  # Mientras i sea menor que la longitud de la mitad izquierda y j sea menor que la longitud de la mitad derecha
            compar += 1  # Incrementa el contador de comparaciones
            if left_half[i] < right_half[j]:  # Si el elemento de la mitad izquierda es menor que el elemento de la mitad derecha
                lista[k] = left_half[i]  # Asigna el elemento de la mitad izquierda a la lista
                i += 1  # Incrementa i
            else:
                lista[k] = right_half[j]  # Asigna el elemento de la mitad derecha a la lista
                j += 1  # Incrementa j
            k += 1  # Incrementa k
            movimient += 1  # Incrementa el contador de movimientos
        while i < len(left_half):  # Mientras i sea menor que la longitud de la mitad izquierda
            lista[k] = left_half[i]  # Asigna el elemento de la mitad izquierda a la lista
            i += 1  # Incrementa i
            k += 1  # Incrementa k
            movimient += 1  # Incrementa el contador de movimientos
        while j < len(right_half):  # Mientras j sea menor que la longitud de la mitad derecha
            lista[k] = right_half[j]  # Asigna el elemento de la mitad derecha a la lista
            j += 1  # Incrementa j
            k += 1  # Incrementa k
            movimient += 1  # Incrementa el contador de movimientos
        iteracio += 1  # Incrementa el contador de iteraciones
    return (lista, iteracio, compar, movimient)  # Devuelve la lista y los contadores

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

#def menu_arb():


#-------------------------Funcion login-----------------------------------------#    



#Eliminar usuarios del registro#
def delet():
    print("<--|ELIMINAR REGISTRO|-->")
    u1 = input("Ingrese el usuario que deasea eliminar:")  # Solicita al usuario que ingrese el nombre de usuario que desea eliminar

    if u1 in usuarios.keys():  # Evalúa si el usuario existe
        C = input("Ingresa la contraseña por favor: ")  # Solicita al usuario que ingrese la contraseña
        if C == contrasenas[u1]:  # Evalúa si la contraseña es correcta y corresponde
            os.system('cls')  # Limpia la consola
            dlt(u1)  # Llama a la función "dlt"
        else:
            os.system('cls')  # Limpia la consola
            print("\nCONTRASEÑA INCORRECTA. VUELVA A INTENTARLO")  # Informa al usuario que la contraseña es incorrecta
            delet()  # Llama a la función "delet"
    else:
        os.system('cls')  # Limpia la consola
        print("\nUSUARIO INEXISTENTE")  # Informa al usuario que el usuario no existe

def dlt(u1):
    # Elimina el usuario de los diccionarios
    del usuarios[u1]  # Elimina el usuario del diccionario de usuarios
    del contrasenas[u1]  # Elimina el usuario del diccionario de contraseñas
    print("<--|USUARIO ELIMINADO EXITOSAMENTE-->>")  # Informa al usuario que el usuario ha sido eliminado exitosamente
    time.sleep(2)  # Espera 2 segundos
    os.system('cls')  # Limpia la consola

#Login
def login():
    i = 0  # Inicializa el contador i
    P = input("Ingresa tu usuario ya registrado: ")  # Solicita al usuario que ingrese un usuario ya registrado
    if P in usuarios.keys():  # Si el usuario existe en el diccionario de usuarios
        C = input("Ingresa su Contraseña: ")  # Solicita al usuario que ingrese la contraseña
        if C == contrasenas[P]:  # Si la contraseña ingresada coincide con la contraseña almacenada en el diccionario para ese usuario
            os.system('cls')  # Limpia la consola
            menu()  # Llama a la función del menú
        else:
            print("\nCONTRASEÑA INCORRECTA. VUELVA A INTENTARLO PORFAVOR")  # Informa al usuario que la contraseña es incorrecta
            os.system('cls')  # Limpia la consola
            time.sleep(2)  # Espera 2 segundos
            login()  # Llama a la función de inicio de sesión
    else:
        print("\nUSUARIO INEXISTENTE. VUELVA A INTENTARLO PORFAVOR")  # Informa al usuario que el usuario no existe
        time.sleep(2)  # Espera 2 segundos
        os.system('cls')  # Limpia la consola
        return  # Sale de la función


# Función para registrar la contraseña
def regC(P):
    global usuarios  # Accede a la variable global 'usuarios'
    global contrasenas  # Accede a la variable global 'contrasenas'
    counter = len(usuarios)  # Cuenta la cantidad de usuarios existentes
    strC = str(counter)  # Convierte el contador a una cadena
    C = input("Ingresa su Contraseña (8 caracteres exactos): ")  # Solicita al usuario que ingrese una contraseña de exactamente 8 caracteres
    if len(C) == 8:  # Si la longitud de la contraseña es 8
        usuarios[P] = P  # Almacena el nombre de usuario en el diccionario de usuarios
        contrasenas[P] = C  # Almacena la contraseña en el diccionario de contraseñas
        os.system('cls')  # Limpia la consola
    else:  # Si la longitud de la contraseña no es 8
        print("\nCONTRASEÑA INVÁLIDA")  # Informa al usuario que la contraseña es inválida
        time.sleep(2)  # Espera 2 segundos
        os.system('cls')  # Limpia la consola
        regC(P)  # Llama a la función 'regC' para solicitar al usuario que ingrese una contraseña válida

# Función para registrar un usuario
def reg():
    print("\n<--|REGISTRO|-->")  # Imprime un mensaje de bienvenida al registro
    global usuarios  # Accede a la variable global 'usuarios'
    global contrasenas  # Accede a la variable global 'contrasenas'
    P = input("Ingresa tu usuario: ")  # Solicita al usuario que ingrese un nombre de usuario
    
    if P not in usuarios.keys():  # Si el nombre de usuario no existe en el diccionario de usuarios
        usuarios[P] = P  # Almacena el nombre de usuario en el diccionario de usuarios
        regC(P)  # Llama a la función 'regC' para registrar la contraseña
    else:  # Si el nombre de usuario ya existe en el diccionario de usuarios
        print("\nUSUARIO YA REGISTRADO. VUELVA A INTENTARLO PORFAVOR")  # Informa al usuario que el nombre de usuario ya está registrado
        os.system('cls')  # Limpia la consola
        reg()  # Llama a la función 'reg' para solicitar al usuario que ingrese un nombre de usuario diferente



# Función principal
def main(end):
    while end == 0:  # Mientras 'end' sea 0, el programa continuará ejecutándose
        a = input("\n<---BIENVENIDO--->\nEscoga una opción.\n \n<---1. Registrar usuario  \n<---2. Iniciar sesión  \n<---3. Eliminar usuario del registro\n<---4.Menu de ordenamientos \n<---5. Salir\n")  # Solicita al usuario que elija una opción
        while a not in {"1", "2", "3", "4", "5","6"}:  # Mientras la opción elegida no sea válida
            print("\nOPCIÓN INVÁLIDA")  # Informa al usuario que la opción es inválida
            a = input("\n<---BIENVENIDO--->\nEscoga una opción.\n \n<---1. Registrar usuario  \n<---2. Iniciar sesión  \n<---3. Eliminar usuario del registro\n<---4.Menu de ordenamientos \n<---5. Salir\n")  # Solicita al usuario que elija una opción válida
        if a == "1":  # Si la opción elegida es '1'
            os.system('cls')  # Limpia la consola
            reg()  # Llama a la función 'reg' para registrar un usuario
        elif a == "2":  # Si la opción elegida es '2'
            os.system('cls')  # Limpia la consola
            login()  # Llama a la función 'login' para iniciar sesión
        elif a == "3":  # Si la opción elegida es '3'
            os.system('cls')  # Limpia la consola
            delet()  # Llama a la función 'delet' para eliminar un usuario del registro
        elif a == "4":  # Si la opción elegida es '4'
           os.system('cls')  # Limpia la consola
           menu()  # Llama a la función 'menu' para mostrar el menú de ordenamientos
        elif a == "5":  # Si la opción elegida es '5'
            print("\nTerminando sesion")  # Informa al usuario que la sesión está terminando
            end = 1  # Establece 'end' como 1 para terminar el programa

main(end) 