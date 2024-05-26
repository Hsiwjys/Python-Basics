"""
create a program for a series of 1, 2, 4, 7, ......., N.
ans:
     Term n =Term n−1+n
     Term n−1 --> previous term
     n --> Nth value for that particular loop
"""
n = int(input("Enter the Nth value:"))
nsd = [n]
nsd[0] = 1
for i in range(1, n):
    i = nsd[i-1]+i
    nsd.append(i)
print("the series is :", nsd)
"""
Finding the longest palindrome in an arrays
input: 	1, 121, 55551, 545545, 10111, 90
output:	545545
"""
num_a = [1, 121, 55551, 545545, 10111, 90]
longest = None
for i in num_a:
    if longest is None or len(str(longest)) < len(str(i)):
        longest = i
print("the longest value:", longest)
