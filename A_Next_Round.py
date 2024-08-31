n,k=list(map(int,input().split()))
count=0
arr=list(map(int,input().split()))
if k<=n:
    for j in arr:
        if j >=arr[k-1] and j>0:
            count+=1
        else:
            break
print(count)
# "https://codeforces.com/problemset/problem/158/A"