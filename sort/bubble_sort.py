# 중간 과정 출력용 함수
def printStep(arr, val) :
    print(" Step %2d = " % val, end='')
    print(arr)

# 버블 정렬 알고리즘        
def bubble_sort(A) :
    n = len(A)
    # i는 마지막 비교 위치(비교 횟수)를 줄여나감
    for i in range(n-1, 0, -1) :
        bChanged = False         # 교환 발생 여부 확인  
        for j in range (i) :
            if (A[j]>A[j+1]) :   # 왼쪽 레코드가 오른쪽 레코드 비교
                temp = A[j]      # 교환
                A[j] = A[j+1]
                A[j+1] = temp
                bChanged = True  # 교환 발생 표시

        if not bChanged: break;	# 교환이 한번도 없으면 이미 정렬 완료 
        printStep(A, n - i);	#중간 과정 출력용 문장

if __name__ == "__main__":
    org = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]

    data = list(org)
    print("Original  :", org)
    bubble_sort(data)
    print("Bubble    :", data)
    