def khawarizmi():
    print("Enter the coefficients of the quadratic equation ax^2 + bx + c = 0: ")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        print("The roots are:", root1, "and", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("The root is:", root)
    else:
        real_part = -b / (2*a)
        imag_part = (-discriminant)**0.5 / (2*a)
        print("The roots are complex numbers:", real_part + imag_part, "and", real_part - imag_part)
        
        khawarizmi()

# possible to write it also in one line using a lambda function

khawarizmi = lambda a, b, c: (-b+cmath.sqrt(b**2-4*a*c))/(2*a), (-b-cmath.sqrt(b**2-4*a*c))/(2*a)

#here's another way to do it also 
def khawarizmi():
    print("Enter the coefficients of the quadratic equation ax^2 + bx + c = 0: ")
    a, b, c = [float(input()) for _ in range(3)]
    d = b**2 - 4*a*c
    roots = [(-b + cmath.sqrt(d)) / (2*a), (-b - cmath.sqrt(d)) / (2*a)]
    print("The roots of the quadratic equation are:", *roots)
In this version, the a, b, and c variables are assigned using a list comprehension that prompts the user to enter the coefficients. The roots variable is a list that contains both roots, calculated using the quadratic formula. Finally, the roots are printed using the * operator to unpack the list into separate arguments for the print() function.

This version is concise and easy to read, while still maintaining readability and understandability.










