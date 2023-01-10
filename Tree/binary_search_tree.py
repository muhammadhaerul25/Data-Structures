class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def search(self, val):
        current = self.root
        while current is not None:
            if current.val == val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False

    def get_height(self):
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        return height(self.root)

    def print_tree(self):
        def print_nodes(node, level):
            if node is not None:
                print_nodes(node.left, level + 1)
                print(' ' * 4 * level + '->', node.val)
                print_nodes(node.right, level + 1)

        print_nodes(self.root, 0)


tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)


print(tree.get_height())  # prints 3
tree.print_tree()  # prints the tree in a readable format
