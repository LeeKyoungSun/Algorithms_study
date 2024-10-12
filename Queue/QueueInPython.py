import queue
import random
import collections

#Queue 모듈의 Queue 테스트
q = queue.Queue(8)

print("삽입 순서: ", end= ' ')
while not q.full() :
    v = random.randint(0, 100) #0~99 사이의 정수를 무작위로 발생해 큐에 삽입
    q.put(v)
    print(v, end= ' ')
print( )

print("삭제 순서 : ", end = ' ')
while not q.empty() :
    print(q.get(), end= ' ') #큐가 공백 상태가 될 때까지 요소를 꺼내서 출력
print( )

#collections 모듈의 deque 클래스 테스트
dq = collections.deque()

print("덱은 공백 상태 아님" if dq else "덱은 공백 상태")
for i in range(9):
    if i%2==0 : dq.append(i)
    else : dq.appendleft(i)
print("홀수는 전단 짝수는 후단에 삽입",dq)

for i in range(2): dq.popleft()
for i in range(3): dq.pop()
print("전단 삭제 2번, 후단 삭제 3번", dq)

for i in range(9,14): dq.appendleft(i)
print("전단에 9~13 삽입         ",dq)

print("덱은 공백 상태 아님" if dq else "덱은 공백 상태")