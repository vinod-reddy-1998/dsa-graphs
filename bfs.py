# k=[[0 for i in range(3)]for j in range(3)]
# print(k)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None
        return temp.data




class Graph(Queue):
    def __init__(self,vertices):
        self.vertices=vertices
        self.adjMat=[[0 for i in range(self.vertices)]for j in range(self.vertices)]
    
    def insertEdge(self,u,v,x=1):
        self.adjMat[u][v]=x
    

    def removeEdge(self,u,v):
        self.adjMat[u][v]=0

    def existEdge(self,u,v):
        return self.adjMat[u][v]!=0
    

    def vertexCount(self):
        return self.vertices

    def edgeCount(self):
        count=0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjMat[i][j]!=0:
                    count+=1
        return count

    def vertices(self):
        for i in range(self.vertices):
            print(i,end=" ")
        print()


    def outdegre(self,v):
        count=0
        for i in range(self.vertices):
            if self.adjMat[v][i]!=0:
                count+=1
        return count
            
    def indegre(self,v):
        count=0
        for i in range(self.vertices):
            if self.adjMat[i][v]!=0:
                count+=1
        return count
            
    def showAdjMat(self):
        print(self.adjMat)
    
    def bfs(self,s):
        i=s
        q=Queue()
        visited=[0]*self.vertices
        print(i,end=" ")
        visited[i]=1
        q.enqueue(i)
        while len(q)!=0:
            i=q.dequeue()
            for j in range(self.vertices):
                if self.adjMat[i][j]==1 and visited[j]==0:
                    print(j,end=" ")
                    visited[j]=1
                    q.enqueue(j)






G=Graph(4)
G.showAdjMat()
print("vertices are:",G.vertexCount())
print("edges count is:",G.edgeCount())
G.insertEdge(0,1,12)
G.insertEdge(1,0,12)
G.insertEdge(0,2,15)
G.insertEdge(2,0,15)
G.insertEdge(0,3,30)
G.insertEdge(3,0,30)
G.insertEdge(1,1,5)
G.insertEdge(2,1,20)
G.insertEdge(1,2,20)
G.showAdjMat()
print("edges count is:",G.edgeCount())
G.bfs(0)