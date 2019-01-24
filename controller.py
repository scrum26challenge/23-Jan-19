#!/usr/bin/env python3

import os
import time


def game_loop(meeting_name,meeting_duration):
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        # FIXME This should have conditions to evaluate against checks in:
        #       - halftime, warning_*
        if counter == meeting_duration:
            return 'times up'


if __name__ == '__main__':
    meeting_name     = input('What\'s the name of your meeting? ')
    meeting_duration = input('How long is your meeting going to be? ')
    print(game_loop(meeting_name,meeting_duration))
