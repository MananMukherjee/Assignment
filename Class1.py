#list- an ordered collection of datatypes, mutable(change of data is possible), encloses data in []
list1 = ['monitor', 'printer', 345, True, 478.36] #a list can store diffrent data types(it can be heterogeneous)
#functions associated with list:
list1.append('system')
print(list1) #prints the list with 'system' added as the last element
list1.insert(1, 'system')
print(list1) #prints the list with 'system' inserted at index 1 or the 2nd position from left
del list1[1]
print(list1) #prints the list after deleting the data present at index value 1
list1[2] = 'easy'
print(list1) #prints the list after replacing the element at index 2 with the string 'easy'
del list1
print(list1) #shows that list isn't defined, which means the entire list is deleted

#tuple- an ordered collection of datatypes, immutable(change of data is not possible), encloses data in ()
tuple_1 = (3, 'physics', 'biology', 4.8)
tuple_1.append(5)
tuple_1.insert(1, 10)
del tuple_1[1]
#since it's immutable, appending, inserting, and deletion of individual elements is not possible. But the entire tuple can be deleted at onece
del tuple_1
print(tuple_1) #shows name not defined, meaning tuple is inexistent

#dictionary- key-value pairs, ordered, elcloses data in {}
dict1 = {
  'hot':'cold'
  'positive':'negative'
}
#updation is possible but append function doesn't work
dict1['lock']='key'
print(dict1) #prints the dictionary with lock:key pair as the last element
del dict1['hot'] #deletes key-value pair with key as 'hot'
del dict1 #deletes entire dictionary

#set- unordered collection, uses {}, mutable
set1 = {'A', 'B', 'C', 54} # can be heterogeneous
print(set1) #prints the set elemtents in random order
print(len(set1)) #counts and shows the number of elements in the set
#add function- adds the given data at a random location
set1.add(True)
print(set1) # displays set with True boolean added to it

#slicing using step index- for printing of selectively printing data out of a whole. Makes use of indices of data
str1 = 'concatenation'
#indexing from left to right- c:0,o:1......and from right to left is n:-1, o:-2 etc
print(str1[1:5:3]) #prints alphabets starting from index1 which is o, till index 5(excluding index 5), so output is oa
print(str1[-5:-1]) #prints elements from index -5 that is alphabet 'a', till index -1(excluding it), so ouput is atio 
list2 = ['thing', 'person', 'name', 'place']
print(list2[-1:-4:-2]) #prints leftwards(since negative step of -2 means printing every 2 steps to the left), from index -1 to -4 (excluded). expected output is ['place', 'person']
str3 = 'thisispython'
print(str3[-4:-1]) #if first specified index is at a lower value, then printing occurs rightwards. output = tho
tuple2 = (True, 'nature', 458, 14.6) 
print(tuple2[-3:1]) #since -3 and 1 indices belong to the same element 'nature', everything is sliced off and we get an empty set

