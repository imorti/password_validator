password = "1234 56789"
# check to see if password is part of our common password list
def common_check(input): 
    with open("common_password_list.txt") as f:

        lines = f.read().splitlines() 
        for line in lines:
        # Check for at too common 
            if input == line:
                print("Password is too common")
                print(input) 

common_check(password)