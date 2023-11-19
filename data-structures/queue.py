class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            return
        
        node = Node(value)
        self.tail.next = Node(value)
        self.tail = self.tail.next
    
    def dequeue(self):
        if not self.head:
            return
        
        if not self.head.next:
            self.head = None
            self.tail = None
            return
        
        self.head = self.head.next

    def getFirst(self):
        return self.head
    
    def getLast(self):
        return self.tail
    
    def log(self):
        queue = []
        
        currNode = self.head
        while currNode:
            queue.append(str(currNode.value))
            currNode = currNode.next
        
        print("->".join(queue))






queue = Queue()
queue.log()

queue.enqueue(1)
queue.log()

queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.log()

queue.dequeue()
queue.dequeue()

queue.log()


queue.dequeue()
queue.dequeue()

queue.log()

queue.dequeue()
queue.dequeue()