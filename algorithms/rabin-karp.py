def isEqual(needle, haystack, windowStart, windowEnd):
    for i in range(windowStart, windowEnd):
        if haystack[i] != needle[i - windowStart]:
            return False
    
    return True


def rabinKarp(needle, haystack):
    if len(needle) > len(haystack):
        return -1

    needleHash = 0
    for char in needle:
        needleHash += ord(char)
    
    windowHash = 0
    for i in range(len(needle)):
        windowHash += ord(haystack[i])

    right = len(needle)
    left = 0

    for i in range(len(haystack) - len(needle)):
        # print(windowHash, needleHash, i)
        if windowHash == needleHash:
            if isEqual(needle, haystack, left, right): return left
  
        
        windowHash -= ord(haystack[left])
        windowHash += ord(haystack[right])

        left += 1
        right += 1
    
    if windowHash == needleHash:
        if isEqual(needle, haystack, left, right): return left

    return -1



needle = "abc"
haystack = "djaskdafnaabcsjdd"


result = rabinKarp(needle, haystack)
print(result)


