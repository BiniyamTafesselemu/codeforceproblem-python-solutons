n=int(input())
for i in range(n):
    word=input()
    if len(word)<=10:
        print(word)
    else:
        letters_at_the_mid=len(word)-2
        print(word[0]+str(letters_at_the_mid)+ word[-1])

        
# "https://codeforces.com/problemset/problem/71/A"