# list basics and program
"""
By using list we store many values like an
array, and it has many operations.

mass = [1, 2, 3, 4, 5, 6]
print(mass)
print(type(mass))
a = []
NthValue = int(input("enter the Nth value"))
for i in range(NthValue):
    num = int(input("enter num"+str(i+1)))
    a.append(num)
print(a)
sum0 = 0
for i in a:
    sum0 = sum0 + i
print(sum0)
"""
"""
# FINDING CUBE OF A NUMBER
cube = []
integer = int(input("Enter the integer value"))
for i in range(integer):
    ip = int(input("Enter the num "+str(i+1)))
    cube.append(ip)
print(cube)
for i in cube:
    hy = i*i*i
    print("the cube value is " + str(hy) + " of a number " + str(i))
"""
naan = [1, 25, 56, 23.4, "naan"]
print(naan)
"""
append is used to add the values in the list
The syntax : 
      variableName.append(any data type value)
"""
naan.append(True)
naan.append(25)
print(naan)
"""
insert is used to add the values in a particular location
address from the list.
Syntax :
    variableName.insert(address value , any data type value)
"""
naan.insert(0, 11)
print(naan)
"""
pop is used to remove the value from the list 
Syntax:
       variableName.pop(address value)
"""
naan.pop(0)
print(naan)
naan.pop()
print(naan)
"""
sri = []
thiru = []
for i in range(1, 101):
    if 30 <= i <= 39:
        continue
    if i % 2 == 0:
        sri.append(i)
    else:
        thiru.append(i)
print(sri)
print(thiru)
print(len(thiru))
print(len(sri))
"""
naan = []
n = int(input("enter the number of digits: "))
k = int(input("Enter the value:"))
for i in range(0, n):
    b = k % 10
    naan.append(b)
    k = k/10
print("The values are:")
print("the last digit:", naan[0])
print("The first digit:", int(naan[n-1]))
original_array = [1, 2, 3, 4, 5]

# Using inbuilt method in Python
reversed_array = list(reversed(original_array))

# Print the reversed array
print(reversed_array)
sri = []
siva = []
for i in range(1, 101):
    if (i % 5 == 0 and i % 11 == 0) and i % 7 != 0:  # condition for find a number divide by 5, 11 not a 7
        sri.append(i)
        for j in range(1, i+1):
            if i % j == 0:
                siva.append(j)
print(sri)
print(siva)
def kthsmallest(ara, n, k):
    ara.sort()

    return ara[k-1]


arr = [12, 3, 5, 7, 19]
N = len(arr)
K = 2
print("K'th smallest element is", kthsmallest(arr, N, K))
