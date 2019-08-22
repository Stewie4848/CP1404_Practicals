password_length = 5
valid_password = False
while valid_password is False:
    password = input("Password: ")
    if len(password) >= password_length:
        valid_password = True
    else:
        print("Invalid password")
print('*' * len(password))
