class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')

    while current.link != None:
        current = current.link
        print(current.data, end=' ')

    print()

    # # 4-02.py
    # current = node1
    # print(current.data)
    # while current.link != None:     # current 노드는 현재 노드1, current 노드의 링크와 연결된 노드가 있다면,
    #                                 # 즉 현재 노드의 링크가 비어 있지 않은 동안은 계속 출력
    #     current = current.link      # 다음 노드를 현재 노드로 지정.
    #     print(current.data, end=' ')


# memory = []
head, current, pre = None, None, None
data_array = ['가', '나', '다', '라', '마']

if __name__ == "__main__":
    node = Node()   # 빈 노드 생성
    node.data = data_array[0]   # 노드 데이터에 '가' 대입
    head = node     # 첫 번째 노드를 헤드로 지정
    # memory.append(node)    #노드를 메모리에 넣음

    for data in data_array[1:]:     # 두 번째부터의 노드
        pre = node  # 기존 노드를 임시저장
        node = Node()   # 빈 노드 생성
        node.data = data    # '나', '다', '라', '마' for문에 따라 데이터에 대입
        pre.link = node     # 기존 노드의 링크를 이번에 만든 노드에 연결
        # memory.append(node)

print_nodes(head)





