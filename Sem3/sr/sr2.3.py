print(' F = A or (B and C) <-> (A or B) and (A or C)')
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
			if C[k]==1 and B[j]==1:
				a = 1
			else:
				a = 0
			if A[i]==1 or a==1:
				a = 1
			else:
				a = 0
			if A[i]==1 or B[j]==1:
				b = 1
			else:
				b = 0
			if A[i]==1 or C[k]==1:
				c = 1
			else:
				c = 0
			if b==1 and c==1:
				b = 1
			else:
				b = 0
			if a==b:
				znak = 1
			else:
				znak = 0
			print('| ',A[i],' | ',B[j],' | ',C[k],' | ',znak,' |')
			print('','-'*23)