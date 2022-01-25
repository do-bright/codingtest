
# ver2 Upgrade
N,M,K = map(int,(input().split()))
list= list(map(int,input().split()))
print(list)

list.sort(reverse=True)
print(list)

first = list[0]
second = list[1]

second_count = M/(K+1)
first_count = M-second_count

sum = first*first_count+second*second_count
print(int(sum))

# 업그레이드 버전 (수열 이용)
# 결국 가장 큰 수와 두번째 큰 수만을 사용하는 순열의 관점으로 볼 수 있음
# 가장 큰 수를 K 개수 만큼 써주고 두번째 큰 수를 1번씩 넣어주는 거
# 그럼 수열 길이 = K(가장 큰 수)+1(두번째 큰 수)
# 사실상 두번째 큰 수를 사용하는 횟수는 수열을 반복하는 횟수만큼임 수열길이당 1이니까 
# -> 해결 : M/(K+1)
# 그리고 가장 큰 수를 사용한 횟수는 전체 횟수 - 두번째 큰 수 사용 횟수겠지
# 결국 구해야 할 건 sum 이기 때문에 리스트 순서 고려안하고 그냥 어떤 값을 몇 번 쓰냐만 알면 됌 


''' ver1 단순
N,M,K = map(int,(input().split()))
list= list(map(int,input().split()))
print(list)

list.sort(reverse=True)
print(list)

first = list[0]
second = list[1]

sum=0
while(True):
  for _ in range(K):
    if(M == 0):
      break
    sum += first
    M-= 1
  if (M==0):
    break
  sum += second
  M-=1
'''
  
# 첫 시도 문제점 : 리스트를 큰 수대로 정렬해야하는데 어떻게 해야할지 몰라서 for문 + max 사용 굴레에 빠짐
# -> 해결 : 굳이 리스트를 큰 수대로 정렬할 필요가 없음, 가장 큰 수랑 두번째로 큰 수 두 개만 알면 됌 (나머지 수는 최대를 만들 수 없기 때문 = 문제 조건에 필요 없는 수들)
# -> 해결 2 : max 말고 sort 쓰면 알아서 정렬해줌
# 리스트.sort ; 작은 수 부터 정렬 / 리스트.sort(reverse=True) ; 큰 수부터 정렬

# 두번째 시도 문제점 : 첫번째로 큰 수랑 두번째로 큰 수 뽑고 for 문으로 더해줘야 하는데 범위 잡는데에서 어려움에 빠짐
# -> 해결 : while True 쓰면 굳이 범위를 안 잡아줘도 됌 
# while True ; 무한 도는데 break 기준을 만나면 탈출 ! 무한 루프 = 범위 안잡아줘도 됌 + 탈출 기준만 잡아주면 됌 

