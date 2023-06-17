n = int(input())
part_f = 1
part_s = 0
for i in range(1, n + 1):
    part_f *= i
    part_s += part_f
print(part_s)