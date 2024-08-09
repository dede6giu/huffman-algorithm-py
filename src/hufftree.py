class NodeLetter:
    def __init__(self, character: str, frequency: int):
        self.char: str = character
        self.freq: int = frequency
    
    def __int__(self):
        return self.freq
    
    def __str__(self):
        return self.char

class HuffTree:
    def __init__(self, *, lchild=None, rchild=None):
        self.check_children_integrity(lchild, rchild)
        if rchild.freq < lchild.freq:
            rchild, lchild = lchild, rchild
        self.left: NodeLetter | HuffTree = lchild
        self.right: NodeLetter | HuffTree = rchild
        self.freq: int = int(self.right) + int(self.left)
    
    def _fixfreq(self):
        self.freq = int(self.right) + int(self.left)

    def __int__(self):
        return self.freq

    def check_children_integrity(self, left, right) -> None:
        if not ((isinstance(right, NodeLetter) or isinstance(right, HuffTree)) and
                (isinstance(left, NodeLetter) or isinstance(left, HuffTree))):
            raise TypeError("Children are of wrong type, expected NodeLetter or HuffTree")
        return None

    def set_children(self, lchild, rchild):
        self.check_children_integrity(lchild, rchild)
        if rchild.freq < lchild.freq:
            rchild, lchild = lchild, rchild
        self.left = lchild
        self.right = rchild
        self._fixfreq()

    def search_char(self, char: str) -> str:
        # Inneficient. Single character searching only.
        # For encoding, use make_encoding_table() instead
        queue: list[tuple[NodeLetter | HuffTree, str]] = [(self, '')]
        while len(queue) != 0:
            current = queue.pop(0)
            if isinstance(current[0].left, NodeLetter) and current[0].left.char == char:
                return current[1] + '0'
            if isinstance(current[0].right, NodeLetter) and current[0].right.char == char:
                return current[1] + '1'
            
            if isinstance(current[0].left, HuffTree):
                queue.append((current[0].left, current[1] + '0'))
            if isinstance(current[0].right, HuffTree):
                queue.append((current[0].right, current[1] + '1'))
        raise KeyError(f"{char} not in tree")
    
    def make_encoding_table(self) -> dict[str, str]:
        queue: list[tuple[NodeLetter | HuffTree, str]] = [(self, '')]
        result: dict[str, str] = {}
        while len(queue) != 0:
            current = queue.pop(0)
            if isinstance(current[0].left, NodeLetter):
                result[current[0].left.char] = current[1] + '0'
            if isinstance(current[0].right, NodeLetter):
                result[current[0].right.char] = current[1] + '1'
            
            if isinstance(current[0].left, HuffTree):
                queue.append((current[0].left, current[1] + '0'))
            if isinstance(current[0].right, HuffTree):
                queue.append((current[0].right, current[1] + '1'))
        return result