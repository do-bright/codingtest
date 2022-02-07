N,K = map(int,input().split())
count = 0

while True:
    target = (N//K) *K
    count += (N-target)
    N = target 
    if N<K:
        break
    count += 1
    N //= K

count += (N-1)
print(count)
    
# 문제 접근 방식 ( 보자마자 떠오른 방식 ) -> only 내 생각 
# 과정을 최대한 적게 거쳐야하니까
# N%K 가 0이 될 때까지 (나눠질 때까지) -1을 한다음
# N%K 가 0이 되면 N/k 하기

# 첫 시도 문제점 : while 반복문이 두개나 있어서 시간이 많이 걸릴 거 같다
# -> 해결 : while을 하나만 사용하기 
# list=[] -> list.append() ; 리스트 안에 리스트 생성 

# 첫번째 시도 
# N,K = map(int,input().split())
# count=0

# while(N%K!=0):
#     N = N-1
#     count=count+1
# while(N!=1):
#     N = N%K
#     count=count+1
# print(count)

# 두번째 시도 문제점 : while 을 하나만 사용했으나, 나눠질 때까지 -1을 해야하니까
# 여전히 시간 낭비가 많음 
# -> 도저히 모르겠어서 답안 참고 후 해석하는 방식을 택함 

# 두번째 시도 
# N,K = map(int,input().split())
# count=0

# while True:
#     if(N%K==0):
#         N = N%K
#         count=count+1      
#     else:
#         N = N-1
#         count=count+1
#     if (N==1):
#         break
# print(count)

# 교재 답안
# 내가 쓴 코드랑 차이 
# 나 : 단순 접근
# 답안 : 거꾸로 접근
# N이랑 가장 가까운 K의 배수를 target으로 구함 -> N과 target과 차이를 구함 = 1을 빼준 횟수
# 즉, N에서 1을 빼는 과정을 target이라는 값과의 차이를 구하는 과정으로 바꿔 시간을 줄여줌
# target은 K에 나눠 떨어짐 
# ex) N K 17 4 
# 여기서 17이랑 가장 가까운 4의 배수 = 16
# 17(N)-16(target) = 1 = 1을 빼준 횟수의 합 
 

    