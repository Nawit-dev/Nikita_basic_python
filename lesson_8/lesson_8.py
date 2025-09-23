
# numbers = [34,63,45,6,4,6234,]
# it_numbers = iter(numbers)
# print(type(it_numbers))
# print(next(it_numbers))




# str_1 = 'Даниил'
# # it_str_1 = iter(str_1)
# # print(type(it_str_1))
#
# for i in str_1:
#     print(i)

# n = 5
#
# # result = []
# # for i in range(1, n + 1):
# # #     result.append(i ** 2 )
# # # result_ = [num ** 2 for num in range(1, n + 1) ]
# # numbers = [34,63,45,6,4,6234,]
# # result_numbers = [num  for num in numbers if num > 35 or num == 0]
# # print(result_numbers)
#
#
# numbers = [-1,2,4,5,636,-5,-676]
#
# # result = []
# # for i in numbers:
# #     if i >= 0:
# #         result.append(f'{i} - положительное')
# #     else:
# #         result.append(f'{i} - отрицательное')
# # print(result)
#
# result = [f'{i} - положительное' if i >= 0 else f'{i} - отрицательное' for i in numbers]
# print(result)


# table_multply = [
#     f'{x} * {y} = {x * y}'
#     for x in range(1, 10)
#     for y in range(1, 10)
# ]
# print(table_multply)

table = []
for x in range(1,10):
    for y in range(1,10):
        table.append(f'{x} * {y} = {x * y}')
print(table)