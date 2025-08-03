#str = input("ban-kai :")
#print(" bankai length is",len(str))
#age = 20
#if(age<18):
 #   print("get going kid")
#elif ( age>25):
 #   print(" old hag")
#else:
 #   print("welcome sweetie")


#### WAP to find greatest among 3 numbers
"""
n1 = int(input("enter a number:"))
n2 = int(input("enter a number:"))
n3 = int(input("enter a number:"))
if(n1>=n2 and n2>=n3):
    print("number 1 is the largest",n1)
elif(n2 >= n1 and n2>= n3):
    print("n2 is the largest")
else:
    print(" n3 is the largest",n3) """

#marks = [ 12,34,43,23,45]
#print(len(marks))
"""str=("hello")
str1=str.replace("hello","hi")
print(len(str1))"""
"""marks=[12,23,32,12,43]
marks.append(5)
marks.sort(reverse=True)
print(marks)"""

"""#### WAP to user input tupple
m1=input("enter fav movie 1:")
m2=input("enter fav movie 2:")
m3=input("enter fav movie 3:")
l=list[m1,m2,m3]
print(l)"""

#### WAP to check if list contains palindrome of elements
"""list1= [ 121,"aaaa","racecar",1331]
copied_list= list1.copy()
copied_list.reverse()
if( list1==copied_list):
    print("is palindromic list")
else:
    print("not palindrome")"""

"""############################# dictionaries
info = {
    "name": "AMIT",
    "marks":{
        "physics":0,
        "maths":0
    }
}
print(info)
print(type(info))
info["marks"]["physics"]=90
print(info)
new_info ={ "city":"karakura"}
info.update(new_info)
print(info) """
################################ ##############SETS
"""info = set()
info.add(24)
info.add(21)
print (info)

print (type(info))
print(info.pop())
print (info)"""

#Q1
"""dictionary={
    "table":["furniture","list"],
    "cat":"small animal"
}
print(dictionary)"""
#Q2
"""info={1,2,3,4,5,5,4,4,4,2,3,1,3,2,1,1,2,5}
print(len(info))"""
#Q3
"""dictionary={}
x= input("subject   ")
y= int(input(x  ,  ))
dictionary.update({x:y})
x= input("subject   ")
y= int(input(x  ,  ))
dictionary.update({x:y})
x= input("subject    ")
y= int(input(x  ,  ))
dictionary.update({x:y})
print(dictionary)"""

########################################LOOPS
'''i=100
while i>=1:
    print(i)
    i-=1'''

"""n=int(input("enter"))
i=1
while i<=10:
    
    print(n*i)
    i+=1"""

#Q4
"""nums=(1,4,9,16,25,36,49,64,81,100)
x= int(input("enter number to be searched "))
i=0  #iterate initialisation
while i<len(nums):
    if(nums[i]==x):
        print("found")
        break
    else :
        print("not found")
    i+=1 
    print("end of loop)"""

#Q5
"""nums=(1,4,9,16,25,36,49,64,81,100)
x= int(input("enter number to be searched "))
for num in nums:
    if(num==x):
        print("found the number")
        break
    print(num)
else:
    print("END")"""
#Q6
"""x=int(input("enter the number"))
for i in range(x,x*10+1,x):
    print(i)"""
#Q7
# sum of n numbers
"""x=int(input("enter the number"))
i=0
sum=0
while i< x:
    i+=1
    sum+=i

print("sum is: ",sum)"""
#Q8
# factorial
"""x=int(input("enter the number"))
i=1
fact=1
for i in range(i,x+1):
    fact*=i
    print(i)

print("factorial is: ",fact)"""

########################################### FUNCTIONS
#Q1
"""def calc_average(a,b,c):
    sum=a+b+c
    print(sum/3)

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))

calc_average(a,b,c)"""

#Q2 length of list
"""def calc_length(my_list):
    print(len(my_list))

n= int(input("enter the number of list components:"))
i=0
my_list =[]
for i in range(n):
    my_list.append(int(input(f"enter the elemnts,{i}")))

calc_length(my_list)"""

"""colours= ("red","black","white")
print(colours)

def print_list( list):
    for item in list:
        print(item, end=" ")


print_list(colours)"""

#Q2 factorial
"""def fact( n):
    i=1
    fac=1
    for i in range(1,n+1):
        fac*=i
        
    print(fac)

n= int(input("enter the number whiose factorial is needed:"))
fact(n)"""

#Q3 USD to INR converter******************
"""
def USD_to(x):
    r=x*85
    print("Rs",r)

def INR_to(x):
    d=x/85
    print("$",d)

print(" CHOOSE 'a' to convert from USD to INR")
print(" CHOOSE 'b' to convert from INR to USD")

command =input("MENTION your choice a/b : ")

x=int(input("Enter the amount: "))

match command:
    case "a":
        USD_to(x)

    case "b":
        INR_to(x)


print("THANK YOU")"""

###########################RECURSIONS
#Q4 sumof

"""def sumof(n):
    if(n==0):
        return 0
    
    return sumof(n-1) + n

sun= sumof(10)

print(sun)"""
#Q5 print_list
"""def print_list(list,i=0):
    if(i== len(list)):
        return
    print(list[i])
    print_list(list,i+1)

n=int(input("enter the maximum number of items: "))
my_list=[]
for i in range(n):
    my_list.append(input("enter the elements: "))

print_list(my_list)"""

########################### FILE I/O

"""f= open("lrn.txt","w")

f.write("\n konichiwa!")

f.close()"""

# using with syntax

"""with open ("lrn.txt","r+") as f:
    data=f.read()
    print(data)

with open ("lrn.txt","a") as f:
    f.write(" minna \n")"""

# deleting a file

"""f = open("select.txt","w")
f.close()

import os
os.remove("lrn.txt")"""

###Q1 create file and write some texts 2) replace the words with different words  3) search for a specific word
"""with open (" quest.txt","w") as f:
    f.write("konnichiwa minna ! \n orewa namaewa AMIT desiyo AMIT warui kaizoku oni naru \n gomu gomu nomi") """
"""
with open (" quest.txt","r") as f:
    data=f.read()

new_data=data.replace("akda","AMIT")
print(new_data)"""

"""def line_of():
    word = input("enter the word to be searched :")
    data=True
    line_no=1
    
    with open (" quest.txt ","r") as f:
        while data:
            data = f.readline()
            if(word in data):      #searches the word
                print(line_no)
                return
            line_no +=1

    return -1

print (line_of())"""

######## finding count of even numbers from another file
  
"""with open ("numbers.txt","w") as f:
    f.write("1,2,3,4,5,6,7,8,9,0,13,23,3,4,6453,56,32")"""
### USING BRUTE FORCE
"""
def find_no_even():
    with open ("numbers.txt","r") as f:
        data = f.read()
        print(data)
        num=""
        for i in range(len(data)):
            if(data[i]==","):
                print(int(num))
                num=""
            else:
                num+=data[i]    

find_no_even()"""

####### OPTIMISED WAY

"""def find_no_even():
    count=0
    with open ("numbers.txt","r") as f:
        data = f.read()

        num = data.split(",")
        print(num)               #prints the numbers as a list

        for i in num:             # using a for-loop to verify the even
            if(int(i)%2==0):
                print(i)
                count+=1

    print("total is:",count)
find_no_even()"""

###########################Reverse a Subarray (Basic Array Reversal)
