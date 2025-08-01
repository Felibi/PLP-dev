listA = [1, 2, 3, 4, 5]
#index  0, 1, 2, 3, 4

print(listA[0])                 #outputs 1, the first element
print(listA)                    #outputs the entire list

len(listA)                      #outputs 5, the number of elements in the list
listA[2] = 15                   #changes the third element to 15
listA.append(6)                 #adds 6 to the end of the list
listA.insert(len(listA), 7)     #inserts 7 at the end of the list

listA.extend([8, 9, 10])        #adds multiple elements to the end of the list- adds element of another list
listA.count(1)                  #counts how many times 1 appears in the list
listA.pop(4)                    #removes the element at index 4
del listA[0]                    #deletes the first element of the list

for item in listA:              #iterates through the list
    print(item)                 #prints each item in the list
    