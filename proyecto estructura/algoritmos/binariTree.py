class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value, counter):
    if root is None:
        counter['movements'] += 1
        return TreeNode(value)
    if value < root.value:
        counter['interactions'] += 1
        root.left = insert(root.left, value, counter)
    else:
        counter['interactions'] += 1
        root.right = insert(root.right, value, counter)
    return root

def inorder_traversal(root, result, counter):
    if root:
        counter['interactions'] += 1
        inorder_traversal(root.left, result, counter)
        result.append(root.value)
        counter['movements'] += 1
        inorder_traversal(root.right, result, counter)

def binary_tree_sort(arr):
    root = None
    counter = {'interactions': 0, 'movements': 0}
    for value in arr:
        root = insert(root, value, counter)
    result = []
    inorder_traversal(root, result, counter)
    return result, counter

# Ejemplo de uso
arr = [8,2,1,9,5,4,3]
sorted_arr, counter = binary_tree_sort(arr)
print("Lista ordenada:", sorted_arr)
print("Interacciones realizadas:", counter['interactions'])
print("Movimientos realizados:", counter['movements'])
