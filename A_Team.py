n = int(input())
count = 0
for i in range(n):
    confidence = list(map(int, input().split()))
    
    if sum(confidence) >= 2:
        count += 1 

print(count)
# "https://codeforces.com/problemset/problem/231/A"