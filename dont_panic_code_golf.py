a,b,c,d,e,f,g,h=[int(i) for i in input().split()]
m=dict()
for i in range(h):
 n,o=[int(j) for j in input().split()]
 m[n]=o

while True:
 p=input().split()
 q=int(p[0])
 r=int(p[1])
 s=p[2]

 t=e if q==d else m[q]if q in m else r
 if(r==t):print("WAIT")
 else:
  u="RIGHT" if r<t else "LEFT"
  print("BLOCK" if s!=u else "WAIT")
