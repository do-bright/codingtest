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
  