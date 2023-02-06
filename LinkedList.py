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


def delete_node(delete_data):
    global pre, head, current

    # 첫번째 노드 삭제
    if head.data == delete_data:
        current = head    # 현재 노드를 삭제할 노드와 같게 만듬.
        head = head.link  # head를 링크가 가리키던 옆에 노드로 변경
        last = head       # last의 시작은 헤드
        while last.link != current:  # 헤드에서 시작해서 마지막 노드를 옆으로 이동하면서 찾는다
            last = last.link
        last.link = head    # 마지막 노드 링크는 헤드가 가리키는 노드
        del(current)        # 현재 노드 삭제
        return

        # 첫번째 외 노드 삭제
    current = head    # 현재 노드 헤드에서 시작
    while current.link != head:     # 헤드에서 시작해서 현재 노드 확인
        pre = current
        current = current.link
        if current.data == delete_data:     # 현재 노드의 데이터가 삭제할 데이터와 같으면
            pre.link = current.link         # 이전 노드 링크를 현재 노드 링크로 둔다.
            del(current)                    # 현재 노드 삭제
            return


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

    delete_node("안양")
    print_nodes(head)

    delete_node("용인")
    print_nodes(head)
    delete_node("평양")
    print_nodes(head)