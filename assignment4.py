#To use in implementing Breadth first searches
class Queue:
    def __init__(self):
        self.data= []
        self.currentSize=0
    
    def enqueue(self, element): #O(1)
        self.data.append(element)
        self.currentSize +=1
    
    def dequeue(self): # O(n) Inefficiant but simple implementation
        self.currentSize -=1
        return self.data.pop(0)
    
    def poll(self):
        return self.data[0]
    
    def size(self):
        return self.currentSize
    
    def displayQueue(self):
        print("Queue: ")
        for i in self.data:
            print(i, "<- ",end='')
        print('\n')
        
class City:
    # Using lists instead of matrixes
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.connectedCities = []
    def neigbors_append(self, city):
        return self.connectedCities.append(city)
    def neigbors(self):
        return self.connectedCities
    def city_population(self):
        return self.population

def create_graph():
    cities = {}
    #looping through every line in the file and placing the string before : in name and after in population
    with open("city_population.txt", "r") as file:
        for line in file:
            name, population = line.split(" : ")
            name, population = name.replace("\n", ""), population.replace("\n", "")
            cities[name] = City(name, int(population))
    
    #looping through every line in the file and appending the string before : in city2's connected cities list and vice versa
    with open("road_network.txt", "r") as file:   
        for line in file:
            city1, city2 = line.split(" : ")
            city1, city2 = city1.replace("\n", ""), city2.replace("\n", "")
            cities[city1].neigbors_append(cities[city2])
            cities[city2].neigbors_append(cities[city1])
            # print(city1, "Cities: ")  
            # for i in range(len(cities[city1].connectedCities)):
            #     print(cities[city1].connectedCities[i].name, "and", end=" ")
            # print("\n")
    return cities
 
                
def number_of_islands(cities):
    visited = []
    count =0
    def bfs(city):
        queue = Queue()
        queue.enqueue(city)
        # loops until queue is empty
        while queue.size() != 0:
            current = queue.dequeue()
            # continue if city is already in visited
            if current in visited:
                continue
            visited.append(current)
            #loops through the neighbors and adds the neighbor to visited if it is not already there
            for neighbor in cities[current].neigbors():
                if neighbor.name not in visited:
                    queue.enqueue(neighbor.name)        
        
    for city in cities:
        if city not in visited:
            bfs(city)
            count+=1
    return count        
# Task 1,2,3 test        
print("Number of Islands: ",number_of_islands(create_graph()))

#Task 4

def island_populations(cities):
    visited = []
    totalPopulation = 0
    def bfs(city):
        queue = Queue()
        queue.enqueue(city)
        totalPopulation = 0
        totalPopulation += cities[city].city_population() 
        while queue.size() != 0:
            current = queue.dequeue()
            if current in visited:
                continue
            visited.append(current)
            for neighbor in cities[current].neigbors():
                if neighbor.name not in visited:
                    queue.enqueue(neighbor.name) 
                    totalPopulation += neighbor.city_population() 
        return totalPopulation
    islands = []                
    for city in cities:
        if city not in visited:
            islands.append(bfs(city))
    return islands

print(island_populations(create_graph()))

def closest_link(city1, city2, cities):
    try:
        cities[city1], cities[city2]
    except KeyError as wrongCity:
        raise Exception("Error: This city does not Exist")
    visited = []
    queue = Queue()
    queue.enqueue(city1)
    queue.enqueue(0)
    while queue.size() != 0:
        current = queue.dequeue()
        distance = queue.dequeue()
        if current == city2:
            return distance
        visited.append(current)
        for neighbor in cities[current].neigbors():
            if neighbor.name not in visited:
                queue.enqueue(neighbor.name) 
                queue.enqueue(distance +1)                 
    return -1

print("Minimum distace: ", closest_link("New York", "Hoover", create_graph() ) )