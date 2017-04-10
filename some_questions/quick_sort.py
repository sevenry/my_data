#快速排序

def divide2(a):
	n=len(a)
	print(a)
	if n == 1:return a
	if n == 2:
		if a[0]>a[1]:return [a[1],a[0]]
		else:return a
	else:
		k1 = a[0]
		k2 = a[n-1]
		k3 = a[int(n/2)]
	comp = min(k1,k2)
	if comp<k3:
		comp=min(max(k1,k2),k3)
	print(comp,'w')

	b=[]
	c=[]
	for num in a:
		if num<comp:
			b.append(num)
		            
		else:
			c.append(num)
	print(c,'c')
	print(b,'b')
    
	b = divide2(b)
	c = divide2(c)

	for max_num in c:
		b.append(max_num)
	return b



