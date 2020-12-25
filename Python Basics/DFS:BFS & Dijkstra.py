#Date: 08/04/2019, 11:59PM EST
########################################
#
# Name: Daehoon Gwak
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__
    
    def isEmpty(self):
        return self.top == None

    def __len__(self):
        return self.count

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.value

    def push(self,value):
        newNode = Node(value)
        if self.isEmpty():
            self.top = newNode
            newNode.next = None

        else:
            newNode.next = self.top
            self.top = newNode

        self.count += 1

    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'

        else:
            self.count -= 1
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    def __init__(self): 
        self.head=None
        self.tail=None
        self.count = 0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        return self.head == None

    def __len__(self):
        if self.isEmpty():
            return None
        return self.count

    def enqueue(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    def dequeue(self):
        if self.head == None:
            return 'Queue is empty'
        
        current = self.head.value
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        
        self.count -= 1
        return current

    
class Graph:
    def __init__(self, graph_repr):
        self.vertList = graph_repr


    def bfs(self, start):
        '''
            >>> g1 = {'A': ['B','D','G'],
            ... 'B': ['A','E','F'],
            ... 'C': ['F'],
            ... 'D': ['A','F'],
            ... 'E': ['B','G'],
            ... 'F': ['B','C','D'],
            ... 'G': ['A','E']}
            >>> g=Graph(g1)
            >>> g.bfs('A')
            ['A', 'B', 'D', 'G', 'E', 'F', 'C']
        '''
        if start not in self.vertList: #error if there is unknown starting point
            return 'error: invalid point'

        que = Queue() #make a queue
        visited = [] #mark visited node
        que.enqueue(start) #put starting node in the queue

        while not que.isEmpty(): #que should not empty until we find final answer
            current = que.dequeue() 

            if current not in visited: #mark the unvisited node
                visited.append(current) 

            neighbor = [i for i in self.vertList[current]] #get neighbor list from current node
            neighbor.sort() #sort by alphabetical order

            for i in neighbor: #mark neighbors if they are unvisited nodes
                if type(i) == tuple: #special case; for dictionary containing tuple
                    if i[0] not in visited:
                        que.enqueue(i[0])

                else: #for normal dictionary mark them
                    if i not in visited:
                        que.enqueue(i)

        return visited #return nodes by being visited order


    def dfs(self, start):
        '''
            >>> g1 = {'A': ['B','D','G'],
            ... 'B': ['A','E','F'],
            ... 'C': ['F'],
            ... 'D': ['A','F'],
            ... 'E': ['B','G'],
            ... 'F': ['B','C','D'],
            ... 'G': ['A','E']}
            >>> g=Graph(g1)
            >>> g.dfs('A')
            ['A', 'B', 'E', 'G', 'F', 'C', 'D']
        '''
        if start not in self.vertList: #error if there is unknown starting point
            return 'error: invalid point'
        
        stk = Stack() #make a stack
        visited = []
        stk.push(start)
        
        while not stk.isEmpty():
            current = stk.pop()

            if current not in visited: #mark the current node in unvisited
                visited.append(current)

            neighbor = [i for i in self.vertList[current]] #get neighbor list from current node
            neighbor.sort(reverse = True) #sort by reverse alphabetic order

            for i in neighbor: #mark neighbors if they are unvisited nodes
                if type(i) == tuple: #special case; for dictionary containing tuple
                    if i[0] not in visited:
                        stk.push(i[0])

                else: #for normal dictionary mark them
                    if i not in visited:
                        stk.push(i)

        return visited


    def dijkstra(self,start):
        if start not in self.vertList: #error if there is unknown starting point
            return 'error: invalid point'
        
        distanceMap = {} #shortest distance map
        predecessor = {} #check what was the node before current node
        
        for node in self.vertList: #reset every node by making them infinity except the start node to zero so that we can use the function
            distanceMap[node] = float("inf")
        distanceMap[start] = 0

        while len(self.vertList) > 0: #check every single node until dictionary is empty
            tempNode = None
            
            for node in self.vertList:
                if tempNode == None:
                    tempNode = node

                elif distanceMap[node] < distanceMap[tempNode]:
                    tempNode = node
    

            for neighbor, cost in self.vertList[tempNode]: #check neighbors and their cost
                if cost + distanceMap[tempNode] < distanceMap[neighbor]: #
                    distanceMap[neighbor] = cost + distanceMap[tempNode]
                    predecessor[neighbor] = tempNode


            self.vertList.pop(tempNode) 


        return distanceMap





       
