def unique(word):
    words = {}
    for i in range(0,len(word)):
        for j in range(i+1,len(word)):
            if word[i] == word[j]:
                return False        
    return True
def uniques(word):
    words = {}
    for i in range(0,len(word)):
        if word[i] in words:
            return False
        elif word[i] not in words:
            words[word[i]] = 1     
    return True
# print(unique("derickk"))
print(uniques("firretruck"))
print(unique("firretruck"))

def reverse(word):
    return word[::-1]

def removedups(word):  
    
    return  
