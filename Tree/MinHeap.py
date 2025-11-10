#최소힙의 삽입 알고리즘
def heappush(heap, n):
    heap.append(n)
    i = len(heap) - 1
    
    while i > 1:
        pi = i // 2
        if n < heap[pi]:
            heap[i] = heap[pi]
            i = pi
        else:
            break
    heap[i] = n

#최소힙의 삭제 알고리즘
def heappop(heap):
    size = len(heap) - 1
    if size == 0:
        return None

    root = heap[1]
    last = heap[size]
    
    pi = 1
    i = 2
    
    while i <= size:
        if i < size and heap[i] > heap[i+1]: 
            i += 1
        
        if last <= heap[i]:
            break
        
        heap[pi] = heap[i]
        pi = i
        i *= 2
        
    heap[pi] = last
    heap.pop()
    return root


#최소힙 테스트 프로그램
if __name__ == '__main__':
    data = [2, 5, 4, 8, 9, 3, 7, 3]
    heap = [0]
    print("입력", data)
    
    for e in data:
        heappush(heap, e)
        print("heap : ", heap[1:])
    
    print("\n--- 삭제 과정 ---")
    print("삭제:", heappop(heap))
    print("heap:", heap[1:])
    print("삭제:", heappop(heap))
    print("heap:", heap[1:])
    print("삭제:", heappop(heap))
    print("heap:", heap[1:])
    print("삭제:", heappop(heap))
    print("heap:", heap[1:])