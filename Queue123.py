def is_queue_full():
    global size, queue, front, rear
    if (rear+1) % size == front:
        return True
    else:
        return False


def is_queue_empty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def enqueue(data):
    global size, queue, front, rear
    if is_queue_full():
        print("Queue is full!")
        return
    rear = (rear + 1) % size
    queue[rear] = data


def dequeue():
    global size, queue, front, rear
    if is_queue_empty():
        print("Queue is empty!")
        return
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    return data


def time():
    global size, queue, front, rear
    time_sum = 0
    for n in range((front + 1) % size, (rear + 1) % size):
        time_sum = time_sum + queue[n][1]
    return time_sum

# 전역 변수
size = 4
front = rear = 0
queue = [None for _ in range(size)]

if __name__ == "__main__" :
    idx = [('fix', 3), ('use', 9), ('refund', 4), ('etc', 1)]

    for call in idx:
        print("waiting time --> ", time(), "min")
        print("waiting list --> ", queue)
        enqueue(call)
        print()

