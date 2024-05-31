
# Create a list of the first 10 positive integers. Write a for loop that calculates 
#and prints the sum of all numbers in the list.
num=[1,2,3,4,5,6,7,8,9,10]
print(num)
sum=0
for i in num:
    sum=sum+i
    print(sum)


    #Create a list of your five favorite movies. Write a for loop that prints each movie along with its position in the list (e.g., "1. Inception").
movies=['Ram Laxman','Bad Boy','Lucifer','Tiger','The Kings Man']
for i in range(len(movies)):
    print(f'{i+1}.{movies[i]}')


    #Given a list of strings representing decimal numbers (e.g., ['1.1', '2.2', '3.3']), write a for loop that converts each string to a float, doubles the value, and prints the result.
list=["2.2","6.5","10.6","12.5"]
for i in range(len(list)):
    double=float(list[i])*2
    print(double)




    #Create a list of numbers from 1 to 20. Write a for loop that iterates through the list, converts each number to a string, and creates a new list with these string values. Print the new list.
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(len(list)):
    string=str(list[i])
    print(string)
    list.append(string)
print(list)


#WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name starts with ‘a’ or ‘A’
name=[]
list=[]
for i in range(10):
    names=(input("Enter the name"))
    name.append(names)
    if(name[i][0]=="a" or name[i][0]=="A"):
        list.insert(i,names)
print(list)


#⁠WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name ends with ‘a’ or ‘A’
name=[]
list=[]
for i in range(10):
    names=(input("Enter the name"))
    name.append(names)
    if(name[i][-1]=="a" or name[i][-1]=="A"):
        list.insert(i,names)
print(list)



