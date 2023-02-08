class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for i in range(size)] for i in range(size)]


def print_graph(data):
    print('        ', end= '')
    for i in range(data.size):
        print(cfc_array[i], end=' ')
    print()
    for n in range(data.size):
        print(cfc_array[n], end='   ')
        for k in range(data.size):
            print(data.graph[n][k], end='      ')
        print()
    print()


chelsea = None
cfc_array = ['Kai   ', 'Mason ', 'Reece ', 'NGolo ', 'Enzo  ', 'Kepa  ', 'Wesley']
Kai =0; Mason=1; Reece =2; NGolo=3; Enzo=4; Kepa=5; Wesley=6

cfc_size= 7

chelsea = Graph(cfc_size)
chelsea.graph[0][1] =1; chelsea.graph[0][3] =1; chelsea.graph[0][4] =1
chelsea.graph[1][0] =1; chelsea.graph[1][2] =1; chelsea.graph[1][6] =1
chelsea.graph[2][1] =1; chelsea.graph[2][4] =1; chelsea.graph[2][5] =1
chelsea.graph[3][0] =1; chelsea.graph[3][6] =1
chelsea.graph[4][0] =1; chelsea.graph[4][2] =1
chelsea.graph[5][2] =1; chelsea.graph[5][6] =1
chelsea.graph[6][1] =1; chelsea.graph[6][3] =1; chelsea.graph[6][5] =1

# 무방향 그래프 출력
print_graph(chelsea)





