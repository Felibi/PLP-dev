tup = (1, 2, 3, 4, 5)   #creates a new tuple named tup with five elements
print(type(tup))        #outputs the variable type, in this case, as Tuple

tup1 = ('Hey', 'You')
print(type(tup1))

tup2 = 'Come', 'Over'
print(type(tup2))

print(tup[2])
print(tup[-2])

# Tuple Methods - Only Two: Count & Index

print(tup.count(2))   
print(tup2.index('Over'))