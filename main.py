#delattr

# class Person:
#     pass
# id_1 = Person()                                     #создаем экземпляр класса
#
# setattr(id_1, "name", "")                           #поле и значение поля
# print(hasattr(id_1, "name"))                        #проверяем есть ли данное поле в классе


# class Person:
#     name = "Вася"
# id_1 = Person()
#
# if hasattr(id_1, "name"):
#     delattr(Person, "name")
# print(id_1.__dict__)




# names = ['Klemantina', 'Roza', 'Balu', 'Lena', 'Leonid']        #список имен
#
# class Person:
#     Vasya = ""
#     Masha = ""
#     Lena = ""
#     Leonid = ""
# for i in names:
#     if hasattr(Person, i):
#         delattr(Person, i)
#         print(i)
# print(len(Person.__dict__))

#----------------------------МЕТОДЫ------------------------------------------

# class Calculator:
#     def addition(self):
#         print('складываю числа')
# #создаем экземпляр класса
#
# calc = Calculator()
# #вызываю экземпляр и метод addition
# calc.addition()
#Calculator.addition()   -------- Ошибка, потому что self

# class Kitty:
#     def hello_kitty(self):
#         print('Hello Kitty!')
# cat = Kitty()
# cat.hello_kitty()

#если self то выводится только через экземпляр класса

# class Kitty:
#     def say_hello(self):
#         print('Hello, Kitty')
# cat = Kitty()
# cat.say_hello()


# def add_numbers(x,y):           #параметры
#     return x + y
# print(add_numbers(11,55))           #аргументы


# class Number:
#     a = 10
#     b = 5
#
# #создаем экземпляр класса
# first = Number()
# print(first.a + first.b)

# class Calculator:
#     a = 10
#     b = 5
#     def addition(self):
#         summ = self.a + self.b
#         print(summ)
# first = Calculator()
# first.addition()
#
# second = Calculator()
# second.b = 10
# second.addition()


#Область видимости класса и self

# a = 10
# b = 5
# def addition():
#     summa = a + b
#     print(summa)
# addition()

# class Calculator:
#     a = 10
#     b = 5
#     def addition(self):
#         summa = self.a + Calculator.b
#         print(summa)
#
# first = Calculator()
# first.addition()

# class Simpson:
#     a = "Bart"
#     b = "Homer"
#     c = "Lisa"
#     d = "Maggi"
#     def method(self):
#         a = f"Привет {self.a}"
#         print(a)
#
#     def method1(self):
#         b = f"Привет {self.b}"
#         print(b)
#
#     def method2(self):
#         c = f"Привет {self.c}"
#         print(c)
#
#     def method3(self):
#         d = f"Привет {self.d}"
#         print(d)
#
# name1 = Simpson()
# name1.method()
#
# name2 = Simpson()
# name2.method1()
#
# name3 = Simpson()
# name3.method2()
#
# name4 = Simpson()
# name4.method3()



# class Simpson:
#     name = "name"
#     def method(self):
#         a = f"Привет {self.name}"
#         print(a)
#
#
# name1 = Simpson()
# name1.name = "Bart"
# name1.method()
#
# name2 = Simpson()
# name2.name = "Homer"
# name2.method()
#
# name3 = Simpson()
# name3.name = "Lisa"
# name3.method()
#
# name4 = Simpson()
# name4.name = "Maggi"
# name4.method()

# class Person:
#     message_counter = 0
#
#     def print_number_of_messages(self):
#         print(self.message_counter)
#
# #создаем 2 экземпляра
# id_1 = Person()
# id_2 = Person()
#
# #к каждому экземпляру присваивается значение
# id_1.message_counter = 5
# id_2.message_counter = 10
# #прибавляем ко 2 значению
# id_2.message_counter += 10
# id_2.message_counter += 21
# id_2.message_counter += 33
# id_2.message_counter += 48
#
# #выводим на экран значение
# id_1.print_number_of_messages()
# id_2.print_number_of_messages()

#Позиционные параметры
# class Calculator:
#     def addition(self, a, b):
#         print(a + b)
# calc = Calculator()
# calc.addition(1,3)

#Параметры по умолчанию
# class Calculator:
#     def addition(self, a=0, b=0):
#         print(a + b)
# calc = Calculator()
# calc.addition(1,3)
# calc.addition(1)
# calc.addition()

# *args **kwargs
# class Calculator:
#     def addition(self, *args, **kwargs):
#         print(sum(args),kwargs)
#
# calc = Calculator()
# calc.addition(1,2,3,11,3,2,5,1,2,33,1,**{"qw":2})



# class Person:
#     def set_attr(self, name, age):
#         self.name = name
#         self.age = age
# person_1 = Person()
# person_1.set_attr("Вася", 14)
# print(person_1.name, person_1.age)


# class Person:
#     def set_attr(self, name, age):
#         setattr(self, "name", name)
#         setattr(self, "age", age)
# person_1 = Person()
# person_1.set_attr("Вася", 14)
# print(person_1.name , person_1.age)


class NewJournal:
    count_money = 0
    def set_attr(self, papa, mama, deda, baba):
        self.papa = papa
        self.mama = mama
        self.deda = deda
        self.baba = baba
        count_money = self.papa + self.mama + self.deda + self.baba
        print(count_money)
    def check_money(self):
        if count_money < 80:
            print("Денег не хватает")
        else:
            print("Ура, денег хватает!")
masha = NewJournal()
masha.set_attr(10,20,30,40)

































