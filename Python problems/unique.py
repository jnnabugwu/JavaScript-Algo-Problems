def unique(word):
    for i in range(0,len(word)):
        for j in range(i+1,len(word)):
            if word[i] == word[j]:
                return False        
    return True
# print(unique("derickk"))
# print(unique("firetruck"))

def reverse(word):
    return word[::-1]

def removedups(word):  
    
    return  
