import re

print('Python password checker')
print('=======================')
print()

# Check is password meets length requirements in accordance with NIST
def check_length(password):
    length = len(password)
    
    if length < 15:
        pass_test = False
    
    else:
        pass_test = True
    
    return pass_test

#Checks if the password contains and uppercase
def contains_uppercase(password):
    if not re.search("[A-Z]", password):
        pass_test = False
    
    else:
        pass_test = True

    return pass_test

#Checks if the password contains a lowercase
def contains_lowercase(password):
    if not re.search("[a-z]", password):
        pass_test = False

    else:
        pass_test = True

    return pass_test

#Checks if the password contains a number 
def contains_number(password):
    if not re.search("[0-9]", password):
        pass_test = False

    else:
        pass_test = True

    return pass_test

#Checks if the password contains a special character
def contains_special_char(password):
    if not re.search("[@#$^&*?!<>]", password):
        pass_test = False

    else:
        pass_test = True

    return pass_test

#Checks if the password contains common patterns
def check_common_passwords(password):
    to_check = password

    match to_check:
        case '123456789':
                pass_test = False
        case '12345678':
                pass_test = False
        case '111111':
              pass_test = False
        case 'password':
              pass_test = False
        case 'password1':
              pass_test = False
        case '1234567':
              pass_test = False
        case '1234567890':
              pass_test = False
        case 'qwerty123':
              pass_test = False
        case '1q2w3e4r':
              pass_test = False
        case _:
              pass_test = True
    
    return pass_test

user_password = input('Please enter a password. ===> ')

if len(user_password) < 8:
    print('Passwords should be eight characters minimum.')
    print()
else:
    password_score = 0
    
    if(check_length(user_password) == True):
        password_score += 4
    if(contains_uppercase(user_password) == True):
        password_score += 2
    if(contains_lowercase(user_password) == True):
        password_score += 2
    if(contains_number(user_password) == True):
        password_score += 2
    if(contains_special_char(user_password) == True):
        password_score += 2
    if(check_common_passwords(user_password) == False):
        password_score = 0

    #Uncomment below to test password score functionality
    if password_score == 10:
        message = f"Your password score is {password_score} out of 12."
        print(message)
    
    else:
        message = f"Your password score is {password_score} out of 12."
        print(message)

        print()
        print('Try to include at least 15 characters, an upper case and lower case, as well as a number and a special character.')
         
