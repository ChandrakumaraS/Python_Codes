num = int(input("Please enter a series of number to reverse: "))
print("Before reversing number: ", num)


reverse = 0
while num != 0:
    reverse = reverse*10 + num % 10
    num = (num//10)


print(f"After reverse: {reverse}")
