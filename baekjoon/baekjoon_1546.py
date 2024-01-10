n = input()
numbers = list(map(int, input().split()))

M = max(numbers)

modified_numbers = [number / M * 100 for number in numbers]

print(sum(modified_numbers)/len(modified_numbers))

