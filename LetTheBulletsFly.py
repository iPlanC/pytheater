'''
Author: PlanC
Date: 2020-12-05 19:28:23
LastEditTime: 2020-12-09 22:06:01
FilePath: \pytheater\LetTheBulletsFly.py
'''

import random
import os
import theator

# define resolution of movie, medium for 640x360
resolution = theator.curtain.mini()
# set console to 64x36
os.system("mode con cols=" + str(int((resolution[0] / 10) * 2)) + " lines=" + str(int(resolution[1] / 10)))

# define some actors
Ma    = theator.actor("汤师爷", "马邦德", "师爷", "斯")
Zhang = theator.actor("张麻子", "张牧之", "县长", "毛")
Huang = theator.actor("黄老爷", "黄四郎", "老爷", "资")

# define each shot and duration (25fps)
def frame0() :
    theator.tools.showraw(12, 26, "南\t北")
    theator.tools.showraw(14, 26, "部\t洋")
    theator.tools.showraw(16, 26, "中\t年")
    theator.tools.showraw(18, 26, "国\t间")
    theator.tools.sleepframes(25 * 4)
    os.system("cls")

def frame1() :
    theator.tools.showraw(random.randint(1, 36), random.randint(1, 64), "长亭外")
    theator.tools.sleepframes(25 * 2)
    theator.tools.showraw(random.randint(1, 36), random.randint(1, 64), "古道边")
    theator.tools.sleepframes(25 * 2)
    theator.tools.showraw(random.randint(1, 36), random.randint(1, 64), "芳草碧连天")
    theator.tools.sleepframes(25 * 4)
    os.system("cls")

def frame2() :
    theator.tools.showraw(16, 1, "鹰")
    theator.tools.sleepframes(5)
    os.system("cls")
    theator.tools.showraw(18, 13, "鹰")
    theator.tools.sleepframes(5)
    os.system("cls")
    theator.tools.showraw(20, 25, "鹰")
    theator.tools.sleepframes(5)
    os.system("cls")
    theator.tools.showraw(18, 37, "鹰")
    theator.tools.sleepframes(5)
    os.system("cls")
    theator.tools.showraw(16, 49, "鹰")
    theator.tools.sleepframes(5)
    os.system("cls")

def frame3() :
    theator.tools.showraw(random.randint(1, 36), random.randint(1, 64), "晚风拂柳笛声残")
    theator.tools.sleepframes(25 * 2)
    theator.tools.showraw(random.randint(1, 36), random.randint(1, 64), "夕阳山外山")
    theator.tools.sleepframes(25 * 4)
    os.system("cls")

# play each frame from 0 to last frame
def play() :
    for i in range(3 + 1) :
        exec('frame{}()'.format(i))

if __name__ == "__main__" :
    exit
