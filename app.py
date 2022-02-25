'''
Created on 

Course work: 

@author: Elakia VM

Source:
    
'''

# Import necessary modules
import random 

#constants
BALLS_PER_OVER = 6


def get_random_number(min = 0,max =6):
    
    return random.randint(min,max)

def get_random_score():

    return get_random_number(0,6)

def play_single_over():

    current_over = BALLS_PER_OVER

    for ball in range(current_over):
        current_run = get_random_number()
        print(f'ball:{ball},run:{current_run}')

def startpy():
    
    # random_score = get_random_score()
    # print(random_score) 

    play_single_over()



if __name__ == '__main__':
    startpy()