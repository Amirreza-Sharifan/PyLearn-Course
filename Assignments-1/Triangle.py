print("Welcome, this project can help you to draw a triangle")
print("So, first give me 3 sizes of different sides of your triangle")
a=float(input("Enter Your First Side: "))
b=float(input("Enter Your Second Side: "))
c=float(input("Enter Your Third Side: "))
if (a<b+c) and(b<a+c) and(c<b+a):
    print("Yes, you can draw it")
else:
    print("No, you cannot draw it, change your sizes")