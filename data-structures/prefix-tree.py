class Node:
    def __init__(self):
        self.children = {}
        self.isEndOfTheWord = False

class PrefixTree:
    def __init__(self):
        self.root = Node() 
    
    def insert(self, word):
        currNode = self.root
        
        for char in word:
            if char not in currNode.children: 
                currNode.children[char] = Node()

            currNode = currNode.children[char]

        currNode.isEndOfTheWord = True

        
    def searchWords(self, keyWord):
        parentNode = self.root

        for char in keyWord:
            if char in parentNode.children:
                parentNode = parentNode.children[char]
            else:
                parentNode = None
                break
        
        result = []

        if parentNode:
            result = self.getAllWords(parentNode)
            for i in range(len(result)):
                result[i] = keyWord + result[i]
        
        if parentNode.isEndOfTheWord:
            result.append(keyWord)
        
        return result


    def getAllWords(self, currNode = None, currWord = []):
        if currNode == None:
            currNode = self.root
        
        result = []
        children = currNode.children

        for char in children:
            currWord.append(char)

            if children[char].isEndOfTheWord:
                result.append("".join(currWord))
            
            subResults = self.getAllWords(children[char], currWord)

            for subResult in subResults:
                result.append(subResult)
            
            currWord.pop()
    
        return result
    


    # here i am deleting using bottom up recursion
    # we could have done this iteratively if we had references from children to parent
    def delete(self, word, currIdx = 0, currNode = None):
        if not currNode:
            currNode = self.root

        if currIdx == len(word):
            if len(currNode.children):
                currNode.isEndOfTheWord = False
                return False
            return True
            

        char = word[currIdx]
        
        if char not in currNode.children:
            return False
        
        shouldDeleteChild = self.delete(word, currIdx + 1, currNode.children[char])  
        
        if not shouldDeleteChild:
            return False

        del currNode.children[char]

        if currNode.isEndOfTheWord or len(currNode.children):
            return False
        
        return True



pTree = PrefixTree()
pTree.insert("cat")
pTree.insert("car")
pTree.insert("carpet")
pTree.insert("banana")

allWords = pTree.getAllWords()
print(allWords)

searchResult = pTree.searchWords("ca")
print(searchResult)


pTree.delete('cat')

searchResult = pTree.searchWords("ca")
print(searchResult)


