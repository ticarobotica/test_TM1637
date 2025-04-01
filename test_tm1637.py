#Senzorul TM1637

from machine import Pin
from time import sleep, localtime
from tm1637 import TM1637


tm=TM1637(clk=Pin(22), dio=Pin(21))

while True:
    ora,min=localtime()[3:5]
    tm.numbers(ora,min)
    print("Ora = ",ora," si minutul = ",min," ", end="\r")
    sleep(1)
    