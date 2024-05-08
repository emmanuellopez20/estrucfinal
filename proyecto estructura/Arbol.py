class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value, counter):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            counter['interactions'] += 1
            root.left = insert(root.left, value, counter)
        else:
            counter['interactions'] += 1
            root.right = insert(root.right, value, counter)
    return root

def inorder_traversal(root, result, counter):
    if root:
        inorder_traversal(root.left, result, counter)
        result.append(root.value)
        counter['movements'] += 1
        inorder_traversal(root.right, result, counter)