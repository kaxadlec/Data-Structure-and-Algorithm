class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for i in range(size)] for i in range(size)]


undi = None
di = None

undi = Graph(5)     # 무방향 그래프, 사이즈는 5
undi.graph[0][1] = 1; undi.graph[0][3] = 1; undi.graph[0][4] = 1
undi.graph[1][0] = 1; undi.graph[1][2] = 1; undi.graph[1][4] = 1
undi.graph[2][1] = 1; undi.graph[2][3] = 1; undi.graph[2][4] = 1
undi.graph[3][0] = 1; undi.graph[3][2] = 1
undi.graph[4][0] = 1; undi.graph[4][1] = 1; undi.graph[4][2] = 1

print("무방향 그래프입니다")
for i in range(5):
    for n in range(5):
        print(undi.graph[i][n], end=' ')
    print()

di = Graph(4)
di.graph[0][3] = 1; di.graph[1][3] = 1
di.graph[1][2] = 1

print("방향 그래프입니다")
for i in range(4):
    for n in range(4):
        print(di.graph[i][n], end=' ')
    print()



