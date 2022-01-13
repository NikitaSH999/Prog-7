print(' F = ((A -> B) and A) <-> (A and B)')
print('','-'*17)
print('|  A  |  B  |  F  |')
print('','-'*17)
n = 2
A = [1,0]
B = [1,0]
for i in range(n):
	for j in range(n):
		if A[i]==1 and B[j]==0:
			c = 0
		else:
		    c = 1
		if c==1 and A[i]==1:
			c = 1
		else:
			c = 0
		if A[i]==1 and B[j]==1:
			znak = 1
		else:
		    znak = 0
		if c==znak:
			znak = 1
		else:
			znak = 0
		print('| ',A[i],' | ',B[j],' | ',znak,' |')
		print('','-'*17)