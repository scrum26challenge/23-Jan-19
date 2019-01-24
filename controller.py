#!/usr/bin/env python3

import os
import time

#def check_time():
#    

def game_loop(meeting_name,meeting_duration):
    counter = 0
    while True:
        time.sleep(1)
        # FIXME This should have conditions to evaluate against checks in:
        #       - halftime, warning_*
        if counter == meeting_duration:
            return 'times up'
        else:
            counter += 1


if __name__ == '__main__':
    meeting_name     = str(input('What\'s the name of your meeting? '))
    meeting_duration = int(input('How long is your meeting going to be? '))
    print(game_loop(meeting_name,meeting_duration))
    print(game_loop(None,None))
    print(game_loop(0,0))
    print(game_loop('a','a'))
    print(game_loop(1.,1.))
    print(game_loop(2,2))
