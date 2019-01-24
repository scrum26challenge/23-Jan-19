#!/usr/bin/env python3

import os
import time


def game_loop(meeting_name):
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        # FIXME This should have conditions to evaluate against checks in:
        #       - halftime, warning_*


def halftime():
    placeholder = 10
    if t < placeholder:
        print('It\'s half-time!')


def warning_10():
    placeholder = 10
    if t < placeholder:
        print('There\'s 10 minutes remaining...')


def warning_1():
    placeholder = 1
    if t < placeholder:
        print('There\'s 1 minute remaining...')


if __name__ == '__main__':
    meeting_name = input('What\'s the name of your meeting? ')
    # TODO Add more user input fields...
    game_loop(meeting_name)
