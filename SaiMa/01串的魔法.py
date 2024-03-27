n, K = map(int, input().split())
nums = list(map(int, input().strip().split()))
left = 0
max_length = 0
zero_cnt = 0
for right in range(n):
    if nums[right] == 0:
        zero_cnt += 1
    while zero_cnt > K:
        if nums[left] == 0:
            zero_cnt -= 1
        left += 1
    max_length = max(max_length, right - left + 1)
print(max_length)