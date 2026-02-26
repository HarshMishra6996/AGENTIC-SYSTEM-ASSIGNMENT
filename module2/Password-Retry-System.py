# Keep asking for password until correct one is entered
while True:
    password = input("Enter password: ")
    
    if password == "admin123":
        print("Access granted")
        break
    else:
        print("Incorrect password, try again.")