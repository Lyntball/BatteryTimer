#!/usr/bin/python3

'''This Program is to help document the uptime of
a RaspberryPi System being powered by JUST a battery pack.
a file is made on the users desktop and can be reviewed for
total uptime.
Created By Lynton Brown 11/14/2018'''

from time import sleep ##import sleep
from os import getenv ##import getenv

hourMultiplier=3600 ##define multiplier for hour
minuteMultiplier=60 ##define multiplier for minutes
secondMultiplier=1 ##define multiplier for seconds

multiplier=secondMultiplier ##define which multiplier to use

def WriteFile(): ##Define WriteFile Function
    timer=0 ##set Timer at 0 at begining of program
    while True: ##keep the function running FFFOOORRREEEVVVEEERRR(pronounced the same way as in The Sandlot)
        with(open(FilePath(),"w"))as timerFile: ##open a new file in write mode
            timerFile.write(Formatter(timer)) ##Write Information to file
##            timerFile.close() ##close file (not really needed but just makes me feel better. File will be closed once 'with' statment is left)
        timer=Timer(timer) ##timer is now equal to value of function

def FilePath(): ##Define FilePath Function
    path=getenv("HOME")+"/Desktop/BatteryTimer.Lynton" ##Define file path and why not do a name drop
##    print(path) ##Debug
    return(path) ##return the file path

def Formatter(timer): ##Define Formatter Function
    if(multiplier==secondMultiplier): ##if Second was choosen as the multiplier
        hour=int(timer/hourMultiplier) ##hour is timer devided by hour multiplier (int to keep it positive)
        minute=(int(timer/minuteMultiplier)-int(hour*hourMultiplier)) ##minute is timer devided by minute multiplier minus hour times hour multiplier (int to keep it positive)
        second=(int(timer)-int(minute*minuteMultiplier)-int(hour*hourMultiplier)) ##second is timer minus minute times minute multiplier minus hour times hour multiplier (int to keep it positive)
    if(multiplier==minuteMultiplier): ##if Minute was choosen as the multiplier
        hour=int(timer/minuteMultiplier) ##hour is timer devided by minute multiplier (int to keep it positive)
        minute=(int(timer)-int(hour*minuteMultiplier)) ##minute is timer minus hour times minute multiplier (int to keep it positive)
        second=0 ##Seconds is left a 0
    if(multiplier==hourMultiplier): ##if Hour was choosen as the multiplier
        hour=int(timer)##hour is timer (int to keep it positive)
        minute=0 ##Minutes is left a 0
        second=0 ##Seconds is left at 0
    formatedTimer=("Up Time:\n%02d:%02d:%02d"%(hour,minute,second)) ##Build String to pass along
##    print formatedTimer ##Debug
    return(formatedTimer) ##return the string

def Timer(timer): ##Define Timer Function
    timer=timer+1 ##add 1 to value of timer
    sleep(multiplier) ##stop everything for multiplier value(passed as seconds)
##    print(timer) ##Debug
    return(timer) ##return timer value

WriteFile() ##Call WriteFile Function To start the program
