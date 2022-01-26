'''
셀프 넘버 = 생성자가 없는 수
생성자 ? 수들의 조합으로 만들어진 수 
ex) 33 = 33 + 3 + 3 = 39
39 = 39 + 3 + 9 = 51
39의 생성자 = 33, 51의 생성자 = 39 
10000보다 작거나 같은 셀프넘버를 한 줄에 하나씩 출력
주의. 어떤 경우는 생성자를 2개 가짐 ex) 101 - 99, 100
'''

def generate(a):
    generated_num=set()
    for i in range(1,a+1):
        for j in str(i):
            i = i +int(j)
        generated_num.add(i)
    return generated_num

num=10000
total_num = set(range(1,num+1))
generated_num = generate(num)
self_num = sorted(total_num-generated_num)
for i in self_num:
    print(i)
    

# 고려사항
# 어떤 수는 생성자를 두개 가짐 
# -> 해결 : 중복을 허용되지 않는 "집합" 사용
# 집합 set ; set("Hello")={'H','l','o','e'} 중복 허용 x 순서 x
    
# 첫 시도 문제점 : 수 10000까지 생성자를 바로 구하려고 하니까 복잡해지면서 막힘
# -> 해결 : 문제접근을 10000까지 생성자를 다 구해야지 라고 가면 안되고, 
# 전체에서 생성자를 가진 수를 빼서 구해야겠다고 생각해야함 

# 두번째 시도 문제점 : 숫자를 어떻게 33 + 3 + 3 이런식으로 나누지 ? 해결 x
# -> 해결 : 숫자를 문자(str)로 바꿔주기 / 문자로 범위에 넣어준 다음, 계산할 땐 숫자로 하기 
# for j in str(i) ; 문자를 범위로 넣어줌 -> ex) 64 를 문자로 바꾸기 때문에 6 4 나눠서 인식함  

# -> 해결 : while True 쓰면 굳이 범위를 안 잡아줘도 됌 
# while True ; 무한 도는데 break 기준을 만나면 탈출 ! 무한 루프 = 범위 안잡아줘도 됌 + 탈출 기준만 잡아주면 됌 
