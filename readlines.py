fo = open("common_password_list.txt", "r+")
lines = []
stripped_lines = []

lines = fo.readlines()

stripped_lines = s.strip('\n') for s in lines

for line in lines:
    print(lines)   
