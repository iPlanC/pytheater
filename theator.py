'''
Author: PlanC
Date: 2020-12-05 20:57:02
LastEditTime: 2020-12-09 21:30:29
FilePath: \pytheater\theator.py
'''

import curses
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

    def position(self, X, Y) :
        self.posX = X
        self.posY = Y
        stdscr.addstr(X, Y, self.shortname)
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

if __name__ == "__main__" :
    exit
