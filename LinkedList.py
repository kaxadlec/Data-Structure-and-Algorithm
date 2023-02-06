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

def find_node(find_data):
    global memory, pre, current, head

    current = head
    if current.data == find_data:   # 찾는 노드가 첫번째 헤드 노드
        return current

    while current.link != None:     # 찾는 노드가 중간에
        current = current.link
        if current.data == find_data:
            return current

    return Node()                   # 찾는 노드가 없을 때



# 전역 변수 선언 부분
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

    a = find_node("가")
    print(a.data)
    b = find_node("다")
    print(b.data)
    c = find_node("켁")
    print(c.data)





