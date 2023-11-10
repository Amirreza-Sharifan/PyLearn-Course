import qrcode
user_input = input("Please enter your Name and your Phone number like (Amirreza Sharifan - 09370140070): ")
x = qrcode.make(user_input)
x.save("Name & Phone Number-QR.png")