#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 01:24:01 2020

@author: stefan
"""

import cv2
import os
import sys
import numpy as np


def change_brightness_linux(value):
    os.system('gdbus call --session --dest org.gnome.SettingsDaemon.Power --object-path /org/gnome/SettingsDaemon/Power --method org.freedesktop.DBus.Properties.Set org.gnome.SettingsDaemon.Power.Screen Brightness "<int32 ' + str(value) + '>"')
  
def change_brightness_windows(value):
    os.system('powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,'+value+')')
    

def main():  
    
    if(os.path.isfile('/home/stefan/.autoBacklight/stop')):
        sys.exit()
    camera=cv2.VideoCapture(0)
    if(camera.open(0)==False):
        sys.exit()
    ret, frame=camera.read()
    camera.release()
    avg=np.average(frame)
    value=np.uint32(np.round(avg))
    if(os.name=='posix'):
        change_brightness_linux(value)
    elif(os.name=='nt'):
        change_brightness_windows(2*value)
    

if __name__=='__main__':
    main()
