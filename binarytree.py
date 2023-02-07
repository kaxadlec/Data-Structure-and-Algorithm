class tree_node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

root = None
club_array = ['첼시', '아스날', '토트넘', '맨유', '맨시티', '뉴캐슬', '리버풀']

# main
node = tree_node()  # 트리 노드 생성
node.data = club_array[0]   # 노드 데이터에 배열의 0번자리 데이터 넣음
root = node     # 루트 노드 생성


for fc in club_array[1:]:     # 클럽 배열의 1번자리부터 처리

    current = root  # 항상 '첼시' = 루트 노드부터 시작. 현재 작업 노드 = 루트 노드
    node = tree_node()  # 새 노드 생성
    node.data = fc      # 클럽 배열 데이터를 노드에 대입

    while True:
        if fc < current.data:
            if current.left is not None:
                current = current.left
            else:
                current.left = node
                break

        elif fc > current.data:
            if current.right is not None:
                current = current.right
            else:
                current.right = node
                break

find_name = input("찾을 epl 클럽 이름을 입력하세요: ")
current = root

while True:
    if find_name == current.data:
        print(f'{find_name}을 찾았습니다')
        break
    elif find_name < current.data:
        if current.left is not None:
            current = current.left
        elif current.left is None:
            print(f'{find_name}은 없습니다')
            break
    elif find_name > current.data:
        if current.right is not None:
            current = current.right
        elif current.right is None:
            print(f'{find_name}은 없습니다')
            break


