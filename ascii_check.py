#check that password is ascii
def ascii_check(password):
    if not password.isascii():
        print("Error: Password has to be ascii")
    elif password.isascii():
        print("password is valid for ascii")

ascii_check("Æ æ")
