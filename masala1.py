# #1_masala
# def count_factors(num):
#     count = 0
#     while num % 5 == 0:
#         count += 1
#         num //= 5
#     return count
#
# n = int(input("n: "))
# m = int(input("m: "))
# zeros = 0
#
# for i in range(n, m + 1):
#     zeros += count_factors(i)
#
# print(zeros)