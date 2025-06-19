word = str(input("input a word "))
letter = str(input("chouse a letter to be found: "))
count = 0

for i in word:
    if i == letter:
        count += 1

print(f"there is {count} of the letter {letter} in your word")