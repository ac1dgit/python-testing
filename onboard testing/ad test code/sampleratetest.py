import time
import ADS1256
import RPi.GPIO as GPIO


ADC = ADS1256.ADS1256()
ADC.ADS1256_init()
ADC.ADS1256_Read_data(1)

ADC_Value = ADC.ADS1256_GetChannalValue(0)

