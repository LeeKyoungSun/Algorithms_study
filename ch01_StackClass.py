class ArrayStack :
    def __init__(self, capacity) :
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self) : return self.top == -1
    def isFull(self) : return self.top == self.capacity-1

    def push(self, item) :
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = item
        else :  pass

    def pop(self) :
        if not self.isEmpty() :
            self.top -= 1
            return self.array[self.top+1]
        else : pass

    def peek(self) :
        if not self.isEmpty() :
            return self.array[self.top]
        else : pass

    def size() :return top+1

# 문자열 역순 출력 프로그램:Stack
s = ArrayStack(100) #ArrayStack의 매개변수 capacity에 100이 전달되어 용량이 100인 스택 객체 생성

msg = input("문자열 입력 : ") # 문자열을 입력받아 msg에 저장하고 각 문자를 c를 순서대로 스택에 삽입
for c in msg :
    s.push(c)

print("문자열 출력 : ", end='')
while not s.isEmpty() :
    print(s.pop(),end='') #스택이 공백이 아닐 때까지 반복

print()

#문자열 역순 출력 프로그램:list

s = list()

msg = input("문자열 입력 : ")
for c in msg :
    s.append(c)

print("문자열 출력 : ", end='')
while len(s) > 0 :
    print(s.pop(),end='') #스택이 공백이 아닐 때까지 반복

print()
#문자열 역순 출력 프로그램:LifoQueue
import queue
s = queue.LifoQueue(maxsize=100)

msg = input("문자열 입력 : ")
for c in msg:
    s.put(c)

print("문자열 출력 : ", end='')
while not s.empty():
    print(s.get(), end='')  # 스택이 공백이 아닐 때까지 반복

print()