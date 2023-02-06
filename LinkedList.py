import random
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def print_nodes(start):
        current = start
        if current == None:
            return
        print(current.data, end=' ')

        while current.link != None:
            current = current.link
            print(current.data, end=' ')
        print()


def dupli_num(num):
    global pre, head, current

    if head == None:
        return False

    current = head
    if current.data == num:
        return True

    while current.link != None:
        current = current.link
        if current.data == num:
            return True

    return False


def lotto_linked_list(num):
    global pre, head, current

    node = Node()
    node.data = num

    if head == None:    # 새 노드가 첫 노드
        head = node
        return

    if head.data > num:    # if 첫 노드 > 새로운 노드
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data > num:     # if 현재노드 > 입력할 노드
            pre.link = node
            node.link = current
            return

    current.link = node


head, current, pre = None, None, None

if __name__ == "__main__":
    cnt = 0
    while True:
        lotto_num = random.randint(1, 45)   # 1에서 45까지 로또 무작위 번호 생성
        if dupli_num(lotto_num):            # 중복된 숫자 제거 위한 함수
            continue                        # True 이면 continue

        lotto_linked_list(lotto_num)
        cnt = cnt + 1
        if cnt > 5:
            break
    print_nodes(head)