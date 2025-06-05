#simple if
number=int(input("Enter a number: "))
if number%2==0:
    print("Number is even")
else:
    print("Number is odd")



#ask user to enetr a dish name and finding which cuisine is the dish

indian=["Samosa","Daal","Naan"]
chinese=["Eggrole","Potsticker","FriedRice"]
italian=["Pizza","Pasta","risottto"]
dish=input("Enter a dish name: ")
if dish in indian:
    print("Indian")
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print("Italian")
else:
    print("Can't recognise")

#for loop
#list if monthly expenses and find out total

expense=[2340,2500,2100,3100,2980]
total=0
for  i in expense:
    total=total+i
print(total)

#range using for

for i in range(1,11):
    print(i)

#in monthly expense example, print month number and expense then in the end print total expense
    
expense=[2340,2500,2100,3100,2980]
total=0
for i in range(len(expense)):
    print('Month:' ,(i+1),'Expense', expense[i])
    total=total+expense[i]
print(total)

#break statement
keyloc="Garage"
locations=["Chair","Garage","Room","Toilet"]
for i in locations:
    if i==keyloc:
        print(f"{keyloc} found in {i}")
        break
    else:
        print("Keyloc not found")

#continue -- to skip operation
# print square of even number
for i in range(1,6):
    if i%2==0:
        print(i*i)
    else:
        continue #skip the value and go for iteration

#print square of odd
for i in range(1,6):
    if i%2==0:
        continue #skip the value and go for iteration
    print(i*i)


#while statement
#print 1 to 5

i=1
while i<5:
    print(i)
    i=i+1

#vending machine

noc=int(input("Enter Numer of candies: "))
i=1
total=10
while i<=noc:
    if i > total:
        break
    print("Candy")
    i+=1
print("Bye")

#Challenge --> Checking a number is prime or not
given=int(input("Enter a number: "))
if given<=1:
    print("The given number is not prime")
else:
    for i in range(2,given):
        if given%i==0:
            print("Not prime")
            break
    else:
            print("The number is prime")

#printing stars
row=int(input("row?: "))
for i in range(1,row+1):
        print("*"*i)