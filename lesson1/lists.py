myList=["A","B","C"]
print("The Elements are: "+str(myList) + "\n")  #printing the list elements

myList2=["Apple",5,True]  #you can have different types of data in a list
print("The second element of the multi-type list is: "+str(myList2[1]) + "\n")  #accessing the second element of the list using its index (index starts from 0)

myList3=["Hello","Hello","Hello"]  #you can have duplicate values in a list
print("the iterated values in the iterate-list are: " +str(myList3)+"\n")

myList4=["A","B","C","D","E"]
print("The last Element of the list is: "+myList4[4] )  #accessing the any element of the list using its index (index starts from 0)
print("The last Element of the list with negative indexing is: "+myList4[-1] )  #accessing the last element of the list using negative indexing

counter=len(myList4)
print("The number of the elements are: "+str(counter) + "\n")  #counting the number of elements in the list


# for element in myList2:  #iterating through the list using a for loop

    # print("The element is: "+str(element))