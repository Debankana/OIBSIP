import string
import random

full_set=string.ascii_letters+string.digits+string.punctuation

length=int(input("Enter the length of the password: "))
password=''.join(random.choices(full_set, k=length))

print("Your password is: ", password)
