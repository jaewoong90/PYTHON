

a = input("첫수를 입력하시오")
b = input("끝수를 입력하시오")

aa = int(a)
bb = int(b)
arr = range(aa,bb+1)

sum = 0

for i in arr:
    sum += i

print(sum)

