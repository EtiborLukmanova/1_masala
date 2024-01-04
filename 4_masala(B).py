# 4_masala

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def prime_numbers_decorator(func):
#     def wrapper(lst):
#         result = func(lst)
#         primes = [x for x in result if isinstance(x, int) and is_prime(x)]
#         sorted_primes = sorted(primes)
#         return sorted_primes
#     return wrapper
#
# @prime_numbers_decorator
# def _list(lst):
#     return lst
#
# input_list = [1, 2, 7, 'hello', 3, 'world', 11, 8, 'python', 13]
# result = _list(input_list)
# print(result)










