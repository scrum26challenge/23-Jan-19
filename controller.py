#!/usr/bin/env python3

import time


def game_loop(meeting_name,meeting_duration):
    # FIXME Check for the following conditions:
    #       - `meeting_duration` >= 1
    #       - `meeting_name`
    if isinstance(meeting_name,str) and isinstance(meeting_duration,int):
	    counter = 0
	    while True:
	        time.sleep(1)
	        # TODO This should have conditions to evaluate against checks in:
	        #      - `halftime`
	        #      - `warning_10`
	        #      - `warning_1`
	        #      - `warning_0` (i.e., `publish_message`)
	        if counter == meeting_duration: # max
	            return 'times up'
	        elif counter == (meeting_duration-60): # max - 60
	            counter += 1
	            print('1 minute left')
	        elif counter == (meeting_duration//2): # max / 2
	            print('halftime')
	            counter += 1
	        else:
	            counter += 1


if __name__ == '__main__':
    meeting_name     = str(input('What\'s the name of your meeting? '))
    meeting_duration = int(input('How long is your meeting going to be? '))
    print(game_loop(meeting_name,meeting_duration))
    #print(game_loop(None,None))
    #print(game_loop(0,0))
    #print(game_loop('a','a'))
    #print(game_loop(1.,1.))
    #print(game_loop(2,2))

# TODO 
#      - ceiling: 2147483647
#      - floor:  -2147483648
