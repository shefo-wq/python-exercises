tries = 5
mainpassword = "555"

inputpassword = input("enter your password: ")

while inputpassword != mainpassword:
    tries -= 1
    print(f"wrong password, {'last' if tries == 0 else tries}")

    if tries == 0:
        break

    inputpassword = input("enter your password: ")

else:
    print("you can not write left")