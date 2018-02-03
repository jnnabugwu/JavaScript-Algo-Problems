from collections import OrderedDict
years_dict = dict()
years_dict[100] = [1]
years_dict[100].append(2)
years_dict[200] = 2
years_dict[300] = [1]
years_dict[300].append(4)
years_dict[0] = [2,3,4]
print(years_dict)
b =sorted(years_dict.items())
print(b)
for i in range(0,len(b)) :
    print(b[i][1])

