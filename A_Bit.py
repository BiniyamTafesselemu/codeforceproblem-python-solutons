n=int(input())
count=0
for i in range(n):
    operations=input()
    if operations=="++X"or operations=="X++":
        count+=1
    else:
        count-=1
print(count)
# https://codeforces.com/problemset/problem/282/A