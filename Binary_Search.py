pos = -1


def search(mass, n):
    lower = 0
    upper = len(mass) - 1
    if lower > upper:
        return False

    while lower <= upper:
        mid = (lower + upper) // 2
        if mass[mid] == n:
            return mid
        else:
            if mass[mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1

    return False


dot = [12, 45, 767, 90.45, 789, 35, 678, "jj"]
print(dot)
input_Number = float(input("Enter the number to find in the list:"))
if search(dot, input_Number):
    print("Found at", pos + 1)
else:
    print("Not found")
