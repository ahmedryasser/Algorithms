# Task 1
def counter(string):
    # creates a dictionary of every letter and the number of occurances
    # example: {a:1, b:1}
    result = {}
    for i in string:
        if result.__contains__(i):
            result[i] +=1
        else:
            result[i] = 1
    return result

def check_permutation(string1, string2):
    # Creates a dictionary for string 1 and the first substring of string 2 in the size of string 1
    # Keeps sliding the window and getting the counter and comparing it to string1's counter
    # O(n) complexity
    counter1 = counter(string1)
    counter2 = counter(string2[:len(string1)])
    for i in range(len(string2) - len(string1)+1):
        counter2 = counter(string2[i:i+len(string1)])
        if counter1 == counter2:
            return True
    return False

# Task 1 tests:  
# print("bid and eidbatoo:", check_permutation("bid", "eidbatoo"))
# print("ab and eidbaooo:",check_permutation("ab", "eidbaooo"))
# print("ab and eidboaoo:",check_permutation("ab", "eidboaoo"))
# print("abo and eidboaoo:", check_permutation("abo", "eidboaoo"))


#Task 2

def n_queens(configuration):
    # -1 means no queen placed yet
    # starting with column 0
    # 8 for minmoves since the returned solution will always be less than 8
    return backtrack(0, configuration, configuration.copy(), 8)
    
def backtrack(column, configuration, initialConfigurataion, minMoves):
    #compare minMoves with current moves and return the smallest
    if column == 8:
        # A solution is found (base case)
        currentMoves= minimum_moves(configuration, initialConfigurataion)
        return min(currentMoves, minMoves)
    #Recursive case
    for row in range(8):
        if not is_attacked(row,column,configuration):
            # place the queen
            configuration[column] = row
            # we keep updating minmoves by calling the backtrack function recursively
            minMoves = backtrack(column+1, configuration, initialConfigurataion, minMoves)
    return minMoves

def minimum_moves(configuration1, configuration2):
    # Since we can move 7 vertically at most to get any combination we are checking if they are equal and if not
    # then a move vertically can be done
    moves =0
    for i in range(len(configuration1)):
        if configuration1[i] != configuration2[i]:
            moves+=1
    return moves

def is_attacked(row, column, configuration):
    #Checks if a queen we want to place would be attacked by any previous queens
    for prev_column in range(column):
        #checking for horizontal attack
        if configuration[prev_column] == row:
            return True
        #checking for diagonal 1 (positive) they attack if they have same difference
        elif configuration[prev_column] - prev_column == row - column:
            return True
        #checking for diagonal 2 (negative) they attack if they have same sum
        elif configuration[prev_column] + prev_column == row + column:
            return True
    return False

#task 2 tests
print(n_queens([4, 7, 3, 0, 6, 1, 5, 2]))
print(n_queens([0,0,0,0,0,0,0,0]))
print(n_queens([1,2,3,4,5,6,7,1]))
print(n_queens([1,1,1,1,4,5,1,1]))

