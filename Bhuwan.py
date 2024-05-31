#1.Create a list of the first 10 positive integers. Write a for loop that calculates and prints the sum of all numbers in the list.

Number=list(range(1,11))
Sum=0
for i in Number:
    Sum += i
    print("The Sum of each number:",Sum)


#2.Create a list of your five favorite movies. Write a for loop that prints each movie along with its position in the list (e.g., "1. Inception").

Movie=["K.G.F","3-idiots","Sanju","Avenger-infinity war","Lappata Ladies"]
for i, Movie in enumerate(Movie):
    print(f"{i+1}. {Movie}")


#3.Given a list of strings representing decimal numbers (e.g., ['1.1', '2.2', '3.3']), write a for loop that converts each string to a float, doubles the value, and prints the result.

list=["1.1","2.2","3.3","4.4","5.5","6.6","7.7","8.8","9.9","10.10"]
multiple=0
for string in list:
    floatvalue=float(string)
    multiple=floatvalue*floatvalue
    print(multiple)


#4.Create a list of numbers from 1 to 20. Write a for loop that iterates through the list, converts each number to a string, and creates a new list with these string values. Print the new list.

list=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
String=[]
for num in list:
    stringvalue=str(num)
    String.append(stringvalue)
print(String)


#5. ⁠WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name starts with ‘a’ or ‘A’

Name=[]
for i in range(10):
    User=input("Enter the Name: ")
    Name.append(User)
print("Name of Users starts with 'a' or 'A'")
for i in Name:
    if(i[0]=='a' or i[0]=='A'):
        print(i)
    else:
        print()


#6. ⁠WAP that asks 10 user with their name and store them in a list. Print the name of only those users whose name ends with ‘a’ or ‘A’

Name=[]
for i in range(10):
    User=input("Enter the Name: ")
    Name.append(User)
print("Name of Users  with ends'a' or 'A'")
for i in Name:
    if(i[-1]=='a' or i[-1]=='A'):
        print(i)
    else:
        print()