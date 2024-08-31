arr=[]
ans=0
for i in range(5):
    x=list(map(int, input().split()))
    arr.append(x)
for j in range(len(arr)):
    for k in range(len(arr)):
        if arr[j][k]==1:
            add=abs(2-j)+abs(2-k)
            ans+=add
            print(ans)
            break
# "https://codeforces.com/problemset/problem/263/A"