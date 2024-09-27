from ch02_ArrayQueue import ArrayQueue

class CircularDeque(ArrayQueue):
    def __init__(self, capacity=10): #생성자는 상속되지 않으므로 다시 구현
        super().__init__(capacity)#부모 클래스의 데이터만 초기화하면 되므로 부모(super())의 생성자 직접 호출

    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front-1+self.capacity)%self.capacity
        else : pass

    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear];
            self.rear = (self.rear-1+self.capacity)%self.capacity
        else : pass

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else : pass

#원형 덱의 테스트 프로그램
dq = CircularDeque()

for i in range(9):
    if i%2==0 : dq.addRear(i) #i가 짝수면 후단, 홀수면 전단으로 삽입
    else : dq.addFront(i)
dq.display("홀수는 전단 짝수는 후단 삽입")

for i in range(2) : dq.deleteFront()
for i in range(3) : dq.deleteRear()
dq.display("전단 삭제 2번 , 후단 삭제 3번")

for i in range(9,14) : dq.addFront(i) #9~13을 전단으로 삽입
dq.display("전단에 9~13 삽입")