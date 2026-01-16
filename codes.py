import random

digit_code=input("Enter number of your digit-code:")
if digit_code == "3":
    digit_code=[random.randint(1,9)for _ in range(3)]
    print("Your code is:",digit_code)
elif digit_code == "4":
    digit_code=[random.randint(1,9)for _ in range(4)]
    print("Your code is:",digit_code)
else: print("Your code can be only 3 or 4 numbers long!")
