#Cesar Cano
#Midterm


#Guessing Game
cano_num = 5

guess = int(input("Guess my number: "))

while guess != cano_num and guess >= cano_num - 2 and guess <= cano_num + 2:
    guess = int(input("Close, try again: "))

if guess == cano_num:
    print("You guessed my number, Aweseome job!")

elif guess > cano_num:
    print("Your guess was higher than my number which is", cano_num, "I am sorry you lost")

else:
    print("Your guess was lower than my number which is", cano_num, "I am sorry you lost")
