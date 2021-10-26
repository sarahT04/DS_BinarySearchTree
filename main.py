# Binary search implementation

class Node:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def get_value(self):
        return self.key

    def set_right(self, value):
        self.right = value

    def set_left(self, value):
        self.left = value


# in order to insert, we use recursive.
def insert(node, key):
    if node is None:
        return Node(key)

    # basically we're inserting a node
    if key < node.key:
        node.set_left(insert(node.left, key))
    elif key > node.key:
        node.set_right(insert(node.right, key))

    return node


def delete(node, key):
    def min_value_node(m_node):
        current = m_node
        while current.left is not None:
            current = current.left
        return current

    if node is None:
        return node

    if key < node.key:
        node.set_left(delete(node.left, key))
    elif key > node.key:
        node.set_right(delete(node.right, key))
    else:
        if node.left is None:
            temp, node = node.right, None
            return temp
        elif node.right is None:
            temp, node = node.left, None
            return temp

        min_key = min_value_node(node.right)
        node.key = min_key.key

        node.set_right(delete(node.right, key))

    return node


def search(node, key):
    if key == node.key or node is None:
        return bool(node)
    if key < node.key:
        search(node.left, key)
    elif key > node.key:
        search(node.right, key)


root = None
