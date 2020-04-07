with open("common_password_list.txt") as f:

    lines = f.read().splitlines() 


for line in lines:
    print(line)   
