# Circular Linked List

class Node2():
    def __init__(self):
        self.data = None
        self.plink = None
        self.nlink = None


def print_nodes(start):
    current = start
    if current == None :
        return
    print("정방향: ", end=' ')
    print(current.data, end=' ')
    while current.nlink != None:
        current = current.nlink
        print(current.data, end=' ')
    print()

    print("역방향: ", end=' ')
    print(current.data, end=' ')
    while current.plink != None:
        current = current.plink
        print(current.data, end=' ')


# 전역 변수 선언
head, pre, current = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    node = Node2()
    node.data = data_array[0]
    head = node

    for data in data_array[1:]:
        pre = node
        node = Node2()
        node.data = data
        pre.nlink = node
        node.plink = pre

    print_nodes(head)