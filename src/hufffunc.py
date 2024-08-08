from hufftree import HuffTree
from hufftree import NodeLetter
from priorityqueue import PriorityQueue

def create_hufftree(
        node1: HuffTree | NodeLetter, 
        node2: HuffTree | NodeLetter) -> HuffTree:
    if int(node1) < int(node2):
        return HuffTree(lchild=node1, rchild=node2)
    else:
        return HuffTree(lchild=node2, rchild=node1)

def count_unique(text: str) -> dict[str, int]:
    # Finds all unique characters of a text
    # and automatically counts them
    result: dict[str, int] = []
    for i in range(len(text)):
        if result.get(text[i]) == None:
            result[text[i]] = 1
        else:
            result[text[i]] += 1
    return result

def create_pq(text: str) -> PriorityQueue:
    # Creates priority queue of nodes 
    # based on frequency, least first
    chars: dict[str, int] = count_unique(text)
    pq = PriorityQueue()
    for i in chars.keys():
        pq.enqueue((i, chars[i]))
    return pq

def compress_text(text: str):
    ...