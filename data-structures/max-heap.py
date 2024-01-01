class MinHeap:
    def __init__(self):
        self.heap = []
    
    def pop(self):
        if not self.heap: return

        popped = self.heap.pop() 

        if not self.heap: return
    
        self.heap[0] = popped

        currIdx = 0
        leftChildIdx = (currIdx * 2) + 1
        rightChildIdx = (currIdx * 2) + 2

        while leftChildIdx < len(self.heap):
            leftChildVal = self.heap[leftChildIdx]
            rightChildVal = self.heap[rightChildIdx] if rightChildIdx < len(self.heap) else None
            currVal = self.heap[currIdx]
            
            if rightChildVal == None:
                if leftChildVal > currVal:
                    self.__swap(currIdx, leftChildIdx, self.heap)
                return
            
            if leftChildVal > currVal and leftChildVal > rightChildVal:
                self.__swap(currIdx, leftChildIdx, self.heap)
                currIdx = leftChildIdx
            elif rightChildVal > currVal:
                self.__swap(currIdx, rightChildIdx, self.heap)
                currIdx = rightChildIdx
            else:
                return

            leftChildIdx = (currIdx * 2) + 1
            rightChildIdx = (currIdx * 2) + 2

        
    def push(self, value):
        self.heap.append(value)
        currIdx = len(self.heap) - 1
        parentIdx = (currIdx - 1) // 2

        while currIdx > 0:
            if self.heap[parentIdx] >= self.heap[currIdx]:
                return
            
            self.__swap(parentIdx, currIdx, self.heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2
    

    def __swap(self, idx1, idx2, heap):
        temp = heap[idx1]
        heap[idx1] = heap[idx2]
        heap[idx2] = temp 

heap = MinHeap()

heap.push(5)
heap.push(3)
heap.push(1)
heap.push(3)
heap.push(7)
heap.push(9)
heap.pop()

print(heap.heap)


