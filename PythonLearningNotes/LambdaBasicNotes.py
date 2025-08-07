"""
Below is the basic of lambda function where 
"""
no = lambda x: x

print(no(3))

"""
Sum with two variables using lambda 
"""
sumtwo = lambda x, y: x+y

print(sumtwo(3,4))

"""lambda function sorting in list """

ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids))
# output: ['id1', 'id100', 'id2', 'id22', 'id3', 'id30']

# now sorting using digit after id? How you will do it?
print(sorted(ids, key=lambda x: int(x[2:])))
# output -> ['id1', 'id2', 'id3', 'id22', 'id30', 'id100']

"""
Sorting in lambda function in dictionary
"""

dict = {"abc": 2, "pqr" : 1, "hdf": 3, "adm":1}
sortedDict = sorted(dict.items(), key=lambda x:(x[0], x[1]))
print(sortedDict)
# output -> [('abc', 2), ('adm', 1), ('hdf', 3), ('pqr', 1)]

sortedDict = sorted(dict.items(), key=lambda x:(x[1], x[0]))
print(sortedDict)
# output -> [('adm', 1), ('pqr', 1), ('abc', 2), ('hdf', 3)]

sortedDict = sorted(dict.items(), key=lambda x:(-x[1], x[0]))
print(sortedDict)
# output -> [('hdf', 3), ('abc', 2), ('adm', 1), ('pqr', 1)]

mySet = {"abc", "adm", "hdf"}
sortedDict = sorted(mySet, key=lambda x:(-dict[x], x))
print(sortedDict)
#Output will be reversed sorted available item in the set 
# Output : ['hdf', 'abc', 'adm']