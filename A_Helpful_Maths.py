add=str(input())
arr=[]
for i in add:
    if i!="+":
        arr.append(i)
arr.sort()
ans="+".join(arr)
print(ans)
# "https://codeforces.com/problemset/problem/339/A"