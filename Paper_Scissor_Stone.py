import random
import time
import string
import cv2
import numpy as np


class PaperScissorStone(object):
    def __init__(self):
        self.all_charts = string.punctuation + string.whitespace
        self.loadings = ['rock', 'scissor', 'paper']
        self.choice = random.randint(0, 3)
        self.run = 1
        self.loser = 0
        self.winner = 0
        self.pngs = ['./rock.png', './scissor.png', './paper.png']

    def show(self, you, computer, sign):
        img = ''
        if sign == 'win':
            if you == self.loadings[0] and computer == self.loadings[1]:
                img = np.hstack([cv2.imread(self.pngs[0]), cv2.imread(self.pngs[1])])
            elif you == self.loadings[1] and computer == self.loadings[2]:
                img = np.hstack([cv2.imread(self.pngs[1]), cv2.imread(self.pngs[2])])
            elif you == self.loadings[2] and computer == self.loadings[0]:
                img = np.hstack([cv2.imread(self.pngs[2]), cv2.imread(self.pngs[0])])
        elif sign == 'lose':
            if you == self.loadings[0] and computer == self.loadings[2]:
                img = np.hstack([cv2.imread(self.pngs[0]), cv2.imread(self.pngs[2])])
            elif you == self.loadings[1] and computer == self.loadings[0]:
                img = np.hstack([cv2.imread(self.pngs[1]), cv2.imread(self.pngs[0])])
            elif you == self.loadings[2] and computer == self.loadings[1]:
                img = np.hstack([cv2.imread(self.pngs[2]), cv2.imread(self.pngs[1])])
        cv2.imshow('You %s!' % sign, img)
        cv2.waitKey(0)

    def play(self, name):
        while self.run <= 3:
            try:
                choice = input('\nGuess(press q to quit) :\n 0)rock 1)scissor 2)paper: ')
                if choice.strip().lower() == 'q':
                    print('\033[31m See you next time, %s \033[0m' % name)
                    print('\033[31m Quit the game. \033[0m')
                    return
                if not choice:
                    continue

                computer = self.loadings[int(self.choice)]
                you = self.loadings[int(choice)]
                if int(choice)-self.choice == -1 or int(choice) - self.choice == 2:
                    print('%s:%s' % (name, you), '\ncomputer:', computer,
                          '\n\033[31mRun %d\033[31m' % self.run, '\033[31m %s win.\033[0m' % name)
                    self.winner += 1
                    self.show(you, computer, 'win')
                elif int(choice) == self.choice:
                    print('%s:%s' % (name, you), '\ncomputer:', computer,
                          '\n\033[31mRun %d\033[31m' % self.run, '\033[31m flat hand.\033[0m')
                else:
                    print('%s:%s' % (name, you), '\ncomputer:', computer,
                          '\n\033[31mRun %d\033[31m' % self.run, '\033[31m %s lose.\033[0m' % name)
                    self.loser += 1
                    self.show(you, computer, 'lose')
            finally:
                self.run += 1
        print('\033[31m Game Over.\033[0m 3 Runs, %s:%d win / %d lose.' % (name, self.winner, self.loser))

    def start(self):
        while True:
            username = input('What is your name: ')
            for i in username:
                if i in self.all_charts:
                    print('Please enter valid name.')
                    continue
            if username.isalpha() is True:
                print('Valid name :%s.' % username)
                time.sleep(1)
                break

        print("Are you ready? %s" % username)
        for i in range(3, -1, -1):
            print('+', "-"*4, "+")
            print("|", str(i).center(3), " |")
        print('+', "-"*4, "+")
        self.play(username)


if __name__ == "__main__":
    player = PaperScissorStone()
    player.start()