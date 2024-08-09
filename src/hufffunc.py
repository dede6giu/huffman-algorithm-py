from hufftree import HuffTree
from hufftree import NodeLetter
from priorityqueue import PriorityQueue

def create_pq(chars: dict[str, int]) -> PriorityQueue:
    # Creates priority queue of nodes 
    # based on frequency, least first
    pq = PriorityQueue()
    for i in chars.keys():
        pq.enqueue((NodeLetter(i, chars[i]), chars[i]))
    return pq

def create_hufftree(chars: dict[str, int]) -> HuffTree:
    # Creates a hufftree from a table
    # if empty -> empty HuffTree
    #     else -> ready HuffTree
    pq = create_pq(chars)
    if pq.is_empty():
        return HuffTree()
    while len(pq) > 1:
        aux = HuffTree(lchild=pq.dequeue(), rchild=pq.dequeue())
        pq.enqueue((aux, aux.freq))
    return pq.dequeue()

def count_unique(text: str) -> dict[str, int]:
    # Finds all unique characters of a text
    # and automatically counts them
    result: dict[str, int] = {}
    for i in range(len(text)):
        if result.get(text[i]) == None:
            result[text[i]] = 1
        else:
            result[text[i]] += 1
    return result

def create_table_string():
    ...

def compress_text(text: str) -> str:
    charTable: dict[str, int] = count_unique(text)
    tree: HuffTree = create_hufftree(charTable)
    resultText: str = ''

    for i in range(len(text)):
        resultText += tree.search_char(text[i])
    
    return resultText