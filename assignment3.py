import time					

def angram_list(list):
    before = time.perf_counter()
    sortedList=[]
    finalList=[]
    for word in list:
        #putting each word in lower case and all it's letters in alphabatical order
        if sortedList.__contains__(angram(word)):
            #add to an array
            index = 0
            while index<len(finalList) and (angram(finalList[index][0]) != angram(word)):
                index+=1
            if index<len(finalList): finalList[index].append(word)
        else:
            #add as a new entry
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

    if (len(string) == 1):
        return string
    else:
        first = string[:len(string)//2]
        second = string[len(string)//2:]
        first = merge_sort(first)
        second = merge_sort(second)
        return merge(first, second)

def merge(first,second):
    i=0
    j=0
    result=[]
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
    if len(string)<=1:
        return string
    middle = string[len(string)//2:len(string)//2+1][0]
    start = [x for x in string if x < middle]
    end =  [x for x in string if x > middle]
    return quick_sort(start) + [middle] + quick_sort(end)

print(angram_list( ["bucket","rat","mango","tango","ogtan","tar"]))
print(''.join(quick_sort("bucket")))