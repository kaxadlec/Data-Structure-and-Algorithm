class Node():
    def __init__(self):
        self.data = None
        self.link = None

# 4-01.py
node1 = Node()      # 빈 노드 생성
node1.data = '1등'   # 데이터 삽입
print(node1.data, end=' ')  # 확인차 노드의 데이터 출력

node2 = Node()  # 빈 노드 생성
node2.data = '2등'   # 노드2에 데이터 삽입
node1.link = node2  # 노드1의 링크에 노드2 연결
print(node1.link.data, end=' ')  # 2등 출력

node3 = Node()
node3.data = "3등"
node2.link = node3
print(node1.link.link.data, end=' ')
#print(node3.data, end=' ')

node4 = Node()
node4.data = "4등"
node3.link = node4
print(node4.data, end=' ')
# print(node1.link.link.link.data, end=' ')

node5 = Node()
node5.data = "5등"
node4.link = node5
print(node5.data)

# 4-03.py
new_node = Node()   # 새 노드 생성
new_node.data = "새로움"   # 새 노드 데이터 대입
new_node.link = node4.link  # 새 노드 링크에 4등->5등 링크 대입
node4.link = new_node   # 4등의 링크에 새 노드 지정

# 4-04.py
node2.link = node3.link  # 3등의 링크를 2등의 링크로 복사
del(node3)  # 3등 삭제

# 4-02.py
current = node1
print(current.data)
while current.link != None:     # current 노드는 현재 노드1, current 노드의 링크와 연결된 노드가 있다면,
                                # 즉 현재 노드의 링크가 비어 있지 않은 동안은 계속 출력
    current = current.link      # 다음노드를 현재노드로 지정.
    print(current.data, end=' ')


