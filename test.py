a=int(input())
b=int(input())
c=int(input())
flag="NO" 
for i in range (0,a):
    x=(a-(b*i))%c
    if x==0:
        d=(a-b*i)//c
        if i>0 and d>0:
            print("YES")
            print(i,d)
            flag="YES"
if flag!="YES":
    print("NO")
