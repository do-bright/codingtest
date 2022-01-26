'''
*
**
***
****
*****
'''
a = int(input())
for i in range(a):
    for j in range(i+1):
        print("*",end='')
    print('')

# 해석 
# print("*",end='') ; 한 줄로 별 출력 
# 원래 print default는 한 줄 띄우기 인데 end='' 붙이면 한 줄로 출력됌 
# print('') ; 줄 바꾸기 (print default는 한 줄 띄우기)
# 줄 단위로 바뀌는 거라 i 문에 들어감

# 관련 개념 
# print('') ; 한 줄 띄우기 
# print('') + end= '' ; 한 줄 안에 출력
# print('') + sep= '' ; 공백없이 출력

# 별 찍기
# *      줄 0  별 1 (줄+1)
# **     줄 1  별 2
# ***    줄 2  별 3
# 줄 0 부터 a 까지
# 별 0 부터 i+1 까지
# 별은 줄(i)을 사용해서 표현 !




