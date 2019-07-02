import random


print('--------------------------')
print('----------GUESS THAT PRIMER GAME')
print('--------------------------')


goal = random.choice('ACGT')
goal += random.choice('ACGT')
goal += random.choice('ACGT')
goal += random.choice('ACGT')
goal += random.choice('ACGT')

print(goal)
guess = 'NNNN'

name = input('Player what is your name?')

while guess != goal:
    guess = input('Guess a 5 bp primer')
    misses = 0
    for i in range(len(guess)):
        if guess [i] != goal[i]:
            misses += 1

    if misses > 0:
        print('Sorry, you guess %i bases wrong. Play again?' %misses)
