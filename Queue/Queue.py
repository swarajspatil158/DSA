class Queue:
    def __init__(self) -> None:
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)
    def is_empty(self):
        return self.queue == []
    def size(self):
        return len(self.queue)
    def display(self):
        print(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()