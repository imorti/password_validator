import sys
import os

valid_flag = True

# get the input file
input_file = sys.argv[1]

if os.path.isdir(input_file):
    print('The path specified does exist')
    sys.exit()


# get the output file name
output_file = sys.argv[2]

common_password_list = sys.argv[3]

# load the input file into read lines
with open(input_file) as f:

    lines = f.read().splitlines() 

    for line in lines: 

        # check for length of input
        if len(line)<8 or len(line)>64:
            with open(output_file, 'a') as f1:
                f1.write(line + os.linesep)
                print("Error: Password has to be between 8 and 64 characters")
                print(line)
                valid_flag = False

        with open(common_password_list) as pwd_list:

            commons = pwd_list.read().splitlines() 
            for common in commons:
            # Check for input in common password list
                if line == common:
                    print("Error: Password is too common")
                    with open(output_file, 'a') as f2:
                        f2.write(line +os.linesep)
                        print(line)
                        valid_flag = False
    # Make sure we're ascii safe
    if not line.isascii():
        print("Error: Password has to be ascii")
        print(line)
        valid_flag = False

    #password is valid   
    if valid_flag:                
        print(line)
        print("Password is valid")



