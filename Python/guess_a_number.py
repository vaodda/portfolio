secret_number = 409

guess = int(input("try to guess a number: "))
if guess == secret_number:
    print("ok, you won this time lucky bastard")
elif guess > secret_number:
    print("you were close, try lower")
else:
    print("you were close, try higher")