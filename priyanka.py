#1. Create a list of the first 10 positive integers. Write a for loop that calculates and prints the sum of all numbers in the list.
numbers=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range(11):
  sum=sum+i
print(sum) 

#2. Create a list of your five favorite movies. Write a for loop that prints each movie along with its position in the list (e.g., "1. Inception").
movies=["RRR","Pushpa","Bahubali","KGF","Bareliki Barfi"]
for i,movie in enumerate(movies,1):
    print(f"{i}.{movie}")


#3. Given a list of strings representing decimal numbers (e.g., ['1.1', '2.2', '3.3']), write a for loop that converts each string to a float, doubles the value, and prints the result.
list=['1.1','2.2','3.3','4.4','5.5']
double=0
for strToFloat in list:
    floatvalue=float(strToFloat)
    double=floatvalue*floatvalue
    print(double) 

#4. Create a list of numbers from 1 to 20. Write a for loop that iterates through the list, converts each number to a string, and creates a new list with these string values. Print the new list.
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
stringValue=[]
for number in list:
    numToStr=str(number)
    stringValue.append(numToStr)
print(stringValue)



#5. ⁠WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name starts with ‘a’ or ‘A’
namelist=[]

for name in range(10):
    yourname=input("enter your name")
    namelist.append(yourname)
print("name of people begin with 'a' or 'A'")
for name in namelist:
    if(name[0]=='a' or name[0]=='A'):
        print(name)
    else:
        print()  


#6. ⁠WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name ends with ‘a’ or ‘A’
namelist=[]

for name in range(10):
    yourname=input("enter your name")
    namelist.append(yourname)
print("name of people end with 'a' or 'A'")
for name in namelist:
    if(name[-1]=='a' or name[-1]=='A'):
        print(name)
    else:
        print()