import checking as c

class NewRegistration:
    def __init__(self):
        self._fname = ''
        self._lname = ''
        self._email = ''
        self._affil = ''
        self._year = ''
        self._country = ''
        self._city = ''
        self._postalCode = ''
        self._adress = ''
        self._hdyk = ''
    
    @property
    def fname(self):
        return self._fname
    @fname.setter
    def fname(self, new_fname):
        self._fname = c.fname_check(new_fname)

    @property
    def lname(self):
        return self._lname
    @lname.setter
    def lname(self, new_lname):
        self._lname = c.lname_check(new_lname)

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, new_email):
        self._email = c.email_check(new_email)

    @property
    def affil(self):
        return self._affil
    @affil.setter
    def affil(self, new_affil):
        self._affil = c.affil_check(new_affil)

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, new_year):
        self._year = c.year_check(new_year)

    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, new_country):
        self._country = c.country_check(new_country)

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, new_city):
        self._city = c.city_check(new_city)

    @property
    def postalCode(self):
        return self._postalCode
    @postalCode.setter
    def postalCode(self, new_postalCode):
        self._postalCode = c.postalCode_check(new_postalCode)

    @property
    def adress(self):
        return self._adress
    @adress.setter
    def adress(self, new_adress):
        self._adress = c.adress_check(new_adress)

    @property
    def hdyk(self):
        return self._hdyk
    @hdyk.setter
    def hdyk(self, new_hdyk):
        self._hdyk = c.hdyk_check(new_hdyk)

values = ['Ann','Li','say@google.com','Herzen University', '1999', 'Russia', 'St.Petersburg', '123923', 'st.Vishnevskogo,56', 'Internet']
new_form = NewRegistration()
try:
    new_form.fname = values[0]
    new_form.lname = values[1]
    new_form.email = values[2]
    new_form.affil = values[3]
    new_form.year = values[4]
    new_form.country = values[5]
    new_form.city = values[6]
    new_form.postalCode = values[7]
    new_form.adress = values[8]
    new_form.hdyk = values[9]
except ValueError as e:
    print(f'Неверная запись: {e}')
else:
    print('Ваша заявка принята')