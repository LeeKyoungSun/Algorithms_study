class BSTNode: #이진 탐색 트리를 위한 노드 클래스
   def __init__(self, key, value):  #생성자: 키와 값을 받음
        self.key = key
        self.value = value  #key를 제외한 데이터 부분
        self.left = None    #왼쪽 자식 링크
        self.right = None   #오른쪽 자식 링크
#이진 탐색 트리의 탐색 연산: 순환 구조
def search_bst(n, key) : #n을 루트로 갖는 이진 탐색 트리에서 킷값이 key인 노드를 찾는 순환 함수
        if n == None :
            return None #n이 None이면 공백 트리이므로 None 반환
        elif key == n.key :
            return n    #n의 키가 탐색키와 같으면 n반환
        elif key < n.key :
            return search_bst(n.left,key)   #탐색키가 n의 키보다 작으면 왼쪽 서브 트리 탐색
        else:
            return search_bst(n.right,key)  #탐색키가 n의 키보다 크면 오른쪽 서브 트리 탐색
#이진 탐색 트리의 값을 이용한 탐색: 전위 순회
def search_value_bst(n, value): #n을 루트로 갖는 이진 탐색 트리에서 키가 아닌 값으로 노드를 찾는 함수
        if n == None : return None
        elif value == n.value : # 루트 탐색: 공백 트리거나 탐색 성공이면 결과를 반환하고 종료
            return n
        res= search_value_bst(n.left,value)
        if res is not None :    # 왼쪽 서브 트리 탐색: 왼쪽 서브 트리에서 탐색 성공이면 결과 반환
            return res
        else:
            return search_value_bst(n.right,value)  #오른쪽 서브 트리 탐색
#이진 탐색 트리의 삽입 연산
def insert_bst(root, node):
    if root is None:
        return node
    if node.key < root.key :
        root.left = insert_bst(root.left, node)
    elif node.key > root.key :
        root.right = insert_bst(root.right, node)
    return root

def delete_bst(root, key):
    if root == None :   #공백 트리
        return root

    if key < root.key :
        root.left = delete_bst(root.left, key)
    elif key > root.key :
        root.right = delete_bst(root.right, key)

    #key가 루트의 키와 같으면 root를 삭제
    else:
        #case1(단말노드) 또는 case2(오른쪽 자식만 있는 경우)
        if root.left == None :
            return root.right   #삭제할 노드 위치에 오른쪽 자식을 끌어올림 > 즉 오른쪽 자식을 반환
        #case2(왼쪽 자식만 있는 경우)
        if root.right == None :
            return root.left    #삭제할 노드 위치에 왼쪽 자식을 끌어올림 > 즉 왼쪽 자식을 반환
        #case3(두 자식이 모두 있는 경우)
        succ=root.right
        while succ.left != None :#후계자를 찾고(오른쪽 서브트리 최소노드)
            succ = succ.left     #후계자의 데이터(key,value)를 복사하고

        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, root.key)#마지막으로, 후계자 삭제(오른쪽 서브 트리에서
    return root
def print_node(msg,n) :
    print(msg,n if n != None else '탐색실패')

def preorder(node):
    if node is not None:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

def print_tree(msg,r) :
    print(msg,end='')
    preorder(r)
    print()

data=[(6,"여섯"), (8,"여덟"),(2,"둘"),(4,"넷"),(7,"일곱"),(5,"다섯"),(1,"하나"),(9,"아홉"),(3,"셋"),(0,"영")]

root = None
for i in range(0,len(data)):
    root = insert_bst(root, BSTNode(data[i][0],data[i][1]))  # root에 반환된 값을 재할당

print_tree("최초: ",root)

n = insert_bst(root,3);             print_node("srch 3: ",n)
n = insert_bst(root,8);             print_node("srch 8: ",n)
n = insert_bst(root,0);             print_node("srch 0: ",n)
n = insert_bst(root,10);            print_node("srch10: ",n)
n = search_value_bst(root,"둘");   print_node("srch둘: ",n)
n = search_value_bst(root,"열");   print_node("srch열: ",n)

n = delete_bst(root,7);             print_tree("del 7: ",root)
n = delete_bst(root,8);             print_tree("del 8: ",root)
n = delete_bst(root,2);             print_tree("del 2: ",root)
n = delete_bst(root,6);             print_tree("del 6: ",root)
