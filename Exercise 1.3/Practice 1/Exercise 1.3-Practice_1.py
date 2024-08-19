a = int(input("Enter a number: "))
b = int(input("Enter another one: "))
operator = input("Choose your operator: (+ or -): ")

if operator == '+':
    result = a + b
    print("When you add them up you get: " + str(result))
elif operator == '-':
    result = a - b
    print("When you subtract them you get: " + str(result))
else:
    print("You didn't choose + or -")
    