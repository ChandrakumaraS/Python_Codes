num = int(input("Enter a number to find it is an armstrong or not: "))

temp = num
total = 0
while temp != 0:
    degit = temp % 10
    total = total + degit**3
    temp = temp // 10


if num == total:
    print("The given number is Armstrong")
else:
    print("No, its not Armstrong")