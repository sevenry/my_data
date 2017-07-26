#归并排序
#testaaa
import numpy
def divide(a):
	n=len(a)
	if n==1:return a
	else:
		k=n/2
		b=a[:k]
		c=a[k:]
		b=divide(b)
		c=divide(c)
		s=merge(b,c)

	return s


def merge(b,c):
	s=[]
	while b!=[] and c!=[]:
		if b[0]<c[0]:
			s.append(b[0])
			b.remove(b[0])
		else:
			s.append(c[0])
			c.remove(c[0])
	if b==[]:
		for num in c:
			s.append(num)
	if c==[]:
		for num in b:
			s.append(num)
	return s


a=[3,2,5,1]
print(divide(a))



