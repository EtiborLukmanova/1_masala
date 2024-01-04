#2_masala

# from faker import Faker
# import random
# fake = Faker()
#
# def generate_name():
#     name = fake.name().split()
#     first_name = name[0]
#     last_name = name[1]
#
#     while len(first_name) <= 7 or first_name[-1].lower() in ['a', 'e', 'i', 'o', 'u']:
#         name = fake.name().split()
#         first_name = name[0]
#     return f"{last_name} {first_name}"
# def generate_age():
#     while True:
#         age = random.randint(18, 60)
#         if age % 2 == 1:
#             return age
# def write_data(filename, num):
#     with open(filename, 'w') as file:
#         for i in range(1, num + 1):
#             full_name = generate_name()
#             age = generate_age()
#             file.write(f"{i}. {full_name}  {age}\n")
#
# write_data('test1.txt', 10)
#
# with open('test1.txt', 'r') as s_file:
#     with open('test2.txt', 'w') as _file:
#         for line in s_file:
#             _, _, full_name, age = line.split()
#             age = int(age)
#             if age % 2 == 1:
#                 _file.write(f"{full_name}  {age}\n")
