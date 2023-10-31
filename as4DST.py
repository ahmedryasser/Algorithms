# BST time complexity: O(log n) everything
import queue
class Node:
    def __init__(self, number, name, home_department, program, year):
        self.number = number
        self.name = name
        self.home_department = home_department
        self.program = program
        self.year = year
        self.left = None  
        self.right = None
        self.parent = None
class Queue:
    def __init__(self):
        self.data= []
        self.currentSize=0
    
    def enqueue(self, element): #O(1)
        self.data.append(element)
        self.currentSize +=1
    
    def dequeue(self): # O(n) Inefficient but simple implementation
        self.currentSize -=1
        return self.data.pop(0)

    def size(self):
        return self.currentSize

class BST:
    def __init__(self):
        self.root = None
        
    def inOrder(self):
        #depth first search
        array = []
        self.inOrderRecursive(array, self.root)
        return array
    
    def inOrderRecursive(self, array, root):
        if self.root:
            if root.left:self.inOrderRecursive(array, root.left)
            #print(root.name)
            array.append(root.name.replace(" ", ""))
            if root.right:self.inOrderRecursive(array, root.right)
        
    def breadth_first(self):
        #Level order Traversal
        if self.root:
            #Using queue to track to enqueue the nodes at each level
            treeQueue = Queue()
            array=[]
            treeQueue.enqueue(self.root)
            #starts at the first level
            while treeQueue.size() != 0:
                #goes down a level with each iteration of the loop
                current = treeQueue.dequeue()
                print(current.name)
                array.append(current.name.replace(" ", ""))
                #enqueues left and right children if exists
                if current.left: 
                    treeQueue.enqueue(current.left)
                if current.right: 
                    treeQueue.enqueue(current.right)
            return array
        else:
            return       
            
    def insert(self, newNode):
        if not self.root:
            self.root = newNode
        else:
            self.insertRecursive(self.root, newNode)
            
    def insertRecursive(self, root, newNode):
        if root.name > newNode.name:
            #If new node is lower alphabatically keep trying to insert to the left till you find a None node or a higher node
            if not root.left : 
                root.left = newNode 
            else:
                #recursive call
                self.insertRecursive(root.left, newNode)
        else:
            #If new node is higher alphabatically keep trying to insert to the right till you find a None node or a lower node
            if not root.right : 
                root.right = newNode
                root.right.parent = root
            else:
                #recursive call
                self.insertRecursive(root.right, newNode)
                
    def delete(self, deletedNode):
        if not self.root:
            raise Exception("Can't delete from empty")
        else:
            self.root = self.deleteRecursive(self.root, deletedNode)
            
    def deleteRecursive(self, root, deletedNode):
        if not root:
            return root
        elif root.name < deletedNode.name:
            root.right = self.deleteRecursive(root.right, deletedNode)
        elif root.name > deletedNode.name:
            root.left = self.deleteRecursive(root.left, deletedNode)
        else:
            if root.right:
                if root.left:
                    #If there exists 2 children to the deleted node
                    #Find minimum right subtree
                    minimum = minTree(root.right)
                    root.name, root.number, root.home_department, root.program, root.year = minimum.name, minimum.number, minimum.home_department, minimum.program, minimum.year
                    root.right = self.deleteRecursive(root.right, minimum)
                #If there is only a right child    
                root= root.right
            elif root.left:
                #if there is only a left child
                root= root.left
            else:
                #If there is no children
                root = None
        return root
    
    def populateBst(self):
        with open("tree-input.txt", "r") as file:
            searchTree= BST()
            for line in file:
                operand = line[:1]
                number = line[1:8]
                name = line[8:33]
                home_department = line[33:37]
                program = line[37:41]
                year = line[41:42]
                currentNode = Node(number, name, home_department, program, year)
                if operand == "I":
                    searchTree.insert(currentNode)
                else:
                    searchTree.delete(currentNode)
            return searchTree
        
    def printInOrderToFile(self, InOrderTree, LevelOrderTree):
        with open("printTraversals.txt", "w") as file:
            file.write("In order: ")
            file.write("\n \n")
            for i in InOrderTree:
                file.write(i)
                file.write("\n") 
            file.write("\n Level order: ")
            file.write("\n \n")
            for i in LevelOrderTree:
                file.write(i)
                file.write("\n")    
                
def minTree(node):
    while node.left:
        node = node.left
    return node

#Tests
# searchTree = BST().populateBst()
# searchTree.printInOrderToFile(searchTree.inOrder(), searchTree.breadth_first() )
# print(searchTree.inOrder())
# print("---------------------------")
# print(searchTree.breadth_first())  
# searchTree.breadth_first()  