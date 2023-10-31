def search_logn(list, target):
    if list == []:
        return [-1,-1]
    return search_helper(0, len(list), list, target)

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
#print(search_logn([1,3,5,7,7,7,8,8,9],9))

#Task 2
def matrix_search(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows = len(matrix) #3
    columns = len(matrix[0]) #4
    end = rows*columns - 1
    return matrix_helper(0, end, matrix, target)
    
def matrix_helper(start, end, matrix, target):
    
    columns = len(matrix[0]) #4
    index = start + (end-start)//2
    middle = matrix[index//columns][index%columns]
    while middle != target:
        if index == start or index == end:
            return False
        elif middle<target:
            return matrix_helper(index, end, matrix, target)
        else:
            return matrix_helper(start, index, matrix, target)
    return True

#task 2
print(matrix_search([[1,2,6,7],[14,15,17,19],[22,24,25,35]], 16))
print(matrix_search([[1,2,6,7],[14,15,17,19],[22,24,25,35]], 14))