# Name : Rey Bar
# Date : 17/02/2026
# Program to illustrate break in Python

number = 1
while number <10:
    print(number)
    number +=1
    if number == 4:
        break 
    print("Breaking from the loop...") 
    continue 

import secrets
import string

def generate_secure_password(length=12):
    """Generate a cryptographically secure random string."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))

# Example: Generate a secure 16-character password
print(generate_secure_password(16))


import random
import string

def generate_random_alphanumeric_loop(length):
  """Generates a random string of uppercase letters and digits using a loop."""
  characters = string.ascii_uppercase + string.digits
  result = ''
  for _ in range(length):
    result += random.choice(characters)
  return result

# Example usage:
random_id_loop = generate_random_alphanumeric_loop(8)
print(random_id_loop) # Output example: 'Y9V1OVO4'


