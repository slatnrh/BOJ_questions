import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)
lst.sort()

print(round(sum(lst) / len(lst)))
print(round(lst[(len(lst)-1)//2]))

dic=dict()
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
mx=max(dic.values())
mx_dic=[]

for i in dic:
    if mx==dic[i]:
        mx_dic.append(i)

if len(mx_dic)>1:
    print(mx_dic[1])
else:
    print(mx_dic[0])

print(max(lst) - min(lst))