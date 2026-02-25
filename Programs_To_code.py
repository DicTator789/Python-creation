from turtle import update
from collections import defaultdict
import math
import time
import os

#  1. *args for average
def average(*args):
    return math.fsum(args)/len(args)

# print(average(1,2,3,4,5))


# 2. **kwargs for keyword arguments

employees = defaultdict(dict)   # defaultdict is used to create a dictionary with default values

def print_kwargs(emp_id,**kwargs):
    employees[emp_id].update(kwargs)

print_kwargs("Employee1",name="John", age=30, city="New York")

# for employee, details in employees.items():
#     print(employee)
#     for key, value in details.items():
#         print(key, value)


# 3. ATM machine with custom exception
class InsufficientBalanceError(Exception):
    pass
def ATM(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    elif amount == 0 or amount < 0:
        raise ValueError("Amount cannot be zero or negative")
    return balance - amount

print(ATM(1000, 1080))


# 4. Read a file and count number of lines
count = 0
with open("app.log", "r") as file:
    for line in file:
        if len(line.strip())==0:   # if not line.strip() is also same
            continue
        count += 1
# print(count)


with open("app.log", 'r') as fp:
    lines = sum(1 for line in fp if line.strip())
    # print('Total Non-Empty Lines:', lines)


# 5. Write student marks to a file
with open("student_marks.txt", "w+") as file:
    file.write("Name: John, Marks: 90\n")
    file.write("Name: Jane, Marks: 80\n")
    file.write("Name: Bob, Marks: 70\n")
    file.seek(0)   # Move cursor to start
    # print(file.read())


time.sleep(3)
os.system('cls' if os.name=='nt' else 'clear')