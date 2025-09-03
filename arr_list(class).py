class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    # 공백 상태 검사
    def isEmpty(self):
        return self.size == 0

    # 포화 상태 검사
    def isFull(self):
        return self.size == self.capacity

    # 삽입 연산
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1

    # 삭제 연산
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e

    # 원소 얻기
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None

    def __str__(self):
        return str(self.array[0:self.size])


# 테스트 프로그램
if __name__ == "__main__":
    L = ArrayList(50)

    print("최초   ", L)
    L.insert(0, 60)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(L.size, 40)
    L.insert(2, 50)
    print("삽입x5", L)
    L.delete(2)
    print("삭제(2)", L)
    L.delete(L.size-1)
    print("삭제(E)", L)
    L.delete(0)
    print("삭제(0)", L)