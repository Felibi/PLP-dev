setStudID = {'csi001', 'csi002', 'csi003', 'csi004', 'csi005'} #creates a set of student IDs
print(setStudID)                    #outputs the set of student IDs

setStaffID = {'felb.b0001', 'felb.b0002', 'felb.b0003', 'felb.b0004', 'felb.b0005'} #creates a set of staff IDs
print(setStaffID)                   #outputs the set of staff IDs

mixedSet = {'bread', 484, 'milk', 3.14, 'eggs'}  #creates a mixed set with different data types
print(mixedSet)                     #outputs the mixed set

emptySet = set()                    #creates an empty set
print(emptySet)                     #outputs the empty set

emptyDict = {}                      #creates an empty dictionary
print(emptyDict)                    #outputs the empty dictionary

setStaffID.add('felb.b0006')       #adds a new staff ID to the set
print(setStaffID)                   #outputs the updated set of staff IDs

mixedSet.update(setStudID)          #adds the set of student IDs to the mixed set
print(mixedSet)                     #outputs the updated mixed set

mixedSet.remove('bread')            #removes 'bread' from the mixed set
print(mixedSet)                     #outputs the mixed set after removal

for item in setStudID:             #iterates through the set of student IDs
    print(item)                    #prints each student ID on a new line

len(setStaffID)                     #outputs the number of elements in the set of staff IDs

print(mixedSet & setStudID)         #outputs the intersection of mixedSet and setStudID
print(mixedSet | setStudID)         #outputs the union of mixedSet and setStudID
print(mixedSet - setStudID)         #outputs the difference of mixedSet and setStudID
print(mixedSet ^ setStudID)         #outputs the symmetric difference of mixedSet and setStudID
print(setStudID - mixedSet)         #outputs the difference of setStudID and mixedSet

setA = {1, 2, 3, 4, 5}
setB = {0, 3, 9, 7, 8, 11}

if setA == setB:
    print('A = B')
else:
    print('notEqual')

# LEARN TO WORK WITH OTHER METHOD OF A SET
# A set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements.
# Sets are useful for membership testing and eliminating duplicate entries.
# They do not support indexing, slicing, or other sequence-like behavior.
# They do not accept duplicate elements.
