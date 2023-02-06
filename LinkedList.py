# Circular Linked List
import random
import math


class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_stores(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')

    while current.link != start:    # 현재 노드의 링크가 첫 번째 노드가 아닐 때까지 반복
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], '편의점: 거리', math.sqrt(x*x + y*y))
    print()


def store_list(store):
    global head, current, pre

    node = Node()
    node.data = store

    if head == None:
        head = node
        node.link = head
        return

    node_x, node_y = node.data[1:]
    node_dis = math.sqrt(node_x * node_x + node_y * node_y)
    head_x, head_y = head.data[1:]
    head_dist = math.sqrt(head_x*head_x + head_y * head_y)

    if head_dist > node_dis:
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        current_x , current_y = current.data[1:]
        current_dis = math.sqrt(current_x * current_x + current_y * current_y)
        if current_dis > node_dis:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head


# 전역 변수 선언
head, pre, current = None, None, None


if __name__ == "__main__":
    store_array = []
    store_name = 'A'
    for _ in range(10):
        store = (store_name, random.randint(1, 100), random.randint(1, 100))
        store_array.append(store)
        store_name = chr(ord(store_name)+1)

    for store in store_array:
        store_list(store)

    print_stores(head)