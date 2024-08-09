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

def enctable_to_str(enctable: dict[str, str]) -> str:
    # Formats an encoded table into a str
    result: str = "{"
    for i in enctable.keys():
        result += f"'{enctable[i]}':'{i}',"
    result = result[:-1]
    result += "}"
    return result

def compress_text(text: str) -> str:
    # Compresses the provided text
    # Returns a str, formatted as "{table}{enctext}"
    charTable: dict[str, int] = count_unique(text)
    tree: HuffTree = create_hufftree(charTable)
    encTable: dict[str, str] = tree.make_encoding_table()
    resultText: str = enctable_to_str(encTable)
    for i in range(len(text)):
        resultText += encTable[text[i]]
    return resultText

def validate_compression(text: str) -> bool:
    # Checks to validate compression
    if text[0] != "{":
        return False
    aux = text.find("'}'") # escaping having '}' present in the table
    if aux == -1:
        tableEnd: int = text.find("}")
    else:
        tableEnd: int = text.find("}", aux+3)
    if tableEnd == -1:
        return False
    size: int = len(text[tableEnd+1:])
    cnt0: int = text.count('0', tableEnd+1)
    cnt1: int = text.count('1', tableEnd+1)
    if size != cnt0 + cnt1:
        return False
    return True

def obtain_denctable_and_text(encStr: str) -> tuple[dict[str, str], str]:
    aux = encStr.find("'}'") # escaping having '}' present in the table
    if aux == -1:
        tableEnd: int = encStr.find("}")
    else:
        tableEnd: int = encStr.find("}", aux+3)
    tableStr: str = encStr[:tableEnd]
    encText: str = encStr[tableEnd+1:]
    sizeTable: int = len(tableStr)
    i: int = 0
    denctable: dict[str, str] = {}
    while i < sizeTable:
        if tableStr[i] == "'":
            i += 1
            aux2 = ""
            while tableStr[i] != "'":
                aux2 += tableStr[i]
                i += 1
            i += 3
            aux = tableStr[i]
            i += 2
            denctable[aux2] = aux
            continue
        i += 1
    return (denctable, encText)

def decompress_text(text: str) -> str:
    # Decompresses the provided text (formatted as "{table}{enctext}")
    # Returns a str, the original text
    if not validate_compression(text):
        raise ValueError("'text' is not a valid compression")
    aux = obtain_denctable_and_text(text)
    dencTable: dict[str, str] = aux[0]
    encText: str = aux[1]
    result: str = ""
    largestEnc: int = 0
    for i in dencTable.keys():
        largestEnc = len(i) if len(i) > largestEnc else largestEnc
    i: int = 0
    sizeEncText: int = len(encText)
    aux = ""
    while i < sizeEncText:
        aux += encText[i]
        if dencTable.get(aux) != None:
            result += dencTable[aux]
            aux = ""
        if len(aux) > largestEnc:
            raise ValueError("'text' is a corrupted compression")
        i += 1
    return result