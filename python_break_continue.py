# how to use the  break statement
int_list = [1,5,7,8,19,13,17,3]

# Find the even value in the given list

for num in int_list:
    if(num%2==0):
        print("this  is even", num)
        break


# how to use continue keyboard?
# print the numbers from for loop and start thrm from value 1
# but print values on terminal if number is greater than 10

for num in range(1,21):
    if(num<=10):
        continue
    
    print(num)
    