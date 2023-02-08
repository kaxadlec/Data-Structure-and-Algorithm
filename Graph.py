class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for i in range(size)] for i in range(size)]


def print_graph(data):
    print(' ', end=' ')
    for i in range(data.SIZE):
        print("%15s" % mart_array[i][0], end=' ')
    print()
    for row in range(data.SIZE):
        print("%8s" % mart_array[row][0], end='   ')
        for col in range(data.SIZE):
            print("%8d" % data.graph[row][col], end='      ')
        print()
    print()


# global variable
chip = None
mart_array = [['Lotte',30], ['E-mart', 50], ['Homeplus', 20], ['Costco',10] ,['Hanaro', 5]]
Lotte, E, Homeplus, Costco, Hanaro = 0, 1, 2, 3, 4

# main
m_size = 5
chip = Graph(m_size)
chip.graph[Lotte][E] = 1; chip.graph[Lotte][Homeplus] = 1
chip.graph[E][Lotte] = 1; chip.graph[E][Homeplus] = 1; chip.graph[E][Costco] = 1
chip.graph[Homeplus][Lotte] = 1; chip.graph[Homeplus][E] = 1; chip.graph[Homeplus][Costco] = 1
chip.graph[Costco][Homeplus] = 1; chip.graph[Costco][E] = 1; chip.graph[Costco][Hanaro] = 1
chip.graph[Hanaro][Costco] = 1

print("graph for mart")
print_graph(chip)

stack =[]
visited_array = []

current = 0     # 시작
stack.append(current)
visited_array.append(current)

max_mart = current
max_count = mart_array[current][1]  # 칩 갯수

while len(stack) != 0:
    next = None

    for vertex in range(m_size):
        if chip.graph[current][vertex] == 1:
            if vertex in visited_array:
                pass
            else:
                next = vertex
                break

    if next is not None:
        current = next
        stack.append(current)
        visited_array.append(current)

        #################################
        # 방문한 마트의 칩 개수가 최대 개수보다 많으면, current 마트의 칩 개수를 max_count에, current를 max_mart에 저장
        if mart_array[current][1] > max_count:
            max_count = mart_array[current][1]
            max_mart = current
    else:
        current = stack.pop()

print("칩 개수가 가장 많은 마트, 개수")
print(mart_array[max_mart][0])
print(mart_array[max_mart][1])
