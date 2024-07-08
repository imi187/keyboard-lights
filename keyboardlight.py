#!/usr/bin/env python3

from pynput.keyboard import Key, Listener
import threading
import os
import time

timeout = 10
device = 'AT Translated Set 2 keyboard'
onStart = '/usr/bin/env msi-perkeyrgb --model gs65 -s 44cab9'
onEnd = '/usr/bin/env msi-perkeyrgb --model gs65 -s 000000'

countDown = 0
keyboardLighStatus = False

def countDownNow():

    global countDown
    global keyboardLighStatus

    if countDown > 1:
        threading.Timer(1, countDownNow).start()

    countDown = countDown - 1
    #print(countDown)

    if countDown == 0:
        os.system(onEnd)
        keyboardLighStatus = False

def on_press(key):

    global countDown
    global keyboardLighStatus

    countDown = timeout

    if keyboardLighStatus is False:
        keyboardLighStatus = True
        #print('ON')
        #print(countDown)
        os.system(onStart)
        countDownNow()

    #print('{0} pressed'.format(key))


def on_release(key):
    print('{0} release'.format(key))


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
