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


delete_fc = '토트넘'

current = root
parent = None      # 삭제할 노드의 상위 노드를 저장할 변수 선언

while True:
    if delete_fc == current.data:
        if current.left is None and current.right is None:
            if parent.left == current:
                parent.left = None
            elif parent.right == current:
                parent.right = None
            del(current)

        elif current.left is not None and current.right is None:
            if parent.left == current:
                parent.left = current.left
            elif parent.right == current:
                parent.right = current.left
            del(current)

        elif current.left is None and current.right is not None:
            if parent.left == current:
                parent.left = current.right
            elif parent.right == current:
                parent.right = current.right
            del(current)

        print(f'{delete_fc} 삭제됨')
        break

    elif delete_fc < current.data:
        if current.left is None:
            print(f'{delete_fc}는 트리에 없습니다')
            break
        else:
            parent = current
            current = current.left

    elif delete_fc > current.data:
        if current.right is None:
            print(f'{delete_fc}는 트리에 없습니다')
            break
        else:
            parent = current
            current = current.right

