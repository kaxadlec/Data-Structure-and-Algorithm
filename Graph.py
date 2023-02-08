class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for i in range(size)] for i in range(size)]

cfc = None
stack = []
visited_array = []
name_array = ["Mount", "James", "Kante", "Kepa", "Mudryk", "Fofana"]
Mount, James, Kante, Kepa, Mudryk, Fofana = 0,1,2,3,4,5

cfc = Graph(6)
cfc.graph[0][1] =1; cfc.graph[0][2] =1
cfc.graph[1][0] =1; cfc.graph[1][3] =1
cfc.graph[2][0] =1; cfc.graph[2][3] =1;
cfc.graph[3][1] =1; cfc.graph[3][2] =1; cfc.graph[3][4] =1; cfc.graph[3][5] =1
cfc.graph[4][3] =1; cfc.graph[4][5] =1
cfc.graph[5][3] =1; cfc.graph[5][4] =1


current = 0
stack.append(current)
visited_array.append(current)

while len(stack) != 0:
    next = None

    for vertex in range(6):
        if cfc.graph[current][vertex] == 1:
            if vertex in visited_array:
                pass
            else:
                next = vertex
                break

    if next is not None:
        current = next
        stack.append(current)
        visited_array.append(current)

    else:
        current = stack.pop()

print("방문순서-->", end=' ')
for z in visited_array:
    print(name_array[z], end = ' ')






