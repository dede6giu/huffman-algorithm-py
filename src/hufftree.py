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
        self.left: NodeLetter = lchild
        self.right: NodeLetter = rchild
        self.freq: int = int(self.right) + int(self.left)
    
    def _fixfreq(self):
        self.freq = int(self.right) + int(self.left)

    def __int__(self):
        return self.freq

    def set_children(self, lchild, rchild):
        self.left = lchild
        self.right = rchild
        self._fixfreq()