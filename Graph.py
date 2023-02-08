class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for i in range(size)] for i in range(size)]


def print_graph(ob):
    print('  ', end='  ')
    for i in range(ob.SIZE):
        print("%12s" % city_array[i], end=' ')
    print()
    for row in range(ob.SIZE):
        print("%s" % city_array[row], end='   ')
        for col in range(ob.SIZE):
            print("%8d" % ob.graph[row][col], end='      ')
        print()
    print()


def find_vertex(ob, find_vtx):
    stack = []
    visited_array = []

    current = 0
    stack.append(current)
    visited_array.append(current)

    while len(stack) != 0:
        next = None

        for vertex in range(c_size):
            if ob.graph[current][vertex] == 1:
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
city = None
city_array = ['Anyang', 'Suwon', 'Seongnam', 'Bucheon', 'Paju', 'Hanam']
Anyang, Suwon, Seongnam, Bucheon, Paju, Hanam = 0,1,2,3,4,5

# main
c_size = len(city_array)
city = Graph(c_size)
city.graph[Anyang][Suwon] = 80; city.graph[Anyang][Bucheon] = 10
city.graph[Suwon][Anyang] = 80; city.graph[Suwon][Bucheon] = 40; city.graph[Suwon][Paju] = 70
city.graph[Seongnam][Paju] = 30; city.graph[Seongnam][Hanam] = 60
city.graph[Bucheon][Anyang] = 10; city.graph[Bucheon][Suwon] = 40; city.graph[Bucheon][Paju] = 50
city.graph[Paju][Suwon] = 70; city.graph[Paju][Bucheon] = 50; city.graph[Paju][Seongnam] = 30; city.graph[Paju][Hanam] = 20
city.graph[Hanam][Seongnam] = 60; city.graph[Hanam][Paju] = 20

print("인터넷 연결 속도(전체 연결도)")
print_graph(city)

# weighted edge / 가중치와 간선 목록 생성
edge_array = []
for i in range(c_size):
    for n in range(c_size):
        if city.graph[i][n] != 0:
            edge_array.append([city.graph[i][n], i, n])


from operator import itemgetter

# 간선 정렬
# 첫번째 매개변수 edge_array 배열 정렬, key=itemgetter(0) -> 정렬하는 기준 0번째로 설정, reverse=True -> 오름차순으로 정렬
edge_array = sorted(edge_array, key=itemgetter(0), reverse=False)   # reverse = False

# 중복 간선 제거
new_array = []
for x in range(0, len(edge_array), 2):
    new_array.append(edge_array[x])


# 가중치가 높은 간선부터 제거
idx = 0

while (len(new_array) > c_size-1) :	# 간선의 개수가 '정점 개수-1'일 때까지 반복
    start = new_array[idx][1]
    end = new_array[idx][2]
    save = new_array[idx][0]

    city.graph[start][end] = 0
    city.graph[end][start] = 0

    start_yn = find_vertex(city, start)
    end_yn = find_vertex(city, end)

    if start_yn and end_yn :
        del (new_array[idx])
    else:
        city.graph[start][end] = save
        city.graph[end][start] = save
        idx += 1

print('효율적인 연결도')
print_graph(city)
