# Rock, Paper and Scissors game!
import random, sys
print('Welcome to Rock, Paper, Scissors game!')
print('Press Y to play!')
R = input()
win = 0
draw = 0
lose = 0
while R == 'Y':
    print('Choose r for rock, p for paper, s for scissor and q for quit!')
    move = input()
    if move == 'p':
        print('Paper versus...')
        break
    elif move == 's':
        print('Scissor versus...')
        break
    elif move == 'r':
        print('Rock versus...')
        break
    elif move == 'q':
        print('Quiting...')
        sys.exit()
    else:
        print('Invalid move, try again')
        continue
randomNumber = random.randint(1, 3)
if randomNumber == 1:
    computermove = 'r'
    print('Rock!')
elif randomNumber == 2:
    computermove = 'p'
    print('Paper!')
elif randomNumber == 3:
    computermove = 's'
    print('Scissor!')
if computermove == move:
    print('It is a tie!')
    draw += 1
elif computermove == 'p' and move == 's':
    print('You win!')
    win += 1
elif computermove == 'p' and move == 'r':
    print('You lose!')
    lose += 1
elif computermove == 's' and move == 'p':
    print('You lose!')
    lose += 1
elif computermove == 's' and move == 'r':
    print('You win!')
    win += 1
elif computermove == 'r' and move == 's':
    print('You lose!')
    lose += 1
elif computermove == 'r' and move == 'p':
    print('You win!')
    win += 1
print('Now you have {} wins, {} loses and {} draws, wanna try again?'.format(win,lose,draw))

