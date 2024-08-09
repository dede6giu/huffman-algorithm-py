from typing import Any

class PriorityQueue:
    def __init__(self,
                 *,
                 smaller: bool = True):
        self.queue: list[tuple[Any, int]] = []
        self.lt: bool = smaller
    
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item: tuple[Any, int]):
        if self.lt:
            for i in range(len(self.queue)):
                if item[1] < self.queue[i][1]:
                    self.queue.insert(i, item)
                    return
            else:
                self.queue.append(item)
                return
        else:
            for i in range(len(self.queue)):
                if item[1] > self.queue[i][1]:
                    self.queue.insert(i, item)
                    return
            else:
                self.queue.append(item)
                return
    
    def dequeue(self):
        return self.queue.pop(0)[0]