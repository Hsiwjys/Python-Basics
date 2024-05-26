pos = -1


def search(list_name, target_value):
    i = 0
    while i < len(list_name):
        if list_name[i] == target_value:
            globals()['pos'] = i + 1
            return True
        i = i + 1
    return False


given_list = []
a = int(input("Enter the range of the list:"))
for sd in range(0, a):
    df = input("Enter the value of the position " + str(sd+1))
    given_list.append(df)
print(given_list)
target = input("Enter the value to find:")
if search(given_list, target):
    print("Found at position:", pos)
else:
    print("Not Found")
