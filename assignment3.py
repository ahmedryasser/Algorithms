import time					

def angram_list(list):
    #To test performance
    before = time.perf_counter()
    # an array that keeps track of words that are in alphabatical order
    sortedList=[]
    # the array that stores words in regular form which is returned to user
    finalList=[]
    for word in list:
        #putting each word in lower case and all it's letters in alphabatical order
        if sortedList.__contains__(angram(word)):
            #add to the final array as an angram of a word that exists
            index = 0
            while index<len(finalList) and (angram(finalList[index][0]) != angram(word)):
                index+=1
            if index<len(finalList): finalList[index].append(word)
        else:
            #add as a new entry if no angram partner is found
            sortedList.append(angram(word))
            finalList.append([word])
    after = time.perf_counter()
    print(f"time elapsed is: {before - after:0.4f} seconds")
    return finalList

def angram(word):
    #quick sort
    return ''.join(quick_sort(word.lower()))   
    #merge sort
    #return merge_sort(word.lower()) 
    
def merge_sort(string):
    # More efficient implementaion with O(nlogn) worst case
    if (len(string) == 1):
        return string
    else:
        #splits string into two halves
        first = string[:len(string)//2]
        second = string[len(string)//2:]
        first = merge_sort(first)
        second = merge_sort(second)
        #merges these two together ordered
        return merge(first, second)

def merge(first,second):
    i=0
    j=0
    result=[]
    #compares each letter in first with each one in second and places the lower in result 
    while i<len(first) and j<len(second):
        if first[i]<second[j]:
            result.append(first[i])
            i+=1
        else:
            result.append(second[j])
            j+=1
    result += first[i:]
    result += second[j:]   
    return ''.join(result)

def quick_sort(string):
    # Sorts elements in average case of O(nlogn) but worst case is O(n^2) with bad pivots
    # Picks a pivot and places all the elements smaller then the pivot in the left and all bigger than the pivot on the right
    # then makes a recursive call on left and right and keeping middle
    if len(string)<=1:
        return string
    middle = string[len(string)//2:len(string)//2+1][0]
    start = [x for x in string if x < middle]
    end =  [x for x in string if x > middle]
    return quick_sort(start) + [middle] + quick_sort(end)

print(angram_list( ["bucket","rat","mango","tango","ogtan","tar"]))
print(''.join(quick_sort("bucket")))