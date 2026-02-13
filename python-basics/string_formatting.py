# Name : Rey Bar
# Date : 12/02/2026
# String formatting

# Get string length
sentence = "Attack On Titan is peak."

string_length = len(sentence)

print(f"The length is: {string_length}")

# Splitting a string
sentence_2 = "Eren Jaeger"
split = sentence_2.split(" ")

print(f"The first subject is: ", split[1])


# Make everything CAPS
mpesa_code = "GF8eds59AS"

capitalized = mpesa_code.upper()

print(f"M-Pesa code: ", capitalized)

# Make to lower
lowercase_code = mpesa_code.lower()

print("New M-Pesa code: ", lowercase_code)

# Replacing characters in a string

balance = "67420"
amount_added = "52000"

cleaned_balance = balance.replace("Kes","")

print("Cleaned balance: ", cleaned_balance)

cleaned_amount_added = amount_added.replace("Kes", "")

print("Cleaned amount added: ", cleaned_amount_added)

# New balance
updated_balance = int(cleaned_balance) + int(cleaned_amount_added)


print(f"Updated Balance: ", updated_balance)

from datetime import datetime 
today = datetime.today()

message = f"{mpesa_code}. Confirmed. {cleaned_amount_added} KES has been added to your account by {sentence_2} at {today} . New balance is {updated_balance} KES."

print(message)