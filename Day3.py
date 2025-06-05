courses=['History','Math','Physics','Compsci']
print(courses[3]) #PRINTING ELEMENTS
print(courses[0:2]) #include 0 notinclude 2
print(courses[2:]) #all these called slicing
#list methods

#adding item
courses.append('Art')
print(courses)

#inserting to specific place
courses.insert(0,'Social')
print(courses)

#Extend for adding multiple values
courses2=['Art','Education']
courses.extend(courses2)
print(courses)

#Removing Values
courses.remove('Math')
print(courses)

#Removing Last Value
courses.pop()
print(courses)

#reversing
courses.reverse()
print(courses)

#sorting
courses.sort()

#sorting in asc or desc
nums=[1,3,5,7,8]
nums.sort(reverse=True) #for asc no value in osrt 
print(nums)

#to get vresult without changing base
sorted_courses=sorted(courses)
print(sorted_courses)


#min,max
print(min(nums))
print(max(nums))
print(sum(nums))

#to find the index
print(courses.index('Art'))

#to check for value
print('Art' in courses)


#to print every items
for item in courses:
    print(item)


#to get index also with value
for index,course in enumerate(courses):
    print(index,course)

#to converrt to string

course_str='-'.join(courses)
print(course_str)

#to split

new=course_str.split('-')
print(new)


#TUPLES
tuple1=('Art','Comp','Math')
tuple2=tuple1

#SETS
#unordered values without duplicates

cs_courses={'History','Art','Math'}

#checking shared values
arts={'Art','Math'}
print(cs_courses.intersection(arts))
print(cs_courses.union(arts))


#Dictionary

d={"a":12,"b":23,"c":34}
print(d)
print(d["a"])  #Accessring Elements
d["d"]=45      #Inserting new element
print(d)
del(d["a"])
print(d)        #deleting elements

#to print all
for key in d:
    print(key,d[key]) #items() returns all key value pair


#Challenge - Create and inventroy file and do some operations

inventory={"Pump":{"Qty":5,"Unit Price":100},
 "Motor":{"Qty":10,"Unit Price":50},
 "Seal":{"Qty":30,"Unit Price":200}}
print(inventory)                                #Created inventory dictionary and assigned values

for item,detail in inventory.items():
    print(f"item - {item}, Qty -{detail['Qty']}, Unit price - {detail['Unit Price']} Total Value-{detail['Qty']*detail['Unit Price']}")  # To view all the items

print('Air' in inventory)                       #Checking if product exists


inp=input("Enter Product Type: ")
if inp in inventory:
    print(f"Product :{inp} Qty : {inventory[inp]['Qty']}, Unit Price: {inventory[inp]['Unit Price']}")
else:
    print("Item not exists")        #taking an input from user and if that exists in the dictionary relevant details printing

#making it more cleaner

item_data=inventory[inp] 
Qaty=item_data['Qty']
UnitPrice=item_data['Unit Price']
Total=Qaty*UnitPrice
inp=input("Enter Product Type: ")
if inp in inventory:
    print(f"Product :{inp} Qty : {Qaty}, Unit Price: {UnitPrice}")
else:
    print("Item not exists")

#Adding another item after taking inputs from user
UserProduct=input("Enter product to be added: ")
UserQty=input("Enter Qaty: ")
Uerprice=input("Enter Price: ")
inventory[UserProduct]={"Qty":UserQty,"Unit Price":Uerprice}
print(inventory)


#Changing the Qty of Pump to 9

inventory['Pump']['Qty']=9
print(inventory)

#After issuing some Quantity updating reducing that value from Stock
Issued=int(input("Enter Issued: "))
Product=input("Enter Product: ")
inventory[Product]['Qty']-=Issued
print(inventory)


#deleting any value
popped=inventory.pop("Pump")
print(popped)

