class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(data):
    print('       ', end= '')
    for i in range(data.size):
        print(name_array[i], end='  ')
    print()
    for n in range(data.size):
        print(name_array[n], end='   ')
        for k in range(data.size):
            print(data.graph[n][k], end='      ')
        print()
    print()


def find_vertex(g, find_vtx):
    stack = []
    visited_array = []

    current = 0
    stack.append(current)
    visited_array.append(current)

    while len(stack) != 0:
        next = None

        for vertex in range(c_size):
            if c1.graph[current][vertex] == 1:
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

    if find_vtx in visited_array:
        return True
    else:
        return False

# global variable
c1 = None
name_array = ['London', "Paris", "Madrid", "Porto", "Roma", "Munich", "Newyork"]
London, Paris, Madrid, Porto, Roma, Munich, Newyork = 0,1,2,3,4,5,6

# main
c_size = 7
c1 = Graph(c_size)
c1.graph[London][Paris] = 10; c1.graph[London][Munich] = 15; c1.graph[London][Roma] = 30
c1.graph[Paris][London] = 10; c1.graph[Paris][Munich] = 12; c1.graph[Paris][Madrid] = 8
c1.graph[Munich][London] = 15; c1.graph[Munich][Paris] = 12; c1.graph[Munich][Madrid] = 20
c1.graph[Madrid][Paris] = 8; c1.graph[Madrid][Munich] = 20; c1.graph[Madrid][Porto] = 18; c1.graph[Madrid][Roma] = 40
c1.graph[Madrid][Newyork] = 50
c1.graph[Roma][London] = 30; c1.graph[Roma][Madrid] = 40
c1.graph[Porto][Madrid] = 18; c1.graph[Porto][Newyork] = 60
c1.graph[Newyork][Madrid] = 50; c1.graph[Newyork][Porto] = 60

print("Airplane Fee (full)")
print_graph(c1)


# weighted edge / 가중치와 간선 목록 생성
edge_array = []
for i in range(c_size):
    for n in range(c_size):
        if c1.graph[i][n] != 0:     #c1.graph 값이 0이면 무씀모
            edge_array.append([c1.graph[i][n], i, n])


from operator import itemgetter

# 간선 정렬
# 첫번째 매개변수 edge_array 배열 정렬, key=itemgetter(0) -> 정렬하는 기준 0번째로 설정, reverse=True -> 내림차순으로 정렬
edge_array = sorted(edge_array, key=itemgetter(0), reverse=True)

# 중복 간선 제거
new_array = []
for i in range(0, len(edge_array), 2):
    new_array.append(edge_array[i])


# 가중치가 높은 간선부터 제거
idx = 0
while len(new_array) > c_size - 1:  # edge 개수가 (vertex 개수 - 1) 일때까지 반복
    start = new_array[idx][1]   # 0번 간선목록 안의 1번방
    end = new_array[idx][2]     # 0번 간선목록 안의 2번방
    save = new_array[idx][0]    # 복구를 대비하여 save 변수에 기존 가중치 저장

    c1.graph[start][end] = 0    # 가중치 0으로
    c1.graph[end][start] = 0    # 가중치 0으로

    # find_vertex 이용하여 제거된 각 정점이 기존 그래프와 동떨어졌는지 확인하기 위해 만듬
    start_yn = find_vertex(c1,start)
    end_yn = find_vertex(c1, end)

    if start_yn and end_yn:     # 두 vertex 모두 그래프와 연결되어있으면
        del(new_array[idx])     # 가중치 배열에서 제거

    else:                       # vertex 하나라도 그래프와 떨어져있으면
        c1.graph[start][end] = save     # save 통해 간선(edge) 복구
        c1.graph[end][start] = save
        idx = idx + 1           # idx 1 증가시켜 제거할 위치를 배열의 다음 위치로 이동

print("최소 비용")
print_graph(c1)