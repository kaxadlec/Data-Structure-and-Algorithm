class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for i in range(size)] for i in range(size)]

cfc = None
stack = []
visited_array = []

cfc = Graph(3)
cfc.graph[0][1] = 1
cfc.graph[0][2] = 1
cfc.graph[1][2] = 1
cfc.graph[2][0] = 1
cfc.graph[2][1] = 1
cfc.graph[1][0] = 1

# 무방향 그래프 출력
print("무방향그래프")
for i in range(3):
    for n in range(3):
        print(cfc.graph[i][n], end=' ')
    print()

current = 0
stack.append(current)
visited_array.append(current)

while len(stack) != 0:
    next = None

    for vertex in range(3):
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

for z in visited_array:
    print(chr(ord('A')+z), end =' ')





