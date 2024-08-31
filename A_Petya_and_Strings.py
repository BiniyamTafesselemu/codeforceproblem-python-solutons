letter1=str(input())
letter2=str(input())
if letter1.lower()==letter2.lower():
    print(0)
for i in range(len(letter1)):
    if ord(letter1[i].lower())<ord(letter2[i].lower()):
        print (-1)
        break
    elif ord(letter1[i].lower())>ord(letter2[i].lower()):
        print (1)
        break
# "https://codeforces.com/problemset/problem/112/A"
