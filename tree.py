class Tree:
    def __init__(self, root_node, children = []):
        self.root = root
        self.children = children

    def __str__(self):
        pass

class TreeAddr:
    def __init__(self, addr):
        self.addr = addr