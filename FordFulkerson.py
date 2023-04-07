import datetime

def display(matrix):
    print("Current matrix values: ")
    for row in matrix:
        print(row)

def FordFulkerson(adjMatrix, capMatrix, source, sink):
    n = len(capMatrix)

    #Initalizes the flow value to 0
    flow = 0

    #Creates a residual matrix with initial values of 0
    #residual matrix is what is used to determine remaining capacity of the system
    residualMatrix = [[0 for y in range(n)] for x in range(n)]


    #Loop that continues until we reach the max capacity of the network
    while True:
        path = [-1 for x in range(n)]
        path[source] = -2

        M = [0 for x in range(n)]
        M[source] = 1e9 

        pathFlow, path = DFS(adjMatrix, capMatrix, source, sink, residualMatrix, path, M)

        if pathFlow == 0:
            #if there can no longer be any flow then we have reached the max flow capacity in all paths
            break

        flow += pathFlow
        v = sink

        while v != source:
            u = path[v]
            residualMatrix[u][v] = residualMatrix[u][v] + pathFlow
            residualMatrix[v][u] = residualMatrix[v][u] - pathFlow
            v = u
    return flow

def DFS(adjMatrix, capMatrix, source, sink, residualMatrix, path, M):

    stack = [source]

    while stack:
        u = stack.pop()
        
        for v in adjMatrix[u]:

            if capMatrix[u][v] - residualMatrix[u][v] > 0 and path[v] == -1:
                path[v] = u
                M[v] = min(M[u], capMatrix[u][v] - residualMatrix[u][v])

                if v != sink:
                    stack.append(v)
                else:
                    return M[sink], path
    return 0, path



if __name__ == "__main__":


    adjMatrix = [[1,4],
                 [2,3],
                 [5],
                 [2,5],
                 [1,3],
                 []
                ]
    
    capMatrix = [[0,7,0,0,4,0],
                 [0,0,5,3,0,0],
                 [0,0,0,0,0,8],
                 [0,0,3,0,0,5],
                 [0,3,0,2,0,0],
                 [0,0,0,0,0,0]
                ]
    
    source = 0

    sink = 5
    begin = datetime.datetime.now()

    for i in range(100):
        FordFulkerson(adjMatrix, capMatrix, source, sink)

    end = datetime.datetime.now()

    print("Max flow with DFS: ", FordFulkerson(adjMatrix, capMatrix, source, sink))

    print(f"Elapsed runtime of the algo over 100 times is {(end - begin)}")