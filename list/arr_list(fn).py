#리스트의 데이터 : 전역변수
capacity = 100    #리스트 용량
array = [None]*capacity   #요소 배열 : 길이가 capacity
size = 0 # 리스트 항목들의 개수 : 공백상태(0)으로 초기화

#리스트의 연산 : 일반 함수

#공백 상태 검사 isEmpty()
def isEmpty():
    if size == 0:
        return True #공백이면 True 반환
    else:
        return False


#포화 상태 검사 isFull()
def isFull(): # size가 capacity이면 포화상태 비교 연산 size == capacity 결과를 바로 반환
    return size == capacity

#삽입 연산
def insert(pos, e):
    global size
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1]
        array[pos] = e  # 수정: 새로운 요소를 삽입 위치에 저장
        size += 1
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()
        
#삭제 연산
def delete(pos):
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size -1):
            array[i] = array[i+1]
        size -= 1
        return e
    else:
        print("리스트 underflow 또는 유효하지 않은 삭제 위치")        
        exit()
        
def getEntry(pos):
    if 0 <= pos < size:  # 수정: 0 <= pos < size
        return array[pos]
    else:
        return None

# 테스트 프로그램
if __name__ == "__main__":
    print("최초   ", array[0:size])
    insert(0, 10)
    insert(0, 20)
    insert(1, 30)
    insert(size, 40)
    insert(2, 50)
    print("삽입x5", array[0:size])
    delete(2)
    print("삭제(2)", array[0:size])
    delete(size-1)
    print("삭제(E)", array[0:size])
    delete(0)
    print("삭제(0)", array[0:size])