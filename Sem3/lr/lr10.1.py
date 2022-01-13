def main():
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
			search_str(input_str,searchable_str)

		if choice == '2':
			rep_str = print('Строка для замены: ')

		# найти функцию, позволяющую осуществлять замену подстроки строкой

		if choice == '3':
			# TODO
			pass

def search_str(what="", where=""):
	# 1 - поиск первого вхождения подстроки
	i = 0
	j = 0
	flag = False
	while i < len(where) and flag == False:
		if where[i] == what[j]:
			i += 1
			j += 1
		else:
			i += 1
			if where[i] == what[j]:
				i += 1
				j += 1
			else:
				j = 0
		if j == len(what):
			flag = True
	if flag == True:
		print("Начало: ",i - len(what),". Нашел")
	else:
		print("Не нашел")

def search_n_replace_str(what="", to_what="", where=""):
	# what - что меняем
	# to_what - на что меняем
	# where - где меняем
	# 3 - найти все вхождения подстроки
	pass

main()
