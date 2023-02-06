# Circular Linked List
import random


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


def count_odd_even():
    global head, current
    even, odd = 0, 0

    current = head
    while True:
        if current.data % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        if current.link == head:
            break
        current = current.link

    return odd, even


def make_zero_num(odd, even):
    if odd > even:
        remainder = 1
    else:
        remainder = 0

    current = head
    while True:
        if current.data % 2 == remainder:
            current.data = current.data * -1
        if current.link == head:
            break
        current = current.link



# 전역 변수 선언
head, pre, current = None, None, None


if __name__ == "__main__":
    data_array = []
    for _ in range(7):
        data_array.append(random.randint(1,50))

    node = Node()
    node.data = data_array[0]
    head = node
    node.link = head  # 노드의 링크를 헤드에 연결

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head  # 노드의 링크를 헤드에 연결 : 원형 연결 리스트이기 때문.

    print_nodes(head)

    odd_count, even_count = count_odd_even()
    print(f'홀수는 {odd_count}개, 짝수는 {even_count}개')

    make_zero_num(odd_count, even_count)
    print_nodes(head)