class Node :
    def __init__(self, elem,link=None):#link는 default 인수
        self.data = elem               #데이터 멤버 생성 및 초기화
        self.link = link               #링크 생성 및 초기화

    def append(self, node):       #self 다음에 node를 넣는 연산
        if node is not None:
            node.link = self.link #삽입할 노드가 None이 아니면 node를 다음 노드에 연결
            self.link = node

    def popNext(self):       #self의 다음 노드를 삭제하는 연산
        next = self.link     #현재 노드(self)의 다음 노드
        if next is not None:
            self.link = next.link
        return next          #다음 노드를 반환

class LinkedList() :     #단순 연결 리스트 클래스
    def __init__(self):
        self.head = None #Head를 선언하고 None으로 초기화

    def isEmpty(self):           #공백 상태 검사
        return self.head == None #Head가 None이면 공백

    def isFull(self): #포화 상태 검사
        return False  #연결된 구조에서는 포화 상태 없음

    def getNode(self, pos):
        if pos < 0 : return None #잘못된 위치면 None을 반환
        ptr = self.head          #시작 위치는 head
        for i in range(pos):
            if ptr== None:       #head 노드에서부터 링크를 따라 pos번 이동하면 pos 위치의 노드에 도착
                return None
            ptr = ptr.link
        return ptr               #최종 노드를 반환

    def getEntry(self, pos):
        node = self.getNode(pos)    #pos번째 노드를 구함
        if node is None: return None#해당 노드가 없는 경우
        else: return node.data      #있는 경우 데이터 필드 반환

    def insert(self, pos, e):
        node = Node(e,None)         #삽입할 새로운 노드를 만듬
        before = self.getNode(pos-1)     #삽입할 위치 이전 노드 탐색, pos번 이동이 필요
        if before == None:
            node.link = self.head   #before가 None이면 맨 앞에 추가, 리스트의 head node가 변경됨
            self.head = node
        else : before.append(node)  #아닌 경우 before뒤에 추가

    def delete(self, pos):
        before = self.getNode(pos-1)#삭제할 위치 이전 노드를 탐색
        if before == None:
            before = self.head      #head node를 삭제하면 head가 다음 노드로 변경
            if self.head is not None :
                self.head = self.head.link
            return before
        else : return before.popNext()

    def size(self):
        ptr = self.head
        count = 0;
        while ptr is not None : #ptr이 none이 아닌 동안
            ptr = ptr.link      #link를 따라 ptr 이동
            count += 1          #이동할 때마다 count 증가
        return count            #count 반환

    def replace(self, pos, e):
        node = self.getNode(pos)  # pos번째 노드를 구함
        if node is None:
            print("위치가 범위를 벗어났습니다.")
        else:
            node.data = e  # 노드의 데이터 필드를 새로운 값으로 교체

    def display(self, msg='LinkedList'):
        print(msg,end=' ')
        ptr = self.head
        while ptr is not None :
            print(ptr.data,end='->')
            ptr = ptr.link
        print('None')



#단순 연결 리스트(linked list)
s=LinkedList()
s.display('연결리스트( 초기 ): ')
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.insert(s.size(),40)
s.insert(2,50)
s.display("연결리스트(삽입x5): ")
s.replace(2,90)
s.display("연결리스트(교체x1): ")
s.delete(2)
s.delete(3)
s.delete(0)
s.display("연결리스트(삭제x3): ")

#파이썬의 리스트
l=[]
print('파이썬list( 초기 ): ', l)
l.insert(0,10)
l.insert(0,20)
l.insert(1,30)
l.insert(len(l), 40)
l.insert(2,50)
print('파이썬list(삽입x5): ',l)
l[2] = 90
print('파이썬list(교체x1): ',l)
l.pop(2)
l.pop(3)
l.pop(0)
print('파이썬liset(삭제x3): ',l)