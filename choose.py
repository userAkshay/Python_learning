# I use this scriüt from https://github.com/MattHeard/Python-Toys/blob/master/hard/1/guess.py, purpose behind this to learn python 
# Thanks MattHeard for toy programming 

from random import Random
from string import Template


def read_mind():
        lo = 1
        hi = 100
        found_it = False
        generator = Random()
        while found_it == False:
                magic = generator.randint(lo, hi)
                template = Template('Is it ${g}?')
                question = template.substitute(g=magic)
                answer = ''
                right_anw = ('y', 'q', 'h', 'l')
                while answer not in right_anw:
                        print(question)
                        print('(H) Higher')
                        print('(L) Lower')
                        print('(Y) You got it!')
                        print('(Q) Quit')
                        answer = input('> ').lower()
                        if answer not in right_anw:
                                print('Uh. Try again.')
                if answer == 'y':
                        found_it = True
                        print('Yay! I got it!')
                        answer = input('Play again? (Y/n) ').lower()
                        if answer == 'y':
                                found_it = False
                                lo = 1
                                hi = 100
                        else:
                                print("Okay. :( I guess you dont want to play with me!")
                elif answer == 'q':
                        print("I will be better in this game one day :) Now Good Bye..!")
                        return
                elif answer == 'h':
                        lo = magic + 1
                elif answer == 'l':
                        hi = magic - 1
                else:
                        print("OOh some error occured..!!!!")



def start():
        print('HIGH OR LOW')
        print('Choose any number between 1-100 and I will try to read your mind')
        user_is_ready = input('Are you Ready:))))))? (Y/n) ').lower()
        if user_is_ready == 'y' or user_is_ready == '':
                read_mind()
        else:
                print("Okay as your wish let's play later then")

if __name__ == '__main__':
        start()
