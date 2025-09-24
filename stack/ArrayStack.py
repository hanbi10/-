class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1
        

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity-1
    
    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else:
            print("stack overflow")
            
    def pop(self):
        if not self.isEmpty():
            item = self.array[self.top]
            self.top -= 1
            return item
        else:
            print("stack overflow")
            
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("stack overflow")
            
    
    def __str__(self):
        return str(self.array[0:self.top+1]) #0~top+1까지만 찍겟다  -> 뒤의 None을 지우는 용도
    
if __name__ == "__main__":
    s = ArrayStack(10)
    for i in range(1,6):  # i = 1, 2, 3, 4, 5
        s.push(i)         # push 연산 5회
    print(' push 5회: ', s) # 스택 내용 출력
    # print(' push 5회: ', s.array)
    
    s.pop()
    print(s)
    print(s.peek())
    s.pop()
    print(s)
    s.pop()
    print(s)
    s.pop()
    print(s)
    