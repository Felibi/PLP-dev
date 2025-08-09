listA = [1, 2, 3, 4, 5]
listB = [6, 7, 8, 9, 10]
languages = ['pigin', 'íjaw', 'english', 'anang', 'hausa', 'igbo', 'ibibio']
#index  0, 1, 2, 3, 4

print(listA[0])                 #outputs 1, the first element
print(listA)                    #outputs the entire list
print(listA[-1])                #outputs 5, the last element
print(listA[1:3])               #outputs [2, 3], elements from index 1 to 2
print(listA[-3:])               #outputs [3, 4, 5], last three elements
print(listA[:])                 #outputs [1, 2, 15, 4, 5, 6], all elements

len(listA)                      #outputs 5, the number of elements in the list
listA[2] = 15                   #changes the third element to 15
listA.append(6)                 #adds 6 to the end of the list
listA.insert(len(listA), 7)     #inserts 7 at the end of the list

listA.extend(listB)             #adds multiple elements to the end of the list- adds element of another list
listA.count(1)                  #counts how many times 1 appears in the list
listA.pop(4)                    #removes the element at index 4
del listA[0]                    #deletes the first element of the list
del languages[4]              #deletes the fifth element of the languages list
del listB[-1]                  #deletes the last element of listB
languages.remove('igbo')         #removes 'igbo' from the languages list

for item in listA:              #iterates through the list
    print(item)                 #prints each item in the list on a new line

numbers = [number*number for number in range(1, 5)]  #creates a new list with squares of numbers from 1 to 5
print(numbers)                  #outputs the new list with squares
num = [number*number for number in range(1, 20)]  #creates a new list with squares of numbers from 1 to 20
print(num)                     #outputs the new list with squares
