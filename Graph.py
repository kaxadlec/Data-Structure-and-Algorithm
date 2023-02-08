class Graph():
    def __init__(self, size):
        self.big = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


my_graph = None
stack =[]
visited_array = []

my_graph = Graph(9)     # 그래프 size는 4
my_graph.graph[0][1] = 1; my_graph.graph[0][2] = 1; my_graph.graph[0][4] = 1
my_graph.graph[1][0] = 1; my_graph.graph[1][2] = 1; my_graph.graph[1][3] = 1
my_graph.graph[2][0] = 1; my_graph.graph[2][1] = 1; my_graph.graph[2][3] = 1; my_graph.graph[2][4] = 1; my_graph.graph[2][5] = 1
my_graph.graph[3][1] = 1; my_graph.graph[3][2] = 1
my_graph.graph[4][0] = 1; my_graph.graph[4][2] = 1; my_graph.graph[4][6] = 1; my_graph.graph[4][7] = 1
my_graph.graph[5][2] = 1
my_graph.graph[6][4] = 1; my_graph.graph[6][8] = 1
my_graph.graph[7][4] = 1; my_graph.graph[7][8] = 1
my_graph.graph[8][6] = 1; my_graph.graph[8][7] = 1

print('이 그래프는 무방향 그래프')
for row in range(9):
    for col in range(9):
        print(my_graph.graph[row][col], end=' ')
    print()


current = 0
stack.append(current)
visited_array.append(current)

while (len(stack) != 0):
    next = None
    for vertex in range(9):
        if my_graph.graph[current][vertex] == 1:
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

print('방문순서')
for i in visited_array:
    print(chr(ord('A')+i), end=' ')