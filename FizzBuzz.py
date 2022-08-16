# FizzBuzz Game  in Python
i = 0
while i < 10:
    n = int(input("Please enter a number: "))
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    i += 1
    print(f"Remaining chances are: {10-i}")
print("Game End, See You Again")
