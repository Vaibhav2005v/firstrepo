'''
print("hello")
print("world")
print("hello coders")
n= "sharan"
age= 22
print(n)
print(age)
print(type(n))
print(type(age))
#boolian define  true and false
age =16
is_adult= False

name= input("what is your name?  ")
print("hello", name)
old_age= input("enter your old age: ")
int(old_age)
new_age = int(old_age) +2
print(new_age)

first = input("enter first number = ")
second = input("enter second number = ")
sum = int(first) + int(second)
print(sum)

name = "tony stark"
#to conert lower to upper case and vice versa
print(name.upper())
print(name.lower())

#to find operation with index
print(name.find('s'))
print(name.find('S'))
#to find in terms of boolian
print("tony" in name)
print("iron" in name)
#to replace
print(name.replace("tony stark", "ironman"))
##here in (name.replace("1","2"))   1=string to be changed, 2=string which will replace it

#operators
#to study operator and operator precedence go to link "https://www.google.com/url?sa=i&url=https%3A%2F%2Fmicromerits.com%2Flesson-2-operators-in-python%2F&psig=AOvVaw0qXRPLBTMLNlYsfzIophh5&ust=1711259800933000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCJCmr-7ZiYUDFQAAAAAdAAAAABAD"
# + and - operator give normal add and sub values
print(5 // 2) #to remove the float value in  python in divide use double slash'//' 
print(5%2) # it give the remainder of a value
print(5**2) #used for doing power values for example 2^3 etc here it means 5^2
#i= 5
#i= i+2 #(here this is minimized and is equal to: i+ =2)
result = (2+3/5)
sr= (2+3)/5
print(result) #here the result is calculated according to operator precedence
print(sr) #here the result will be done by basic maths terms

##comparision operator these operator return boolian value
print(3<2)
print(3>=2)
print(3==2) # to check the value equality use "==" operator
print(3!=2) # here "!=" is operator used for proving they arent equal

## logic operator out of given two condition  which is right one and give output accordingly
print(2>3 or 2>1)
print(2<4 and 3>1)
print(not 2>3) #here not will convert the result to their opposites

#if else equations

age = int(input("enter your age:"))
if age>= 18:
    print("the subject is adult")
    print("subject can vote")
    print("thankyou for voting")
elif age <18 and age >3:
    print("subject is not adult they are school attendee")
    print("head back, thankyou")
else:
    print("subject is a new born or a child")

#build a calculator using python
    
first= int(input("enter your first number = "))
second= int(input("enter your second number = "))
operator= input("enter your operator(+,-,/,%.*)= ")

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
elif operator == "*":
    print(first * second)
else:
    print("no operations are held")

# range is a list of number until the limit reaches the give number and it is upto (n-1) if n=input no.

print(1)
print(9)

# for repetitive nuber we use loop

i=1
while i <= 5:
    print(i)
    i= i+1 #where this statement dont exist then the loop is infinite loop and it is wrong
'''
# to print star pattern
i= 1 # here i = 1 is refered as the stzrting point
while i <= 5:
    print(i * "*") #here * help writing string a given times
    i= i+1

#for loop

for item in range(5):
    print(item + 1)


#lists 

marks= [95,98,97] #to write list "[]" these brackets are used
print(marks)
print(marks[0]) 
# to print a certain marks write its position where first term from left side is considered as '0th' the second as '1st' 
#from last the term no. start from '-1'
print(marks[-2])
#to make a new list from a given list use:
print(marks[1:3]) #the list is taken till number before third term

#to use loop on particular object from list

for score in marks:
    print(score)

#for addition in the last
marks.append(99)
print(marks)

# to insert some thing in between a list
marks.insert(0,99) # where 0 is posi and 99 is item to be added
print(marks)

# to check
print(99 in marks)
print(93 in marks)

#to find length
print(len(marks))

#to iterate using while loop

i=0
while i< len(marks):
    print(marks[i])
    i= i+1

# to clear a list
marks.clear()
print(marks)

#break and continue
students = ["ram", "shyam", "kishan", "radha", "radhika"]
#to print till radha name 
for students in students:
    if students == "radha":
        break
    print(students)
# to remove a single item from the list
for students in students:
    if students == "kishan":
        continue
    print(students)