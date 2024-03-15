Side1=input("Enter Side1 Length ")
Side2=input("Enter Side2 Length ")
Side3=input("Enter Side3 Length ")
if Side1==Side2==Side3:
    print("it is a Equilateral Triangle")
else:
    print("it is NOT a Equilateral Triangle")
if Side1==Side2 or Side2==Side3 or Side1==Side3:
    print("it is a Isosceles Triangle")
else:
    print("it is NOT a Isosceles Triangle")
if Side1!=Side2!=Side3:
    print("it is a Scalene Triangle")
else:
    print("if is NOT a Scalene Triangle")