'''
Created on 

Course work: 

@author: Elakia VM

Source:
    
'''

# Import necessary modules
import random 
import time


#constants

QUICK_TESTING = False

BALLS_PER_OVER  =   6
TOTAL_WICKETS   =   10
TOTAL_OVERS     =   2
CURRENT_TEAMS   = [
    'India',
    'Pakistan'
]

team_a_players = [
    "Virat Kohli",
    "Rohit Sharma",
    "Jasprit Bumrah",
    "Ravichandran Aswin",
    "Ravindra Jadeja",
    "Mohammed Shami",
    "Hardik Pandya",
    "Bhuvneshwar Kumar",
    "Kuldeep Yadav",
    "Rishabh Pant",
    "Shreyas Iyer"
]

team_b_players = [
    "Asif Ali",
    "Shoaib Malik",
    "Fakhar Zaman",
    "Mohammad Rizwan",
    "Mohammad Hafeez",
    "Imad Wasim",
    "Shaheen Afridi",
    "Hasan Ali",
    "Haider Ali",
    "Sarfaraz Ahmed",
    "Mohammad Wasim Jr"
]


team_a_total_score = 0
team_b_total_score = 0

def get_random_number(min = 0,max =6):
    
    return random.randint(min,max)


def is_wicket():
    
    r_number = get_random_number()
    
    if(r_number % 7 == 0):
        return True
    if(r_number % 9 == 0):
        return True
    return False
    

def automate_ball():
    if(QUICK_TESTING):
        return
    time.sleep(1)
    
def gap(count = 1):
    for space in range(count):
        print('')

def get_random_score():

    return get_random_number(0,6)

def play_single_over(
    chase_flag              = False,
    chasing_score           = 0,
    team_current_score      = 0,
    current_wicket_index    = 0
    ):

    current_over = BALLS_PER_OVER
    
    total_score_current_over = 0 
    
    current_team_players = team_a_players
    
    if(chase_flag):
        current_team_players = team_b_players
    
    for ball in range(current_over):
        
        automate_ball()
        ball += 1 
        
        wicket_flag = is_wicket()
        
        current_batsman = current_team_players[current_wicket_index]
        
        if(wicket_flag):
            current_run = 0
            print(f'BALL: {ball}: OUT !!!! ITS A WICKET !!! {current_batsman} is out ')
            
            current_wicket_index += 1
            
        else:
            current_run = get_random_number()
        
            total_score_current_over += current_run
        
            print(f'ball: {ball}, {current_batsman} scored: {current_run}, total runs: {total_score_current_over}')

        if(chase_flag):
            if(team_current_score > chasing_score):
                # print(f'Beat the score: chasing_score: {chasing_score}, team_innings_score: {team_innings_score}')
                return team_current_score, current_wicket_index

    return total_score_current_over, current_wicket_index

def print_score_board(playing_over, team_innings_score):
    
    print(f'Scoreboard: Over {playing_over}; Runs: {team_innings_score}')
    
def play_innings(
    chase_flag              =   False, 
    over_count              =   1, 
    chasing_score           =   0,
    team_current_score      =   0
):
    team_innings_score = 0 
    
    for _current_over in range(over_count):
        
        playing_over = _current_over + 1
        
        print(f'Current over : {playing_over}')
        print('-' * 25)
        
        if(_current_over == 0):
            wicket_index = 0
        
        team_innings_score, wicket_index = play_single_over(
            chase_flag              =   chase_flag,
            chasing_score           =   chasing_score,
            team_current_score      =   team_current_score,
            current_wicket_index    =   wicket_index
        )
        
        print_score_board(playing_over, team_innings_score)
        
        if(chase_flag):
            if(team_innings_score > chasing_score):
                # print(f'Beat the score: chasing_score: {chasing_score}, team_innings_score: {team_innings_score}')
                
                gap()
    return team_innings_score

def play_team_a(team_a):
    
    #FIRST TEAM BATTING
    print(f'{team_a} batting: ')
    gap()
    
    team_a_total_score = play_innings(
        chase_flag              =   False,
        over_count              =   TOTAL_OVERS,
        chasing_score           =   0,
        team_current_score      =   0 )
    
    print(f'\n{team_a} scored: {team_a_total_score}')
    gap()

    print('-' * 70)
    
    return team_a_total_score


def play_team_b(
    team_b, 
    chasing_score):
    
    #SECOND TEAM BATTING
    print(f'{team_b} batting: ')
    gap()

    global team_b_total_score
    team_b_total_score = play_innings(
        chase_flag          =   True, 
        chasing_score       =   chasing_score,
        over_count          =   TOTAL_OVERS,
        team_current_score  =   team_b_total_score)
    
    print(f'\n{team_b} scored: {team_b_total_score}')

    gap()
    
    return team_b_total_score

def choose_winner(
    team_a,
    team_b,
    team_a_total_score,
    team_b_total_score
):
    
    if(team_b_total_score > team_a_total_score):
        print(f'{team_b} won')
    else:
        print(f'{team_a} won')
        return 
    
    if(team_b_total_score == team_a_total_score):
        print('Its a draw!')
    return 

def play_game():
    
    team_a = CURRENT_TEAMS[0]
    team_b = CURRENT_TEAMS[1]
    
    team_a_total_score = play_team_a(team_a)
    team_b_total_score = play_team_b(team_b, team_a_total_score)

    choose_winner(
    team_a,
    team_b,
    team_a_total_score,
    team_b_total_score

    )
    
    pass



def startpy():
    play_game()

if __name__ == '__main__':
    startpy()