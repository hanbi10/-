class CircularQueue:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0
        
    def isEmpty(self):
        return self.front == self.rear
        
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item  # 아이템 저장 코드 추가
        
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity  # front 포인터 이동 코드 추가
            return self.array[self.front]
        else: pass
        
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front +1) % self.capacity]
        
    def size(self):
        if self.rear >= self.front:
            return self.rear - self.front
        else:
            return self.capacity - (self.front - self.rear)
    
    #원형 큐 : 문자열 변환을 위한 __str__() 연산
    def __str__(self):
        if self.front < self.rear :
            return str(self.array[self.front+1:self.rear+1])
        else :
            return str((self.array[self.front+1:self.capacity]+self.array[0:self.rear+1] ))

#원형 큐 테스트 코드
if __name__ == "__main__":
    q = CircularQueue(8)
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    q.enqueue('E')
    q.enqueue('F')
    print('A B C D E F 삽입: ', q)
    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())
    print('      3번의 삭제: ', q)
    q.enqueue('G')
    q.enqueue('H')
    q.enqueue('I')
    print('      G H I 삽입: ', q)