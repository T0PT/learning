x=int(input())
y=input()
xy=set()
for i in range(1, len(y)-1,3):    
    xy.add(y[i])    
z=input()
xz=set()
for i in range(1, len(z)-1,3):    
    xz.add(z[i])   
w=xy.union(xz)
print(w)
print(x-len(w))



z=int(input())+1
it=set()
while(True):
    it=set()
    x=z
    for i in range(0,4):
        it.add(x%10)
        x-=x%10
        x/=10
    if len(it)==4: break
    z+=1
print(z)
        
        



x='toosmallword'
x=set(x)
if len(x)==26: print('Yes')
else:print('NO')



x=[1, 3, 2]
y=[4, 3, 2]
y=set(y)
ans=y.difference(x)
print(ans)



x=[1, 3, 2]
x=set(x)
y=[4, 3, 2]
ans=x.intersection(y)
print(ans)





x=set()
i=str(input())
for idi in range(1,len(i)-1,3):    
    x.add(i[idi])
print(len(x))



x=set()
i=str(input())
d=0
for idi in range(0,len(i),2):
    x.add(i[idi])
    if len(x)==d: print('YES')
    else:print('NO')
    d=len(x)




x={1, 3, 2}
s=0
y={4, 3, 2}
x=list(x)
for i in x:
    if i in y: s+=1
print(s)



x={1, 2, 3, 4, 5, 1, 2, 1, 2, 7, 3}
print(len(x))
