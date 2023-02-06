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


def linkedlist(bts):
    global memory, head, current, pre
    print_nodes(head)

    node = Node()
    node.data = bts

    if head == None:    # 헤드가 비어있을 때 헤드에 첫 노드 지정.
        head = node
        return


    if head.data[1] > bts[1] :    # 새로운 데이터가 첫 노드보다 작다면.
        node.link = head
        head = node
        return


    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[1] > bts[1]:     # 현재의 노드가 입력할 노드보다 크다면  (입력할 노드는 첫 노드보다 큼)
            pre.link = node
            node.link = current
            return

    current.link = node     # 삽입하는 노드가 가장 클 때


# 전역 변수 선언 부분
memory = []
head, current, pre = None, None, None
data_array = [["지민", 180], ["정국", 177], ["뷔", 183], ["슈가", 175], ["진", 179]]


if __name__ == "__main__":
    for data in data_array:
        linkedlist(data)

    print_nodes(head)






