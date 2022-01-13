def main():
	"""
		Функция 'меню'
	"""
	input_str = input("Введите строку для поиска: ")

	searchable_str = input("Введите строку, по которой мы ищем: ")

	choice = None
	while choice != '4':

		print('1 - поиск первого вхождения подстроки')
		print('2 - замена первой подстроки')

		print('3 - найти все вхождения подстроки' )

		print('4 - для выхода')
		choice = input("Сделайте выбор (1..4) ")

		if choice == '1':
			f = search_str(input_str,searchable_str)
			if f != -1:
				print("Начало: ",f,". Нашел", sep = "")
			else:
				print("Не нашел")

		if choice == '2':
			rep_str = input("Строка для замены: ")
			search_n_replace_str(input_str, rep_str, searchable_str)

		if choice == '3':
			search_all_str(input_str,searchable_str)
			
def search_str(what="", where=""):
	"""
		Функция поиска первого вхождения подстроки

		Функция ищет первое вхождение подстроки в строке и возвращает индекс начала вхождения.
		Если вхождение было не найдено, возвращает -1.

		Первый аргумент (what) - подстрока, которую мы должны найти.
		Второй аргумент (where) - строка, где мы ищем подстроку.
	"""
	i = 0
	j = 0
	flag = False
	while i < len(where) and flag == False:
		if where[i] == what[j]:
			i += 1
			j += 1
		else:
			i += 1
			if i < len(where) and where[i] == what[j]:
				i += 1
				j += 1
			else:
				j = 0
		if j == len(what):
			flag = True
	if flag == True:
		return i - len(what)
	else:
		return -1

def search_n_replace_str(what="", to_what="", where=""):
	"""
		Функция замены одной подстроки на другую

		Функция ищет первое вхождение подстроки в строке, заменяет его на заданную строку и выводит результат.
		Если данной подстроки в строке не было, выводит соответствующую надпись.

		Первый аргумент (what) - подстрока, которую мы должны заменить.
		Второй аргумент (to_what) - строка, которой мы должны заменить данную подстроку.
		Третий аргумент (where) - строка, где мы заменяем подстроку.
	"""
	f = search_str(what, where)
	if f != -1:
		str1 = where[:f]
		i = f + len(what)
		str2 = where[i:]
		str0 = str1 + to_what + str2
		print("Результат:",str0)
	else:
		print("Строки '",what,"' нет", sep = "")
	
def search_all_str(what="", where=""):
	"""
		Функция поиска всех вхождений подстроки

		Функция ищет все вхождения подстроки в строке и 
		возвращает строку со значениями индексов начала каждого вхождения.

		Первый аргумент (what) - подстрока, которую мы должны найти.
		Второй аргумент (where) - строка, где мы ищем подстроку.
	"""
	f = 0
	i = 0
	k = 0
	l = "Нашел '" + what + "' на местах: "
	while i != -1 and i < len(where):
		k = len(where[:i])
		f = search_str(what,where[i:])
		if f == -1:
			break
		f += k
		l += str(f) + " "
		i = f
		i += len(what)
	if i == -1:
		print("Строки '",what,"' нет", sep = "")
	else:
		print(l)

main()
