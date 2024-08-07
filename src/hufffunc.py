from hufftree import HuffTree

def create_hufftree(node1, node2):
    if node1 < node2:
        return HuffTree(lchild=node1, rchild=node2)
    else:
        return HuffTree(lchild=node2, rchild=node1)