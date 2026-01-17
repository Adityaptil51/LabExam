a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("The Number", a, "is gretest")
elif b > c and b > a:
    print("The Number", b, "is gretest")
else:
    print("The Number", c, "is gretest")


if a < b and a < c:
    print("The Number", a, "is smallest")
elif b < c and b < a:
    print("The Number", b, "is smallest")
else:
    print("The Number", c, "is smallest")