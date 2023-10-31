def search_logn(list, target):
    if list == []:
        return [-1,-1]
    tuple = search_helper(0, len(list), list, target)
    return tuple

def search_helper(start, end, list, target):
    index = (start+end)//2
    while list[index] != target:
        if index == start or index == end:
            return [-1,-1]
        elif list[index]<target:
            return search_helper(index, end, list, target)
        else:
            return search_helper(start, index, list, target)
    firstLast = first_last(index, list, target)
    return firstLast

def first_last(index, list, target):
    first = index
    last = index
    while last<len(list) and list[last] == target:
        last +=1
    while list[first] == target:
        first -=1
    return [first+1, last-1]    

#test task 1
print(search_logn([1,3,5,7,7,7,8,8,9],9))

def matrix_search(matrix, target):
    list = []
    for i in matrix:
        list +=i
    return [-1,-1] != search_logn(list, target)


print(matrix_search([[1,2],[3,4],[5,6]], 9))