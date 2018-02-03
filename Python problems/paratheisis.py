# Remove the minimum number of invalid parentheses in order to make the 
# input string valid. Return all possible results.

# Note: The input string may contain letters other than the parentheses ( and ).

# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]

def uniplz(array):
    unique = {}
    for i in range(len(array)):
        if array[i] not in unique:
            unique[array[i]] = 1
        elif array[i] in unique:
            unique[array[i]] += 1
    for key in unique:
        if unique[key] == 1:
            return key
    return False
print(uniplz([1,2,3,2,3,1,7,3,4,5,5,4]))
print(uniplz([7,8,2,10,4,2,8,7,9]))
