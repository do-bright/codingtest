N,M = map(int,input().split())
list = []
min_list=[]
for _ in range(N):
    a = input().split()
    list.append(a)

for i in range(N):
    min_list.append(min(list[i]))

print(max(min_list))


# 문제 접근 방식 ( 보자마자 떠오른 방식 ) -> only 내 생각 
# 리스트 형태를 만들어 놓고 그 안에 리스트로 입력 값을 넣자
# 그 다음 그 안에 리스트 중에서 최소 값을 구하고 
# 그 최소값들을 모은 리스트를 만든 다음에 거기서 최대값을 구하자 
# a = [] -> a = [['1','2','3'],['4','5','6'],...]

# 첫 시도 문제점 : 리스트 안에 리스트를 넣으려면 어떻게 코드를 작성해야하지 ? 
# -> 해결 : 리스트 하나 만들어 놓고 for 문 돌아가면서 입력 받으며 + 리스트.append() 사용
# list=[] -> list.append() ; 리스트 안에 리스트 생성 

# 두번째 시도 문제점 :  코드 짤 때 for 문에 넣는 게 잘 되지 않음
# -> 해결 : 수로 표현한 다음에 for문으로 바꿈  
    # print(min(list[0]))
    # print(min(list[1]))
    # print(min(list[2]))
    # -> min(list[i])

# 관련 개념 ; min() 최소값 구하기 max() 최대값 구하기, 매개변수 안에는 함수 넣기 가능 


# 교재 답안
# 내가 쓴 코드랑 차이 
# 나 : 입력을 다 받고 그 중에서 최소 값을 구하고 최종 최대 값을 구함 / 리스트안에 리스트 방식 사용 
# 답안 : 입력을 받으면서 최소 값을 구하고 최대 값을 구함 / 하나의 리스트 (리스트에 넣을 때 한 줄마다 입력받으니까 그 한줄마다 최소 값 구하는 방법)

'''
N,M= map(int,input().split())

result = 0
for i in range(N):
    data = list(map(int,input().split()))
    min_value=min(data)
    result = max(result,min_value)
print(result)

'''