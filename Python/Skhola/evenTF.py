
def is_even(n):
     if n % 2 == 0:
         return True
     else:
         return False

try:
    n = int(input("number: "))
except ValueError:
    print("enter a number!")
