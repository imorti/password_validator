# Overview
This solution validates passwords with the following criteria:
```
1. Have an 8 character minimum
2. AT LEAST 64 character maximum
3. Allow all ASCII characters and spaces (unicode optional)
4. Not be a common password
```

# Usage
This validation script takes 3 parameters: 
1. A text file with passwords in newline text format
2. An output file to write out weak passwords to. 
3. A common_password_list to check inputs against. 

`python password_validator.py input_passwords.txt weak_list.txt common_password_list.txt`

# The process
