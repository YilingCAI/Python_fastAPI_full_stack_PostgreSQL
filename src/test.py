"""
ctrl + /
tab
shift + tab
ctrl + d (duplicate)
python -m venv yiling_projet
source yiling_projet/bin/activate
.\yiling_projet\Scripts\activate
deactivate
pip -V
pip install pandas
pip install fastapi
pip install "unicorn[standard]"
pip install "passlib[bcrpyt]"
pip install psycopg2-binary
pip list
pip freeze > requirements.txt
git init
git push --force-with-lease
git pull
git remote add projet xxxxxxx
git remote -v 

sudo -u postgres psql postgres
CREATE USER dbuser WITH PASSWORD 'dbuser';



# https://www.bytebase.com/blog/top-psql-commands-with-examples/
# https://www.postgresql.org/docs/current/app-psql.html
# https://docs.postgresql.fr/10/sql-grant.html 



# sudo apt install pgbadger

# sudo pgbadger -f stderr -v /var/lib/pgsql/16/data/pg_log/postgresql-*.log -o /home/yiling/project/fastAPI/TodoApp/report.html
modify postgresql.conf  -> restart the service

logging_collector = on
log_directory = '/var/lib/pgsql/13/data/pg_log'
log_filename = 'postgresql-%a.log'
log_rotation_age = 1d
log_rotation_size = 0

"""
import random

from grades import print_my_name

# first_name = 'eric'
# last_name = 'pioupiou'
#
# print("my name \n is {first_name}")
# print(f'my name is {first_name}')
# print(r'my name is {first_name}')
#
# sentence = "my name is {} {}"
# print(sentence.format(first_name, last_name))
#
# input_name = input("Enter your first name: ")
# print(input_name)
# print(f"hi {input_name}")
#
# days = int(input("entre the day:"))
# print(type(days))
# print(round(days/7))

# list
# my_list = [2, 98, 778, 67,56]
# print(my_list)
# print(my_list[0])
# my_list.append(1000)
# print(my_list)
# my_list.remove(98)
# print(my_list)
# my_list.insert(2, 997)
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)
# my_list.pop(1)
# print(my_list)

# people_list = ['piou', 'mumu', 'mimi']
# print(people_list[-1])
# print(people_list[0:2])
# print(len(people_list))

# set and tuples
# set are similar to list, but only contain unique and unordered value using curly brackets, have no index

# my_set = {1, 2, 4, 5, 9, 23}
# print(my_set)
# my_set.add(11)
# print(my_set)
# # remove check the value before remove, else error throw
# my_set.remove(999)
# print(my_set)
# my_set.discard(999)
# print(my_set)
# my_set.update([6,99])
# print(my_set)

# tuple : cannot change the value, cannot add value
# my_tuple = (2, 3, 5)
# print(my_tuple)
# print(my_tuple[1])
# print(len(my_tuple))
#
# for i in my_tuple:
#     print(i)

# like_meuh = False
# like_piou = True
#
# print(type(like_piou))
# print(1 == 2)
# print(1 != 2)
# print(1 >= 2)
#
# print(1 > 3 and 5 < 7)
# print(1 > 3 or 5 < 7)
# print(not(1 == 1))

# IF ELSE IF
# x = 3
# if x == 1:
#     print('x = 1')
# elif x == 2:
#     print('x = 2')
# else:
#     print('not in the value')

# LOOP
# my_list = range(0, 5)
# print(my_list)
#
# sum_list = 0
# for i in range(0, 5):
#     sum_list+= i
# print(sum_list)
#
# while 0 < i < 5:
#     i+=1
#
# print(i)
#
# while i < 5:
#    i += 1
#    if i == 3:
#        continue
#    if i == 4:
#        break

# dictionary
# my_dictionary = {
#     'username': "yiling",
#     'age': 32
# }
#
# print(my_dictionary.get('username'))
# my_dictionary['married'] = True
# print(my_dic)
# print(len(my_dic))
#
# my_dic.pop('age')
# print(my_dic)

# my_dic.clear()
# print(my_dic)

# del my_dic

# for value in my_dictionary:
#     print(my_dictionary[value])
#
# for key, value in my_dictionary.items():
#     print(key)
#     print(value)
#
# for tuple_value in my_dictionary.items():
#     print(tuple_value)
#
# my_dictionary2 = my_dictionary.copy()
#
# my_list_dic = [
#     {"username": 'piou', 'age': 30},
#     {"username": 'mumu', 'age': 2}
# ]
#
#
# for i in my_list_dic:
#     for x, y in i.items():
#         print(x, y)
#
# print(my_list_dic[0].get('age'))
#
# my_list_lsit = [
#     [1, 2, 3, 4],
#     ['piou', 'mumu']
# ]
#
# print(my_list_lsit[0][1])


# function
# def print_my_name(name):
#     print(f'hi {name}')
# print_my_name('yiling')
#
# def mul_num(a, b):
#     return a*b
# solution = mul_num(2, 2)
# print(solution)

# module

# print_my_name('yiling')
#
# import random
# type_of_drinks = ['piou', 'mumu']
# print(random.choice(type_of_drinks))
#
# print(random.randint(2, 7))

# OOP
# class Student:
#     number_of_students = 0
#     school = 'Online School'
#     def __init__(self, first_name, last_name, major):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.major = major
#
#         Student.number_of_students +=1
#
#     def fullname_with_major(self):
#         return f'{self.first_name} {self.last_name} is a ' \
#                f'{self.major} major!'
#
#     def full_name_school(self):
#         return f'{self.first_name} {self.last_name} is a ' \
#                f'going to {self.school}'
#
#     @classmethod
#     def set_online_school(cls, new_school):
#         cls.school = new_school
#
#     @classmethod
#     def split_student(cls, student_str):
#         firstname, lastname, major = student_str.split('.')
#         return cls(firstname, lastname, major)
#
# print(Student.number_of_students)
# student_1 = Student('Eric', 'Roby', 'CS')  # une instance de Class student
# student_2 = Student('John', 'Miller', 'Math')
# print(Student.number_of_students)
# print(student_1.first_name)
# print(student_2.first_name)
#
#
# print(student_1.full_name_school())
#
# print(student_1.fullname_with_major())  # more popular in this way
# print(Student.fullname_with_major(student_2))
#
# Student.set_online_school('Pioupiou school')
# print(student_1.school)
# print(student_2.school)
#
# new_student = 'yiling.cai.energy'
# student_3 = Student.split_student(new_student)
# print(student_3.fullname_with_major())
#
# class CollegeStudent(Student):
#     def __init__(self, first_name, last_name, major, job):
#         super().__init__(first_name, last_name, major)
#         self.job = job
#
# print (CollegeStudent('yiling', 'mou', 'CS', 'teacher').fullname_with_major())
# print (CollegeStudent('yiling', 'mou', 'CS', 'teacher').job)