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


def LinkedList(name_email):
    global pre, head, current

    node = Node()
    node.data = name_email
    if head == None:    # 새 노드가 첫 노드
        head = node
        return

    if head.data[1] > name_email[1]:    # if 첫 노드 > 새로운 노드
        node.link = head
        head = node
        return

    current = head      #
    while current.link != None:
        pre = current
        current = current.link
        if current.data[1] > name_email[1]:     # if 현재노드 > 입력할 노드
            pre.link = node
            node.link = current
            return

    current.link = node


head, current, pre = None, None, None

if __name__ == "__main__":

    while True:
        name = input("이름: ")
        if name == None:
            break
        email = input("이메일: ")
        LinkedList([name, email])

        print_nodes(head)