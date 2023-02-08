# Breadth First Search - BFS
from collections import deque


class Graph:
    def __init__(self, size):
        self.big = size
        self.graph = [[0 for x in range(size)] for x in range(size)]


my_g = None
# queue = []
queue = deque([])
visited_array = []

my_g = Graph(9)     # 그래프 size
my_g.graph[0][1] = 1; my_g.graph[0][2] = 1; my_g.graph[0][4] = 1
my_g.graph[1][0] = 1; my_g.graph[1][2] = 1; my_g.graph[1][3] = 1
my_g.graph[2][0] = 1; my_g.graph[2][1] = 1; my_g.graph[2][3] = 1; my_g.graph[2][4] = 1; my_g.graph[2][5] = 1
my_g.graph[3][1] = 1; my_g.graph[3][2] = 1
my_g.graph[4][0] = 1; my_g.graph[4][2] = 1; my_g.graph[4][6] = 1; my_g.graph[4][7] = 1
my_g.graph[5][2] = 1
my_g.graph[6][4] = 1; my_g.graph[6][8] = 1
my_g.graph[7][4] = 1; my_g.graph[7][8] = 1
my_g.graph[8][6] = 1; my_g.graph[8][7] = 1


current = 0
queue.append(current)
visited_array.append(current)

while len(queue) != 0:
    next = None
    for vertex in range(9):
        if my_g.graph[current][vertex] == 1:
            if vertex in visited_array:
                pass
            else:
                next = vertex
                break
    if next is not None:
        current = next
        queue.append(current)
        visited_array.append(current)

    else:
        current = queue.popleft()   # pop() 대신 popleft() 사용

for i in visited_array:
    print(i, end= ' --->  ')
print('END')