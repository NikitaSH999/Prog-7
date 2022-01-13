print('','-'*21)
print('|  A  |  B  | A and B |')
print('','-'*21)
n = 2
A = [1,0]
B = [1,0]
for i in range(n):
	for j in range(n):
		if (A[i]==1) and (B[j]==1):
			znak = 1
		else:
		    znak = 0
		print('| ',A[i],' | ',B[j],' |   ',znak,'   |')
		print('','-'*21)