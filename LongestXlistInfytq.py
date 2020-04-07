def check(ii,jj,n,m):
    m.append(n[ii])
    m.append(n[jj])
    a=n[ii]
    b=n[jj]
    sum=a+b
    a=n[jj]
    for iii in range(jj+1,len(n)):
        if sum==n[iii]:
            m.append(n[iii])
            b=n[iii]
            sum=a+b
            a=n[iii]
        else:
            break

n=list(map(int,input().split(",")))
m=[]
mm=[]
for i in range(len(n)-1):
    check(i,i+1,n,m)
    if len(m)>len(mm):
        mm=m
        m=[]
    else:
        m=[]
for i in range(len(mm)):
    if i==len(mm)-1:
        print(mm[i])
    else:
        print(mm[i],end=",")
