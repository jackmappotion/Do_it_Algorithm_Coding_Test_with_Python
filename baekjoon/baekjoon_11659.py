import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_sum = [0]
tmp = 0

for number in numbers:
    tmp += number
    prefix_sum.append(tmp)

results = list()
for _ in range(M):
    st, end = map(int, input().split())
    results.append(prefix_sum[end] - prefix_sum[st - 1])

for result in results:
    print(result)
