capacity = 10
array = [None]*capacity
top = -1
print(array)

def isEmpty():
    if top == -1 : return True
    else :  return False

def isFull() : return top == capacity - 1

def push(e) :
    global top
    if not isFull() :
        top += 1
        array[top] = e
    else :
        print("stack overflow")
        exit()

def pop() :
    global top
    if not isEmpty() :
        del array[top]
        top -= 1
        return array[top+1]
    else:
        print("stack underflow")
        exit()

push(5)
push(6)
pop()
print(array)