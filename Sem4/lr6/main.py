import re

countryList = ['Russia','Finland','Britain','France','Germany','Spain','Italy']

class NewRegistration:
    def __init__(self, fname, lname, email, affil, year, country, city, postalCode, adress, hdyk):
        try:
            arg1 = self.__fname_check(fname)
            arg2 = self.__lname_check(lname)
            arg3 = self.__email_check(email)
            arg4 = self.__affil_check(affil)
            arg5 = self.__year_check(year)
            arg6 = self.__country_check(country)
            arg7 = self.__city_check(city)
            arg8 = self.__postalCode_check(postalCode)
            arg9 = self.__adress_check(adress)
            arg10 = self.__hdyk_check(hdyk)
        except ValueError as e:
            print(f'Неверная запись: {e}')
        else:
            self.fname = arg1
            self.lname = arg2
            self.email = arg3
            self.affil = arg4
            self.year = arg5
            self.country = arg6
            self.city = arg7
            self.postalCode = arg8
            self.adress = arg9
            self.hdyk = arg10
            print('Ваша заявка принята')

    def __fname_check(self, value):
        if value == '':
            raise ValueError('Заполните параметр First Name')
        if len(value) < 2:
            raise ValueError('Параметр First Name должен содержать не менее 2 символов')
        if re.search(r'[0-9]', value) != None:
            raise ValueError('Параметр First Name не должен содержать цифр')
        return value
    
    def __lname_check(self, value):
        if value == '':
            raise ValueError('Заполните параметр Last Name')
        if re.search(r'[0-9]', value) != None:
            raise ValueError('Параметр Last Name не должен содержать цифр')
        return value
    
    def __email_check(self, value):
        if value == '':
            raise ValueError('Заполните параметр Email')
        if re.fullmatch(r'.+?@.+?\..{1,4}',value) == None:
            raise ValueError('Неверно введен параметр Email')
        return value
            
    def __affil_check(self, value):
        if value == '':
            raise ValueError('Заполните параметр Affiliation')
        if re.search(r'[0-9]', value) != None:
            raise ValueError('Параметр Affiliation не должен содержать цифр')
        if value.find('University') == -1:
            raise ValueError('Параметр Affiliation должен содержать слово "University"')
        return value
    
    def __year_check(self, value):
        if value == '':
            raise ValueError('Заполните параметр Year of birth')
        if int(value) < 1900 or int(value) > 2015:
            raise ValueError('Невозможное значение параметра Year of birth')
        return value
    
    def __country_check(self, value):
        if value == '':
            raise ValueError('Заполните параметр Country')
        if value not in countryList:
            raise ValueError('Неверное заполнение параментра Country. Данная страна не принимает участие в конференции')
        return value
    
    def __city_check(self, value):
        if value == '':
            raise ValueError('Заполните параметр City')
        if re.search(r'[0-9]', value) != None:
            raise ValueError('Параметр City не должен содержать цифр')
        if len(value) < 4:
            raise ValueError('Параметр City должен содержать не менее 4 символов')
        return value
    
    def __postalCode_check(self, value):
        if value == '':
            raise ValueError('Заполните параметр Postal Code')
        if len(value) < 6:
            raise ValueError('Параметр Postal Code должен содержать не менее 6 цифр')
        if re.search(r'\D',value) != None:
            raise ValueError('Параметр Postal Code должен состоять только из цифр')
        return value
    
    def __adress_check(self, value):
        if value == '':
            raise ValueError('Заполните параметр Adress')
        if re.fullmatch(r'st\.[\s]?[\w]+?,[\s]?[\d]+?[\w]*?', value) == None:
            raise ValueError('Неверно введен параметр Adress. Введите его по шаблону "st. NameOfStreet, NumberOfHouse"')
        return value
    
    def __hdyk_check(self, value):
        if value == '':
            raise ValueError('Заполните параметр "How Did You Know About Us?"')
        if len(value) < 3:
            raise ValueError('Параметр "How Did You Know About Us?" заполнен не корректно')
        return value

new_form = NewRegistration('Ann','Li','say@google.com','Herzen University', '1999', 'Russia', 'St.Petersburg', '123923', 'st.Vishnevskogo,56', 'Internet')
