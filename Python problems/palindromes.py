def palindromes(word):
    return word == word[::-1]
print(palindromes("racecar"))
print(palindromes("rac"))
