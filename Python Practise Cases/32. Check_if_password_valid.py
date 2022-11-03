import re


"""Rules:
1. Length between 6-20
2. At least one lowercase letter
3. At least one upper case letter
4. At least one number
5. At least one special character
"""

password = "Interpreting@123"

# use Re to check
# def check_password(password: str) -> bool:
#     result = re.fullmatch(
#         r'.+(?=.{6,20})(?=.*\d)(?=.*[A-Z])(?=.*[$%?!%](?=.*[a-z]))', password)
#     if result is None:
#         return False
#     else:
#         return True


# check_password(password)

# use `if` check and return the reason

def check_password(password: str) -> bool:
    if not 20 >= len(password) >= 6:
        return False, "The length must be between 6 and 20."
    if not re.findall(r'[a-z]', password):
        return False, "The password must have at least one lowercase letter."
    if not re.findall(r'[A-Z]', password):
        return False, "The password must have at least one uppercase letter."
    if not re.findall(r'[0-9]', password):
        return False, "The password must have at least one number."
    if not re.findall(r'[\W]', password):  # or [^0-9a-zA-Z] [not alphanumeric]
        return False, "The password must have at least one special character."

    else:
        return True, "The password is valid."


check_password(password)
