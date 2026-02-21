import functools
from functools import reduce



# 3. lambda function

add = lambda x, y: x + y

# print(add(1, 2))


# 4. map function

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))

# print(squared)


# 5. filter function

numbers = [1, 2, 3, 4, 5]

even = list(filter(lambda x: x % 2 == 0, numbers))

# print(even)



# 6. reduce function

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print(product)    