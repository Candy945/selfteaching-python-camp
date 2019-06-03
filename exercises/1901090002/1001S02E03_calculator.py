
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if choice == '1':
    print(a, "+", b, "=", a+b)
elif choice == '2':
    print(a, "-", b, "=", a-b)
elif choice == '3':
    print(a, "*", b, "=", a*b)
elif choice == '4':
    print(a, "/", b, "=", a/b)
else:
    print("Invalid input")