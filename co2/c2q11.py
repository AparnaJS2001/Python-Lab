#Area of square
c=int(input("Enetr the side of square"))
x = lambda a : a*a
print("Area of square is :",x(c))

#Area of rectangle
d=int(input("Enter the length"))
f=int(input("Enetr the breadth"))
y=lambda d,f : d*f
print("Area of rectangle is :",y(d,f))

#Area of triangle
b=int(input("Enter the base length"))
h=int(input("Enter the height"))
z=lambda b,h : 0.5*b*h
print("Area of triangle is :",z(b,h))
