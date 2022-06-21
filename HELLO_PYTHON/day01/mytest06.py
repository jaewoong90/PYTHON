
import random

a = input("홀짝을 입력하시오")

arr = ["홀","짝"]

com = random.choice(arr)

print("컴퓨터 : ", com)

if(a == com):
    print("승리")
else:
    print("패배")

