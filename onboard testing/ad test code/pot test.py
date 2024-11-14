import time
import ADS1256
import RPi.GPIO as GPIO


ADC = ADS1256.ADS1256()
ADC.ADS1256_init()

while(True):
    ADC_Value = ADC.ADS1256_GetAll()
    print ("0 ADC = %lf"%(ADC_Value[0]*5.0/0x7fffff))
