## 내가 짠 코드 ##
import sys
input = sys.stdin.readline
print = sys.stdout.write

input_list = []
num = 0
index = 0
for i in range(3):
    a = input()
    input_list.append(a)

for value in input_list:
    index +=1
    try:
        num = int(value)
        break
    except(ValueError, TypeError):
        pass

num += 4-index



if(num%3==0 and num%5==0):
    print("FizzBuzz\n")
elif(num%3==0):
    print("Fizz\n")
elif(num%5==0):
    print("Buzz\n")
else:
    print(str(num) +"\n")



#### GPT식 코드 ##### 
input_list = []
for _ in range(3):
    input_list.append(input().strip())  # 입력 받기 (줄바꿈 제거)

# i를 찾기
start_i = None
for idx, val in enumerate(input_list):
    if val.isdigit():
        # val이 숫자라면
        start_i = int(val) - idx
        break

# 찾은 i를 기반으로, 다음 값을 찾는다
next_i = start_i + 3

# FizzBuzz 규칙 적용
if next_i % 3 == 0 and next_i % 5 == 0:
    print("FizzBuzz")
elif next_i % 3 == 0:
    print("Fizz")
elif next_i % 5 == 0:
    print("Buzz")
else:
    print(next_i)