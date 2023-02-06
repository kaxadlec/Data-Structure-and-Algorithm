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