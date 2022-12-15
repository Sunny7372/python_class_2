# declare empty list
L1 =[]

# insert values in list
L1.append(5)
L1.append(7)
L1.append(8)
print(L1)

# create a list of 1000 numbers start from 1 to 1000
L2 =[]
for num in range(1,1001):
    L2.append(num)
    print(L2)


# How to calculate the length of a list?

length_of_list = len(L1)
print(" length of list :",length_of_list)

# how to check is list are equal to each other
list1 = [1,"sunny",20,"hi"]
list2 =[1,"sunny",20,"hi"]
print("lists are equal??",list1==list2)

list1 = [1,"sunny",20,"hi"]
list2 =[1,"sunny","hi",20]
print("lists are equal??",list1==list2)

# list concat
List4  = [1,2,3,4,5]
List5 = [80,90,100,110]
result = List4 + List5
print(result)

# how to access list value
List6 =[10,15,20,25,30,35]
# print all the elements of giveen list

for num in List6:
    print(num)

# what will happpen??
#print(List6[100])
# ans will be index out of range

List7 =[1,"sunny",1000]
print(List7)
# how to update the list value
# update sunny to adarsh
List7[1] = "adarsh"
print(List7)

# how to print list element using length

for index in range(0,len(List7)):
    print(List7[index])

# Difference between append() and extend()
list9 = [20,30,40]
list10 = ["hi","hello","bye"]
list9.append(list10)
print(" output of append:",list9)
print(" length after append:",len(list9))

list11 = [20,30,40]
list12 =["hii","hello","bye"]
list11.extend(list12)
print(" output of extend:",list11)
print(" length after extend:",len(list11))

# so, the append() combine the whole list as a single element
# means the list inside the list
# ex:- output of append: [20, 30, 40, ['hi', 'hello', 'bye']]

# and the extend function combine the each element
# there will be no list inside the list
# ex:-output of extend: [20, 30, 40, 'hii', 'hello', 'bye']


List8 = [1,2,50,"sunny", [6,6,6],"adarsh"]
print(len(List8)) # what will be the output ??

# List slicing

list13 = [20,30,40,50,60,80,90]
# syntax -> list_name[start:end]

print(list13[0:]) # if we not mention last index by default it will print till last element
print(list13[3:])
print(list13[:])  # by default it will print whole list

# we have to print element till 50
print(list13[0:4]) # last index will be exclusive

print(list13[0: :2]) # 3rd value is for steping

# how to print the last value of the list??

print(list13[len(list13)-1])
print(list13[-1])

# print second last element from the list
print(list13[-2])

# print input list in reverse direction
print(list13[-1 : : -1])


