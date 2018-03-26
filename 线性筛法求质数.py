import os
from PIL import Image
a=list(range(50))
is_prime=[True]*len(a)
father=a[:]
primes=[]
for i in range(2,len(a)):
    if is_prime[i]:
        primes.append(i)
    for j in primes:
        if j*i>=len(a):break
        is_prime[j*i]=False
        father[j*i]=i
        if j%i==0:
            break
print(primes)
filename=os.path.splitext(__file__)[0]+".dot"
with open(filename,"w",encoding='utf8') as f:
    f.write('digraph mygraph{rankdir="LR";')
    for i in range(2,len(a)):
        if father[i]!=i:
            f.write("%d->%d;"%(father[i],i))
    f.write("}")
os.system("dot -Tjpg %s -O"%(filename))#-O表示按照当前名称输出
Image.open("%s.jpg"%filename).show()
