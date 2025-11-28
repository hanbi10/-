"""
이진 탐색 트리 (Binary Search Tree)
응급도를 기준으로 환자를 트리에 저장
"""

class PatientNode:
    """이진 트리의 노드 - 환자 한 명을 저장"""
    def __init__(self, patient):
        self.patient = patient  # 환자 정보
        self.left = None  # 왼쪽 자식 (응급도가 더 낮은 환자)
        self.right = None  # 오른쪽 자식 (응급도가 더 높은 환자)


class PatientBST:
    """환자 관리 이진 탐색 트리"""
    def __init__(self):
        self.root = None  # 루트 노드
    
    def insert(self, patient):
        """환자를 트리에 삽입 (응급도 기준)"""
        if self.root is None:
            self.root = PatientNode(patient)
            print(f"✓ {patient['이름']} 환자 등록 (응급도 {patient['응급도']})")
        else:
            self._insert_recursive(self.root, patient)
    
    def _insert_recursive(self, node, patient):
        """재귀적으로 적절한 위치에 삽입"""
        # 응급도가 낮으면 왼쪽으로
        if patient['응급도'] < node.patient['응급도']:
            if node.left is None:
                node.left = PatientNode(patient)
                print(f"✓ {patient['이름']} 환자 등록 (응급도 {patient['응급도']})")
            else:
                self._insert_recursive(node.left, patient)
        # 응급도가 높거나 같으면 오른쪽으로
        else:
            if node.right is None:
                node.right = PatientNode(patient)
                print(f"✓ {patient['이름']} 환자 등록 (응급도 {patient['응급도']})")
            else:
                self._insert_recursive(node.right, patient)
    
    def inorder_traversal(self):
        """중위 순회: 응급도 낮은 순으로 출력 (왼쪽 → 루트 → 오른쪽)"""
        print("\n=== 응급도 순서 (낮은 순) ===")
        self._inorder_recursive(self.root)
    
    def _inorder_recursive(self, node):
        """재귀적으로 중위 순회"""
        if node is not None:
            self._inorder_recursive(node.left)
            print(f"- {node.patient['이름']}: 응급도 {node.patient['응급도']} ({node.patient['증상']})")
            self._inorder_recursive(node.right)
    
    def find_urgency(self, urgency_level):
        """특정 응급도의 환자들 찾기"""
        result = []
        self._find_urgency_recursive(self.root, urgency_level, result)
        return result
    
    def _find_urgency_recursive(self, node, urgency_level, result):
        """재귀적으로 특정 응급도 환자 찾기"""
        if node is not None:
            self._find_urgency_recursive(node.left, urgency_level, result)
            if node.patient['응급도'] == urgency_level:
                result.append(node.patient)
            self._find_urgency_recursive(node.right, urgency_level, result)
    
    def show_tree(self, node=None, level=0, prefix="Root: "):
        """트리 구조 시각화"""
        if node is None:
            node = self.root
        
        if node is not None:
            print("  " * level + prefix + 
                  f"{node.patient['이름']} (응급도 {node.patient['응급도']})")
            
            if node.left is not None or node.right is not None:
                if node.left:
                    self.show_tree(node.left, level + 1, "L--- ")
                else:
                    print("  " * (level + 1) + "L--- (없음)")
                
                if node.right:
                    self.show_tree(node.right, level + 1, "R--- ")
                else:
                    print("  " * (level + 1) + "R--- (없음)")


# ===== 메인 실행 =====

# 이진 탐색 트리 생성
bst = PatientBST()

# 환자 데이터
patients = [
    {"이름": "김철수", "나이": 45, "증상": "골절", "응급도": 3},
    {"이름": "이영희", "나이": 28, "증상": "심정지", "응급도": 1},
    {"이름": "박민수", "나이": 35, "증상": "열상", "응급도": 4},
    {"이름": "최지우", "나이": 52, "증상": "심장질환", "응급도": 2},
    {"이름": "정수진", "나이": 19, "증상": "천식", "응급도": 3},
]

# 환자들을 트리에 삽입
print("=== 환자 등록 (이진 탐색 트리) ===")
for patient in patients:
    bst.insert(patient)

# 트리 구조 출력
print("\n=== 트리 구조 ===")
bst.show_tree()

# 중위 순회 (응급도 낮은 순)
bst.inorder_traversal()

# 특정 응급도 환자 찾기
print("\n=== 응급도 3단계 환자 ===")
urgency_3 = bst.find_urgency(3)
for patient in urgency_3:
    print(f"- {patient['이름']} ({patient['증상']})")


