'''
    *
   **
  ***
 ****
*****
'''
a = int(input())
for i in range(a):
    for j in range(a-i-1):
        print(" ",end='')
    for j in range(i+1):
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
# _ _ _ _ *    줄 i=0  별 1 공백 4
# _ _ _  **    줄 i=1  별 2 공백 3
# _ _   ***    줄 i=2  별 3 공백 2
# 줄 0 부터 a 까지
# 별 0 부터 i+1 까지
# 공백 0 부터 a-i-1 까지
# 별과 공백은 줄(i) + 입력값(a)을 사용해서 ( = 줄과 변수를 기준으로 ) 표현 !




