class ArrayQueue:
    def __init__(self,capacity = 10): #생성자 정의
        self.capacity = capacity      #용량(고정)
        self.array = [None]*capacity  #요소들을 저장할 배열
        self.front = 0                #전단 인덱스
        self.rear = 0                 #후단 인덱스

    def isEmpty(self):                 #공백 상태
        return self.front == self.rear

    def isFull(self):                  #포화 상태
        return self.front == (self.rear+1)%self.capacity

    def enqueue(self, item):                #삽입 연산
        if not self.isFull():               #포화 상태가 아닌 경우
            self.rear = (self.rear+1)%self.capacity
            self.array[self.rear] = item
        else : pass                         #오버플로 오류: 처리 안 함

    def dequeue(self):      #맨 앞의 요소를 삭제하는 dequeue 연산
        if not self.isEmpty():
            self.front = (self.front+1)%self.capacity
            return self.array[self.front]
        else : pass

    def peek(self):         #상단 들여다보기 연산
        if not self.isEmpty():
            return self.array[(self.front+1)%self.capacity]
        else : pass

    def size(self):         #전체 요소의 수
        return (self.rear - self.front + self.capacity) % self.capacity

    def display(self,msg): #전체 요소를 화면으로 출력, msg는 큐의 이름이나 메세지를 출력하기 위한 매개변수
        print(msg, end= '= [ ')
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i%self.capacity], end=' ') #front+!부터 size()개의 요소를 순서대로 출력
        print(" ]")

#원형 큐 테스트 프로그램
import random            #난수 발생을 위해 random 모듈 포함
q = ArrayQueue(8)        #큐 객체를 생성(capacity=8)

q.display("초기 상태")
while not q.isFull() :
    q.enqueue(random.randint(0,100))  #큐가 포화상태가 될 때까지 0-99사이의 정수를 무작위로
q.display("포화 상태")                  #발생하여 큐에 삽입. 용량이 8이므로 7개까지 삽입됨

print("삭제 순서:", end= ' ')
while not q.isEmpty():
    print(q.dequeue(), end= ' ')      #큐가 공백 상태가 될 때까지 요소를 꺼내 화면에 출력
print()