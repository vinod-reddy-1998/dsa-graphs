# k=[[0 for i in range(3)]for j in range(3)]
# print(k)


class Graph:
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