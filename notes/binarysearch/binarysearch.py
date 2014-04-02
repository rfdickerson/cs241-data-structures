def binarysearch(value, mylist):
    left = 0
    right = len(mylist) - 1
    mid = (right + left) // 2
    
    while left != right:
        if mylist[mid] < value:
            left = mid + 1
        elif mylist[mid] > value:
            right = mid - 1
        elif mylist[mid] == value:
            return mid
        mid = (right + left) // 2
        
    if mylist[left] == value:
        return left
    else:
        return None
    
    
def recbinarysearch(value, mylist, left, right):
    mid = (left + right) // 2
    if left > right:
        return None
    elif mylist[mid] < value:
        return recbinarysearch(value, mylist, mid + 1, right)
    elif mylist[mid] > value:
        return recbinarysearch(value, mylist, left, mid - 1)
    elif mylist[mid] == value:
        return mid
    else:
        return None
    
    

a = [1,3,5,7,9,11,13,15]

index = binarysearch(7, a)

print 'element is at index:' + str(index)
# element is at index 4

# you can use the len function

    

