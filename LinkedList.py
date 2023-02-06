class Node():
    def __init__(self):     # 노드 클래스 정의
        self.data = None
        self.link = None


def print_nodes(start):     # 단순 연결 리스트의 전체 노드 출력. # 매개변수는 시작노드 start
    current = start         # 전달받은 시작노드를 현재 노드로 지정
    if current == None:     # 노드에 데이터가 하나도 없는 연결 리스트인 경우 그냥 반환
        return
    print(current.data, end=' ')

    while current.link != None:     # 노드의 링크가 빌 때까지 다음 노드를 계속 추적해서 출력
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


def insert_node(find_data, insert_data):
    global memory, head, current, pre

    # 첫 번째에 노드 삽입
    if head.data == find_data:
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        return

    # 중간에 노드 삽입
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    # 마지막에 노드 삽입
    node = Node()
    node.data = insert_data
    current.link = node


memory = []
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

    insert_node("가","A")
    print_nodes(head)

    insert_node("다", "MID")
    print_nodes(head)

    insert_node("배열에 없는 문자", "END")
    print_nodes(head)





