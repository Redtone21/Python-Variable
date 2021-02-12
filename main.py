'''
Text type (String)
'''

# s = "This is a single line string"
# print(s)
# print(type(s))

# ========================

# s = '''this is a multiline'
# string example'''
# print(s)

# ========================

# find a character by index 
# s = 'string sample'
# print(s[5])

# slicing
# s = 'string sample'
# print(s[1:6])

# ========================
# immutable
  
# s = 'string sample'
# s[2] = 'o'
# print(s)
  
'''
Numeric type (Integer, Float, Complex)
'''
# x = 123456787654 
# print(type(x))

# accurate up to 15-16 decimal places 
# x = 0.123345678987654321
# print(type(x))
# print(x)
 
# x = 1+2j
# print(type(x))

'''
Sequence type (List, Tuple, Range)
'''
# homogeneous
# List
# x = [10,2.5, 'hello']
# print(x[2])
# print(x[1:3])

# # mutable 
# x[2] = 'Python'
# print(x)

# Tuple 
# heterogeneous
# tuple = ()

# ========================

# both of examples below are type tuples, without comma makes it a string.
# tuple = ["hello")
# tuple = "hello",
# print(type(tuple))

# ========================

# tuple = ("cat", [4,3,2], (1,2,3))
# print(type(tuple[2]))

# ========================

# immutable

# tuple = ("cat", [4,3,2], (1,2,3))
# tuple[2] = 10
# print(tuple)

# ========================

#  Range
# x = range(30)
# for n in x:
#   print(n)
 
'''
Mapping Type (Dictionary)
'''

# dict = {}
# print(type(dict))

# ========================

# dict = {'name': 'Kingsley', 'age':37}
# print(dict['age'])
# print(dict.get('name'))

# dict['age'] = 26
# print(dict)

'''
Set Type
'''

# empty set having set = {} is an empty dict
# set = set()
# print(type(set))

# ========================

# mixed data types ( all immutable)

# set = {3.2, "hi", (1,2,3)}
# print(type (set))
# TypeError: 'set' object is not subscriptable
# print(set[0])

# ========================
# no duplicates 

# set = {3.2, "hi", (1,2,3), "hi"}
# print(set)

# ========================

# cannot have mutable (list) in a set
# set = {3.2, "hi", (1,2,3), [1,2,3]}
# unhashable type: 'list'
# print(set)

'''
Boolean Type (True or False)
'''

# print(type(True))

# boolean as numbers 
# print(True ==1)
# print(False == 0)

# not boolean operator 
# print(True + True)
# print(not False)

# and boolean operator 
# print(True and False)
# print(True and True)
# print(False and False)

# or boolean operator 
# print (True or False)
# print (True or True) 
# print (False or False)


