class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"{self.key} : {self.value}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def updateOrInsert(self, key, value):
        if not self.head:
            self.head = Node(key, value)
            self.length += 1
            return 1

        prev = None
        curr = self.head
        while curr:
            
            if curr.key == key:
                curr.value = value
                return 0
            
            prev = curr
            curr = curr.next
        
        prev.next = Node(key, value)
        self.length += 1
        
        return 1

    def get(self, key):
        curr = self.head
        while curr and curr.key != key:
            curr = curr.next
        
        if not curr:
            return
        
        return curr.value
    
    def remove(self, key):
        if not self.head:
            return
        
        prev = None
        curr = self.head
        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        
        if not curr:
            return
        
        if not prev:
            self.head = curr.next
            self.length -= 1
            return 
        
        prev.next = curr.next
        self.length -= 1



    def __repr__(self) -> str:
        keyValues = []

        curr = self.head
        while curr:
            keyValues.append(f"{curr.key}:{curr.value}")
            curr = curr.next

        return "->".join(keyValues)

        


class HashMap:
    def __init__(self):
        self.table = [None] * 20
        self.loadFactor = 0.75
        self.numOfElements = 0
    
    def get(self, key):
        self.__validateKey(key)
        
        key = str(key)
        idx = self.__getHash(key)
        ll = self.table[idx]

        if not ll:
            return

        return ll.get(key) 


    def set(self, key, value):
        self.__validateKey(key)

        key = str(key)
        hash = self.__getHash(key)
        

        if not self.table[hash]:
            ll = LinkedList()
            result = ll.updateOrInsert(key, value)
            self.table[hash] = ll 
        else:
            result = self.table[hash].updateOrInsert(key, value)
        
        self.numOfElements += result
    

        if self.numOfElements / len(self.table) > self.loadFactor:
            self.__expandAndRehash()
    
    def remove(self, key):
        self.__validateKey(key)
        key = str(key)

        idx = self.__getHash(key)
        element = self.table[idx] 
        
        if not element:
            return
        
        if element.length == 1:
            self.table[idx] = None
            self.numOfElements -= 1
            return
        
        self.numOfElements -= 1
        element.remove(key)

    
    def __expandAndRehash(self):
        oldTable = self.table
        newTable = [None] * len(self.table) * 2
        self.numOfElements = 0
        self.table = newTable

        for elem in oldTable:
            if not elem:
                continue

            curr = elem.head
            while curr:
                self.set(curr.key, curr.value)
                curr = curr.next

    def __getHash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
            hash %= len(self.table)
        
        return hash

    def __validateKey(self, key):
        if not isinstance(key, str) and not isinstance(key, int):
            raise Exception('key must be type of string or int')


hashmap = HashMap()

hashmap.set(563, 10)
hashmap.set(356, 20)
hashmap.set(536, "c")
hashmap.set(533, "d")
hashmap.set("apple", "pen")


print(hashmap.get(563))
print(hashmap.get(356))
print(hashmap.get(536))
print(hashmap.get("apple"))

hashmap.remove(563)
print(hashmap.table)