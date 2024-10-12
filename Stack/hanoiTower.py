def hanoi_Tower(n,fr,tmp,to):
    if ( n == 1) :
        print("원판 1: %s --> %s" % (fr,to)) #순환을 멈추는 부분
    else :
        hanoi_Tower(n-1,fr,tmp,to)              #1단계
        print("원판: %d: %s --> %s" % (n,fr,to)) #2단계
        hanoi_Tower(n-1,tmp,to,to)              #3단계

hanoi_Tower(4,'A','B','C')