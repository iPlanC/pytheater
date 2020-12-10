'''
Author: PlanC
Date: 2020-12-05 19:28:23
LastEditTime: 2020-12-10 14:07:27
FilePath: \pytheater\LetTheBulletsFly.py
'''

import random
import os
from time import thread_time
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
# shot0 show raw content "北洋年间 南部中国" for 4 second 100 frames
def shot0() :
    theator.tools.showraw(12, 26, "南\t北")
    theator.tools.showraw(14, 26, "部\t洋")
    theator.tools.showraw(16, 26, "中\t年")
    theator.tools.showraw(18, 26, "国\t间")
    theator.tools.sleepframes(25 * 4)
    theator.tools.clean()

# shot1 show raw content "长亭外 古道边 芳草碧连天" at random place for 2/2/4 seconds 50/50/100 frames
def shot1() :
    theator.tools.showraw(random.randint(1, 36), random.randint(1, 58), "长亭外")
    theator.tools.sleepframes(25 * 2)
    theator.tools.showraw(random.randint(1, 36), random.randint(1, 58), "古道边")
    theator.tools.sleepframes(25 * 2)
    theator.tools.showraw(random.randint(1, 36), random.randint(1, 54), "芳草碧连天")
    theator.tools.sleepframes(25 * 4)
    theator.tools.clean()

# shot2 show raw content "a eagle fly over" for 1 second 5 frames frash rate
def shot2() :
    theator.tools.showraw(16, 1, "鹰")
    theator.tools.sleepframes(5)
    theator.tools.clean()
    theator.tools.showraw(18, 13, "鹰")
    theator.tools.sleepframes(5)
    theator.tools.clean()
    theator.tools.showraw(20, 25, "鹰")
    theator.tools.sleepframes(5)
    theator.tools.clean()
    theator.tools.showraw(18, 37, "鹰")
    theator.tools.sleepframes(5)
    theator.tools.clean()
    theator.tools.showraw(16, 49, "鹰")
    theator.tools.sleepframes(5)
    theator.tools.clean()

def shot3() :
    theator.tools.showraw(random.randint(1, 36), random.randint(1, 50), "晚风拂柳笛声残")
    theator.tools.sleepframes(25 * 2)
    theator.tools.showraw(random.randint(1, 36), random.randint(1, 54), "夕阳山外山")
    theator.tools.sleepframes(25 * 4)
    theator.tools.clean()

# background music
def shot4() :
    theator.tools.mix("久石譲 - 太阳照常升起.mp3")

def shot5() :
    pass

# play each frame from 0 to last frame
def play() :
    for i in range(4, 4 + 1) :
        exec('shot{}()'.format(i))

if __name__ == "__main__" :
    #exit
    play()
