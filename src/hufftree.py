class NodeLetter:
    def __init__(self, frequency: int, character: str):
        self.freq: int = frequency
        self.char: str = character
    
    def __int__(self):
        return self.freq
    
    def __str__(self):
        return self.char

class HuffTree:
    def __init__(self, *, rchild=None, lchild=None):
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