a = int(input())
list = input().split()
print(list)
x = 1
y = 1
for i in range(len(list)):
    if list[i] == 'R':
        if (y==a):
            continue
        else:
            y = y+1
    elif list[i] == 'L':
        if (y==1):
            continue
        else:
            y = y-1
    elif list[i] == 'U':
        if (x==1):
            continue
        else:
            x = x-1
    elif list[i] == 'D':
        if (x==a):
            continue
        else:
            x = x+1
    else:
        pass
print (x,y)

# 문제 접근 방식 ( 보자마자 떠오른 방식 ) -> only 내 생각
# 우선 숫자 입력받고 경로는 리스트로 저장 
# for문으로 경로의 길이 만큼 돌리면서 if 를 통해 각각의 상황을 나누면 되겠다 생각
# + L R U D 각각의 상황에 맞게 x랑 y가 어떻게 증가하는 지 구분하려 함
# 공간 밖은 무시하는 경우도 생각해줘야 하기에
# 공간 밖이 무시가 되는 경우가 어떻게 될까 보니까
# 위 / 아래 / 왼쪽 / 오른쪽이 각각 없을때임 
# 그걸 어떻게 표현할까 생각한 후 코드 짬

# 첫, 두번째 시도 문제점 : 1. list로 어떻게 받냐 + 2. L R U D 에 맞는 x,y 증가량 틀림, 무시되는 경우 틀림 + 3. while문 사용 
# 1. 리스트로 받는 방법; list = input().split()
# 따로 list= [] + list.append 하지 말고 바로 받으면 리스트 형식으로 받아짐 
# 2. 그림을 통해서 어떻게 흘러가는지 봤어야했는데 L R U D 의미만 생각함 (왼쪽은 x감소, 오른쪽은 x증가 이런식)
# 근데 예시를 넣어서 해보니까 왼쪽은 y감소고 오른쪽은 y증가 였음
# 3. while 문 사용이 필요가 없음 이미 끝점은 정해져있기에 for 문으로 충분함 while 문 사용했다면 탈출 지점이 없음 (break 되는 지점이 x)

# a = int(input())
# b = input().split()
# list = []
# for _ in range(b):
#     blist = input().split()
#     list.append(b)
# print(list)
# x = 0
# y = 0
# while(True):
#     for i in range(len(list)):
#         if b[i] == 'R':
#             if (x==1):
#                 continue
#             x = x+1
#         elif b[i] == 'L':
#             if (x==a):
#                 continue
#             x = x-1
#         elif b[i] == 'U':
#             if (y==1):
#                 continue
#             y = y+1
#         elif b[i] == 'D':
#             if (y==a):
#                 continue
#             y = y-1
#         else:
#             pass
# print (x,y)


# 교재 답안
# 내가 쓴 코드랑 차이 
# 나 : 경로를 리스트로 입력받고 
# for 문을 통해 경로가 L R U D 중 어디에 해당하는지 체크하면서 
# 각 상황에 따라 x y 증가시켜 좌표 구하기 + 공간 벗어나는 경우 특정 수로 표현

# 답안 : L R U D 를 리스트를 이용하여 케이스에 맞게 나누고 x와 y의 움직임 표현
# 리스트가 L R U D 에 해당하는 경우 
# 리스트를 활용해 x y 한 번에 증가 + 공간 벗어나는 경우 곱셈 표현 

'''
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx<1 or ny <1 or nx > n or ny > n:
        continue    
    x,y=nx,ny
print(x,y)
'''
        
                 
            
        
                 
            
        