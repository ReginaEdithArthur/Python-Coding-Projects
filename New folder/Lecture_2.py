y = 'manner \n'
g = y * 5
print(g)

print(y,g)

# prompt = input("Enter any verb of your choice: ")
# print(f'I can {prompt} better than you.')
# space = prompt + ' '
# print(space * 4 + prompt)

guess = int(input("Guess the number: "))
number = 8

if guess == number:
    print("The guess is the same")

elif guess > number:
    print("The guess is larger")

else:
    print("The guess is smaller")


result = guess == number

print(result)
