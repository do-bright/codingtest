'''
*****
****
***
**
*
'''
# 
a = int(input())
for i in range(a):
    for j in range(a-i):
        print("*",end='')
    print('')
    

# 해석 
# print(" ",end='') ; 한 줄로 공백 출력 
# print("*",end='') ; 한 줄로 별 출력 
# 원래 print default는 한 줄 띄우기 인데 end='' 붙이면 한 줄로 출력됌 
# print('') ; 줄 바꾸기 (print default는 한 줄 띄우기)
# 줄 단위로 바뀌는 거라 i 문에 들어감

# 관련 개념 
# print('') ; 한 줄 띄우기 
# print('') + end= '' ; 한 줄 안에 출력
# print('') + sep= '' ; 공백없이 출력

# 별 찍기 ex) a=5
# ***** 줄 i = 0  별 5 (a-i)
# ****  줄 i = 1  별 4
# ***   줄 i = 2  별 3
# 줄 0 부터 a 까지
# 별 0 부터 a+i 까지
# 별은 줄(i)을 사용해서 표현 !

# 개선
# 처음엔 별 + 공백 출력해야 하나 했음 
# But 별이 먼저 출력 되면 공백은 굳이 출력을 안 해줘도 됌 !
# 밑에가 개선 전 버전 (공백 + 별 출력)
'''
for i in range(a):
    for j in range(a-i):
        print("*",end='')
    for j in range(i):
        print(" ",end='')
    print('')
'''





