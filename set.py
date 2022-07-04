"""l1=[1,2,3]
s1={1,2,3}
print(type(l1))
print(type(s1))
A=[1,3,5,2,]
S=set(A)
print(S)
for x in S:
    print(x)
S2=set(range(1,6))
print(S2)
sum=0
for x in S2:
    sum=sum+x
print(sum)"""
s2={1,2,3}
s2.add("D")
print(s2)
s2.update({4,"B"})
print(s2)
a={5,6,7}
s2.update(a)
print(s2)
s2.pop()
print(s2)
s2.remove("B")
s2.discard(1)
print(5 in a)
print(len(a))
s2=a
print(s2)
print(a)
s2.remove(5)
print(s2)
print(a)
s1={1,2,3}
s2=s1.copy()

c={1,2,3,4,5,6}
d={4,5,6}
print(c.union(d)) # or |
print(c.intersection(d)) # or &
print(c.difference(d)) #element which are in c and not in d 
print(c ^ d) # the elments other than common are displaced
print(c.isdisjoint(d))
print(d.issubset(c))
print(c.issuperset(d))
l=[1,4,5,5]
s=set(l)
print(s)
T=([1,2,3])
print(T)   
d={[1,2,3]:"divya"}
print(d[1,2,3])