'''
Author: PlanC
Date: 2020-12-05 20:57:02
LastEditTime: 2020-12-10 14:00:00
FilePath: \pytheater\theator.py
'''

import curses
import os
import pygame
import time

stdscr = curses.initscr()
stdscr.clear()
stdscr.refresh()

class actor :
    def __init__ (self, shortname, fullname, fakename, historyname) :
        self.shortname      = shortname
        self.fullname       = fullname
        self.fakename       = fakename
        self.histroyname    = historyname

    def position(self, X, Y, reverse) :
        self.posX = X
        self.posY = Y
        if reverse :
            stdscr.addstr(X, Y, self.shortname)
        else :
            stdscr.addstr(X, Y, self.shortname[::-1])
        stdscr.refresh()

    def speak(self, offset, content) :
        stdscr.addstr(self.posX - 1, self.posY + offset, "/")
        stdscr.addstr(self.posX - 2, self.posY + offset + offset, content)
        stdscr.refresh()

class curtain :
    def mini() :
        return 640, 360
    def medium() :
        return 1280, 720
    def big() :
        return 1920, 1080
    def __inhuman() :
        return 1366, 768

class tools :
    def sleepframe() :
        time.sleep(0.04)

    def sleepframes(frames) :
        for i in range(frames):
            time.sleep(0.04)

    def showraw(X, Y, content) :
        stdscr.addstr(X, Y, content)
        stdscr.refresh()

    def clean() :
        os.system("cls")

    def mix(filepath) :
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        pygame.mixer.music.fadeout(60000)


if __name__ == "__main__" :
    exit
