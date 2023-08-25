for a in "Apple":
    print(a)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

mylist = ["Amit", "Kapil", "Anjali"]  
i = 0
while i < len(mylist):
   print(mylist)
   i = i + 1

mylist = ["Amit", "Kapil", "Anjali"]  
i = 0
while i < len(mylist):
   print(mylist[i])
   i = i + 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
   if "a" in x:
      newlist.append(x)
print(newlist)      
newlist.sort()
print(newlist)
newlist.reverse()
print(newlist)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)  

l = 2300
while l > 15:
   print(l)
   if i == 20:
      break
   i += 1

# Warning : Dont try to run this

m = 23
while m > 15:
   print(m)
   if m == 20:
      break
   m  += 1   