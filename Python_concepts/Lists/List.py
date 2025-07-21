#We are going to study lists today
'''To create a list, you need to enter values in a sqauare bracket. 
    Depending on the type of variable the values are, you may enter them as they are or put them in quotes.
    Numbers are enter without quotes and are separated with a comma;
    Strings however are put in quote and separated with a comma.'''

list = ['Rice','Jollof','Banku']
list #will not display your list, you need to use the print statement before will be display it
print(list) #now it will be printed
list[0] #will not display your list, you need to use the print statement before will be display it
print(list[0])
list[0]= 'waakye' #this will replace the item that was initially at that position
print(list[0])
len(list) #you need to use print before you can veiw it
print(len(list))
print(list)
list = ['Rice', 1] #you can mix variable types
print(list)

# Now we will explore the variou methods that can be used with lists
#append method
list.append(3) #only takes a single argument, you can add to a list, this will add the new value to the end
print(list)
list.append(3) #you can add the same value multiple times
print(list)

#index method
print(list.index(3)) 
'''seems to take multiple arguments. 
It returns the index of the first occurance of the first argument passed into it.
If the arguemets are present in list,
it will return the index of the first argument but ignore the other argument(s).
However if one of the arguments or all are not it the list, it raises an error.'''

#count method
print(list.count(3)) 
'''takes only one argument, and returns the number of times it occurs, after you as it to print.'''

#clear method
list.clear() #does not take an argument and it clears every thing in a list
print(list)

#copy method
new_list = list.copy() #takes no argument, and copys a list to another list
print(new_list)

#extend method
''' list.extend(5), will have to look into this'''

#insert method
list.insert(0,6) 
'''it takes the index you want your new value to be at and your new value as arguments respectively.
Then prints your new value infront of the value that had that index.
Making the new value take the specified index. 
In turn causing all the values after the new value to shifting their indexes by one''' 
print(list)

