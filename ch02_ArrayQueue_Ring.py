class ArrayQueue:
    def __init__(self, capacity=10):  # 생성자 정의
        self.capacity = capacity  # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0  # 전단 인덱스
        self.rear = 0  # 후단 인덱스

    def isEmpty(self):  # 공백 상태
        return self.front == self.rear

    def isFull(self):  # 포화 상태
        return self.front == (self.rear + 1) % self.capacity

    def dequeue(self):  # 맨 앞의 요소를 삭제하는 dequeue 연산
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            pass

    def peek(self):  # 상단 들여다보기 연산
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            pass

    def size(self):  # 전체 요소의 수
        return (self.rear - self.front + self.capacity) % self.capacity

    def display(self, msg):  # 전체 요소를 화면으로 출력, msg는 큐의 이름이나 메세지를 출력하기 위한 매개변수
        print(msg, end='= [ ')
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i % self.capacity], end=' ')  # front+!부터 size()개의 요소를 순서대로 출력
        print(" ]")

    def enqueue2( self , item ):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty():
            self.front = (self.front+1)%self.capacity


# 링 버퍼 테스트 프로그램
q = ArrayQueue(8)  # 큐 객체를 생성(cap

q.display("초기 상태")
for i in range(6) :
    q.enqueue2(i)
q.display("삽입 0-5")

q.enqueue2(6); q.enqueue2(7)
q.display("삽입 6,7")     #여기서 큐가 포화 상태

q.enqueue2(8); q.enqueue2(9) #포화 상태로 가장 오래된 요소 2개가 삭제
q.display("삽입 8,9")

q.dequeue(); q.dequeue()
q.display("삭제 x2")