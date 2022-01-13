a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
def dscr(a,b,c):
	"""
		Вычисление дискриминанта

		Расширенное описание: входные и выходные значения, особенности, работа и т.д.
	"""
	#print(dscr.__doc__) - можно увидеть документацию
	d = b**2-4*a*c
	return d
print(dscr(a,b,c))

#упаковка
def sup_dscr(*args):
	print(args)
	#много аргументов в функции

#распаковка
sup_dscr(*(1,2,3))