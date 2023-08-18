import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+,./\;:"

print("Random Password Generator\n")
num_of_passwords = int(input("How many passwords do you want to generate?"))
password_length = int(input("How many characters do you want in your password?"))
print("Here are the generated passwords")

for x in range(num_of_passwords):
    password = ""
    for i in range(password_length):
        password += random.choice(characters)
    print(password)
