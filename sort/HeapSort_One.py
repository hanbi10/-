# 배열 1-based 방식의 heapify 함수 - 최대 힙 만들기(제자리 정렬)
def heapify(arr, n, i):
    largest = i           # 현재 서브트리의 루트(i)를 가장 큰 값으로 가정
    left = 2 * i          # 왼쪽 자식 노드 인덱스
    right = 2 * i + 1     # 오른쪽 자식 노드 인덱스

    # 왼쪽 자식이 존재하고, 루트보다 크다면 largest를 왼쪽 자식으로 변경
    if left <= n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 존재하고, 현재 largest보다 크다면 largest를 오른쪽 자식으로 변경
    if right <= n and arr[largest] < arr[right]:
        largest = right

    # largest가 변경되었다면(자식 중 더 큰 값이 있으면), 부모(i)와 교환
    if largest != i:
        temp = arr[i]             # swap: arr[i] <-> arr[largest]
        arr[i] = arr[largest]
        arr[largest] = temp

        # 교환된 위치에서 다시 heapify 수행 (아래 방향으로 힙 속성 회복)
        heapify(arr, n, largest)

# 1-based heap sort
def heapSort(arr):
    n = len(arr) - 1        # 실제 데이터 개수 (0번 인덱스는 사용하지 않음)

    # 1단계: 최대 힙 만들기 (build-heap)
    # 마지막 단말노드의 부모노트 부터 루트(1) 까지 heapify 수행
    for i in range(n // 2, 0, -1):  
        heapify(arr, n, i)
        print("i =", i, arr[1:])    # 현재 단계에서 힙이 어떻게 변하는지 출력

    print() # 줄바꿈

    # 2단계: 힙에서 최대값을 하나씩 꺼내어 정렬
    # 루트(최대값)를 배열의 맨 뒤로 보내고,
    # 힙 크기를 줄인 뒤 다시 heapify하여 힙 속성을 유지
    # 이 과정을 반복하면 뒤에서부터 정렬이 완성된다.
    for i in range(n, 1, -1):
        temp = arr[1]          # 루트와 맨 마지막 요소 교환 (최대값을 고정 위치로 이동)
        arr[1] = arr[i]
        arr[i] = temp
        heapify(arr, i - 1, 1)            # 힙 크기(i-1)만큼 다시 최대 힙이 되도록 조정
        print("i =", i, arr[1:])          # 정렬 과정 출력

# 힙 테스트 프로그램
if __name__ == "__main__":
    data = [None, 5, 3, 8, 4, 9, 1, 6, 2, 7]		# 힙에 삽입할 데이터
    print("\n제자리 정렬")
    print("정렬전:", data[1:])
    heapSort(data)
    print("정렬후:", data[1:])