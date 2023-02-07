import random


class tree_node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

root = None
stuff_array = ['삼각깁밥', '햄버거', '초코에몽', '제로콜라', '아메리카노', '쫄병스낵', '생수']
sell_num = random.randint(10,30)
sell_array = [random.choice(stuff_array) for _ in range(sell_num)]    # 중복가능
print("오늘 판매된 물품(중복됨)")
print(sell_array)


node = tree_node()
node.data = sell_array[0]   # 첫번째 물품 - 노드에 데이터 입력
root = node                 # 루트 - 첫번째 노드

for item in sell_array[1:]:
    current = root  # 루트에 있던 첫번째 노드는 current에 넣어둠
    node = tree_node()
    node.data = item    # sell_array 1번지부터 node에 대입

    while True:
        if item == current.data:
            break

        elif item < current.data:
            if current.left is None:
                current.left = node     # item이 작다면 item 노드가 current의 왼쪽링크에.
                break
            else:
                current = current.left  # 계속 왼쪽 아래로 내려갑니다

        elif item > current.data:
            if current.right is None:
                current.right = node
                break
            else:
                current = current.right


def sold_stuff(node):
    if node is None:
        return
    print(node.data, end=' ')
    sold_stuff(node.left)
    sold_stuff(node.right)


print("오늘 판매된 물품종류(중복아님)")
sold_stuff(root)



