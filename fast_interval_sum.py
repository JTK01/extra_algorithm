N, left, right = map(int,input().split())
data = list(map(int,input().split()))

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

print(prefix_sum[right] - prefix_sum[left - 1])
