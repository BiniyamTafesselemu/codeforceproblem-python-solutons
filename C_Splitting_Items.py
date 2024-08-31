n=int(input())
for i in range(n):
    items,increase_amount=map(int,input().split())
    costs=list(map(int, input().split()))
    costs.sort(reverse=True)
    maxx=costs[0]
    for k in range(len(costs)):
        if costs[k]+increase_amount>=maxx:
            costs[k]=maxx
        else:
            costs[k]+=increase_amount
    A=0
    B=0
    for l in range(len(costs)):
        if l%2==0:
            A+=costs[l]
        else:
            B+=costs[l]
    print(A-B)

# "https://codeforces.com/problemset/problem/2004/C"