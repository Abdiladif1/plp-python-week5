Question 1
import random
import string

def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
       password += random.choice(characters)
    return password

print(make_password())
print(make_password(12))import math


Question 2
def tables_needed(people, seats):
    return math.ceil(people / seats)

def welcome(name):
  return f"Welcome to PLP, {name}!"

if __name__ == "__main__":
    print(tables_needed(10, 4))

question 3
import helpers

print(helpers.welcome("Amina"))
print(helpers.tables_needed(47, 6))
print(helpers.tables_needed(20, 5))
