# def calculate_rectangle_area(width, height):
#     print(width * height)
# calculate_rectangle_area(5, 8)



# 3
# def celsius_to_fahrenheit(temperature):
#     print((temperature *9 / 5) +32)
# celsius_to_fahrenheit(25)


# 4
def is_even(a):
    if a %2 == 0:
     return True
    else:
       return False
print(is_even(10))


# 5
def max_of_two(num1, num2):
   if (num1 > num2):
      return num1
   else:
      return num2
max = max_of_two(32, 78)
print("the maximum of 32 and 78 is:", max)


# 6
def is_vowel(a):
   vowel = ["a", "e", "i", "o", "u"]
   if a in vowel:
      return True
   else:
      return False
print("is 'a' a vowel letter", is_vowel("a"))

#7
def factorial(n):
   if (n <= 1):
      return 1
   else:
      return n * factorial(n-1)
print('factorial 5 is', factorial(5))

#10

def print_triangle(n):
   for x in range(0, n+1):
      print("*" * x)
print_triangle(5)


# 8
def plaindrom(plaindrom):
   if (plaindrom == plaindrom[::-1]):
      return True
   else:
      return False
print(plaindrom("radar"))
