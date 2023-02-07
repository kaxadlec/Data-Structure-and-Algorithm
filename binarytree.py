import random


class tree_node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


root_club, root_captain= None, None
epl_array = [['첼시', '아스필리쿠에타'], ['아스날', '외데고르'], ['토트넘', '요리스'],
              ['맨유', '매과이어'], ['맨시티', '귄도안'], ['리버풀', '헨더슨'],
              ['뉴캐슬', '라셀레스'], ['웨스트햄', '라이스']]
random.shuffle(epl_array)


# club 트리
node = tree_node()  # 트리 노드 생성
node.data = epl_array[0][0]   # 노드 데이터에 배열의 0번자리의 0번자리 club 데이터 넣음
root_club = node     # 루트 노드 생성


for epl in epl_array[1:]:     # epl 배열의 1번자리부터 처리

    current = root_club  # 현재 작업 노드 = 루트 노드

    club = epl[0]
    node = tree_node()  # 새 노드 생성
    node.data = club     # epl 배열의 0번방 club을 노드에 대입

    while True:
        if club < current.data:
            if current.left is not None:
                current = current.left
            else:
                current.left = node
                break

        elif club > current.data:
            if current.right is not None:
                current = current.right
            else:
                current.right = node
                break


# captain 트리
node = tree_node()
node.data = epl_array[0][1]
root_captain = node


for epl in epl_array[1:]:     # epl 배열의 1번자리부터 처리

    current = root_captain  # 현재 작업 노드 = 루트 노드

    captain = epl[1]
    node = tree_node()  # 새 노드 생성
    node.data = captain     # epl 배열의 1번방 captain을 노드에 대입

    while True:
        if captain < current.data:
            if current.left is not None:
                current = current.left
            else:
                current.left = node
                break

        elif captain > current.data:
            if current.right is not None:
                current = current.right
            else:
                current.right = node
                break

club_or_captain = int(input('검색하고 싶은 목록을 선택하세오. 클럽---1 주장---2   '))
find_epl = input('검색어를 입력하세요.')

if club_or_captain == 1:
    root = root_club
elif club_or_captain == 2:
    root = root_captain

current = root

while True:
    if find_epl == current.data:
        print(f'{find_epl}은 목록에 있습니다.')
        break

    elif find_epl < current.data:
        if current.left is None:
            print(f'{find_epl}은 목록에 없습니다ㅠ')
            break
        else:
            current = current.left

    elif find_epl > current.data:
        if current.right is None:
            print(f'{find_epl}은 목록에 없습니다ㅠ')
            break
        else:
            current = current.right