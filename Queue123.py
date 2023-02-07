def is_queue_full():
    global size, queue, front, rear
    if rear == size - 1:     # 큐의 (사이즈-1)과 rear 같으면 꽉 채워진 것임.
        return True
    else:
        return False


def is_queue_empty():
    global size, queue, front, rear
    if front == rear:       # rear와 front가 같으면 큐는 비워진 것임.
        return True
    else:
        return False


def enqueue(data):
    global size, queue, front, rear
    if is_queue_full():     # 데이터 넣어야 하는데 큐가 꽉 채워져 있으면 안 되죠
        print("Queue is full!")
        return
    rear = rear + 1
    queue[rear] = data


def dequeue():
    global size, queue, front, rear
    if is_queue_empty():    # 데이터 빼야 하는데 큐가 비워져 있으면 안 되죠
        print("Queue is empty!")
        return
    front = front + 1       # 큐의 데이터가 하나씩 빠질수록 front 는 1 씩 커짐
    data = queue[front]     # data 에 저장
    queue[front] = None     # front가 가리키는 큐의 데이터를 없어면 끝.

    for n in range(front+1, rear +1):    # 만약 큐의 크기가 5일 때 꽉 차있는 상태라면 front = -1, rear = 4 이므로 0,1,2,3,4 범위이다.
                                         # 한 명 나가면 front = 0, rear = 4 이므로 1,2,3,4 범위이다.
        queue[n-1] = queue[n]
        queue[n] = None
    front = -1
    rear = rear -1

    return data

# 전역 변수
size = 6
front = rear = -1
queue = [None for _ in range(size)]

if __name__ == "__main__" :
    enqueue('Thiago')
    enqueue('Micheal')
    enqueue('Mason')
    enqueue('Kai')
    enqueue('Reece')
    enqueue('Ben')
    print('줄 순서')
    print(queue)

    for _ in range(rear+1):     # range(6)
        print(dequeue(), '입장')
        print(queue)

    print("finish!")