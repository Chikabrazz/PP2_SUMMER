n = int(input())
sum = 0
# sum == n * (n + 1) // 2
for i in range(1, n + 1):
    sum += i

for i in range(n - 1):
    sum -= int(input())
print(sum)