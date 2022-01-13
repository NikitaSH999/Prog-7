print(' F = (A or B) and not C')
print('','-'*23)
print('|  A  |  B  |  C  |  F  |')
print('','-'*23)
n = 2
A = [1,0]
B = [1,0]
C = [1,0]
for i in range(n):
	for j in range(n):
		for k in range(n):
			if (A[i]==1 or B[j]==1) and C[k]!=1:
				znak = 1
			else:
		  	  	znak = 0
			print('| ',A[i],' | ',B[j],' | ',C[k],' | ',znak,' |')
			print('','-'*23)