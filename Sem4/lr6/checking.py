from re import search, fullmatch

countryList = ['Russia','Finland','Britain','France','Germany','Spain','Italy']

def fname_check(value):
    if value == '':
        raise ValueError('Заполните параметр First Name')
    if len(value) < 2:
        raise ValueError('Параметр First Name должен содержать не менее 2 символов')
    if search(r'[0-9]', value) != None:
        raise ValueError('Параметр First Name не должен содержать цифр')
    return value
    
def lname_check(value):
    if value == '':
        raise ValueError('Заполните параметр Last Name')
    if search(r'[0-9]', value) != None:
        raise ValueError('Параметр Last Name не должен содержать цифр')
    return value
    
def email_check(value):
    if value == '':
        raise ValueError('Заполните параметр Email')
    if fullmatch(r'.+?@.+?\..{1,4}',value) == None:
        raise ValueError('Неверно введен параметр Email')
    return value
            
def affil_check(value):
    if value == '':
        raise ValueError('Заполните параметр Affiliation')
    if search(r'[0-9]', value) != None:
        raise ValueError('Параметр Affiliation не должен содержать цифр')
    if value.find('University') == -1:
        raise ValueError('Параметр Affiliation должен содержать слово "University"')
    return value
    
def year_check(value):
    if value == '':
        raise ValueError('Заполните параметр Year of birth')
    if int(value) < 1900 or int(value) > 2015:
        raise ValueError('Невозможное значение параметра Year of birth')
    return value
    
def country_check(value):
    if value == '':
        raise ValueError('Заполните параметр Country')
    if value not in countryList:
        raise ValueError('Неверное заполнение параментра Country. Данная страна не принимает участие в конференции')
    return value
    
def city_check(value):
    if value == '':
        raise ValueError('Заполните параметр City')
    if search(r'[0-9]', value) != None:
        raise ValueError('Параметр City не должен содержать цифр')
    if len(value) < 4:
        raise ValueError('Параметр City должен содержать не менее 4 символов')
    return value
    
def postalCode_check(value):
    if value == '':
        raise ValueError('Заполните параметр Postal Code')
    if len(value) < 6:
        raise ValueError('Параметр Postal Code должен содержать не менее 6 цифр')
    if search(r'\D',value) != None:
        raise ValueError('Параметр Postal Code должен состоять только из цифр')
    return value
    
def adress_check(value):
    if value == '':
        raise ValueError('Заполните параметр Adress')
    if fullmatch(r'st\.[\s]?[\w]+?,[\s]?[\d]+?[\w]*?', value) == None:
        raise ValueError('Неверно введен параметр Adress. Введите его по шаблону "st. NameOfStreet, NumberOfHouse"')
    return value
    
def hdyk_check(value):
    if value == '':
        raise ValueError('Заполните параметр "How Did You Know About Us?"')
    if len(value) < 3:
        raise ValueError('Параметр "How Did You Know About Us?" заполнен не корректно')
    return value

if __name__ == "__main__":
    pass