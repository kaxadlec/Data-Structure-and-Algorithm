# Circular Linked List
class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')

    while current.link != start:    # 현재 노드의 링크가 첫 번째 노드가 아닐 때까지 반복
        current = current.link
        print(current.data, end=' ')

    print()



def insert_node(find_data, insert_data):
    global head, current, pre

    if head.data == find_data:  # 맨 앞에(첫번째 노드) 삽입할 경우
        node = Node()
        node.data = insert_data
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return
    # 중간에 노드 삽입할 경우
    current = head     # 헤드부터 시작해서 현재, current 노드가  find_data인지 확인
    while current.link != head:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current  # 새로만든 노드는 current 노드로 링크
            pre.link = node      # pre 링크는 노드로
            return

    # 마지막에 노드 삽입할 경우
    node = Node()
    node.data = insert_data
    current.link = node
    node.link = head


# 전역 변수 선언
head, pre, current = None, None, None
data_array = ["안양", "수원", "시흥", "성남", "용인"]

if __name__ == "__main__":
    node = Node()
    node.data = data_array[0]
    head = node
    node.link = head        # 노드의 링크를 헤드에 연결

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head    # 노드의 링크를 헤드에 연결 : 원형 연결 리스트이기 때문.

    print_nodes(head)

    insert_node("안양", "동두천")
    print_nodes(head)
    insert_node("성남", "파주")
    print_nodes(head)
    insert_node("평양", "부천")
    print_nodes(head)