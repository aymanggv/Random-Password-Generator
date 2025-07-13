# Collect user preferences
# -length --done
# -should contain uppercase
# -should contain special characters
# -should contain digits

# get all available characters
# randomly pick characters up to length
# ensure we have at least 1 of each character type (uppercase, special, digit)
# ensure length is valid --done

import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation
#all_characters = list(upper) + list(digits) + list(punctuation) + list(lower)
#print(all_characters)

def generate_password():
    
    password_length =  int(input("What length would you like your password to be?: "))
    if password_length < 4:
        print("Password length must be at least 4 characters.")
        return
    uppercase_req = input("Should there be an uppercase letter? (y/n): ").strip().lower()
    digits_req= input("Should there be digits? (y/n): ").strip().lower()
    puntuationc_req = input("Should there be a punctuation? (y/n): ").strip().lower()
        
    new_password= []
    all_characters = []
    
    if uppercase_req == "y":
        new_password.append(random.choice(upper)) # Ensure at least one upper
        all_characters += list(upper)
        password_length -= 1
        

    if digits_req == "y":
        new_password.append(random.choice(digits)) # Ensure at least one digit
        all_characters += list(digits)
        password_length -= 1
        
        
    if puntuationc_req == "y":
        new_password.append(random.choice(punctuation)) # Ensure at least one punctuation
        all_characters += list(punctuation)
        password_length -= 1
        
        
    # Always include lowercase by default
    all_characters += list(lower)
    new_password.append(random.choice(lower))  # Ensure at least one lowercase
    password_length -= 1
    # print(all_characters)
    # print(new_password)

    for _ in range(password_length):
        new_password.append(random.choice(all_characters))

    
    random.shuffle(new_password)    
    return print("Your randomly generated password is:", "".join(new_password))
    
generate_password()
        



