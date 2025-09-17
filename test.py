# a=int(input())
# b=int(input())
# c=int(input())
# flag="NO" 
# for i in range (0,a):
#     x=(a-(b*i))%c
#     if x==0:
#         d=(a-b*i)//c
#         if i>0 and d>0:
#             print("YES")
#             print(i,d)
#             flag="YES"
# if flag!="YES":
#     print("NO")

n=int(input())
p=n 
a=[]
b=p//100
p=p%100
a.append(b)
b=p//10
p=p%10
a.append(b)
a.append(p)
a.sort()


# Extracting digits from num2
y=int(input())
k=y
x=[]
z=k//100
k=k%100
x.append(z)
z=k//10
k=k%10
x.append(z)
x.append(k)
x.sort()

# Write logic to check for anagrams
flag="True"
for i in range (len(a)):
    if a[i]==x[i]:
        flag="True"
    else:
        flag="False"



# Print the result (True or False based on the condition)
if flag!="True":
    print ("False")
else:
    print("True")