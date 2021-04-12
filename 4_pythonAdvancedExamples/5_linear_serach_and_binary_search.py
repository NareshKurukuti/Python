#Linear Search
pos = -1
def serach(list, n):
    k = 0
    for i in list:
        if i == n:
            globals()['pos'] = k
            return True
        k = k + 1

list = [5,6,4,8,9,2]
n = 9

if serach(list, n):
    print("Found at the index of",pos)
else:
    print("Not Found")



#In linear serach values are not sorted, but in Binary Search values are sorted
print("Binary Search Example")
position = -1
def binary_search(list, n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2  #Integer Division

        if list[mid] == n:
            globals()['position'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1

    return False

list_of_items = [4,7,8,12,45,99, 101, 1078,19909, 90099]
k = 45

if binary_search(list_of_items, k):
    print("Found at ", position)
else:
    print("Not Found")

