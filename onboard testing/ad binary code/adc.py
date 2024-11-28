import RPi.GPIO as GPIO

# gain channel
GAIN = {'1' : 0, # GAIN   1
        '2' : 1, # GAIN   2
        '4' : 2, # GAIN   4
        '8' : 3, # GAIN   8
        '16' : 4,# GAIN  16
        '32' : 5,# GAIN  32
        '64' : 6,# GAIN  64
        }

# data rate
DATA_RATE = {'30000SPS' : 0xF0,
             '15000SPS' : 0xE0,
             '7500SPS' : 0xD0,
             '3750SPS' : 0xC0,
             '2000SPS' : 0xB0,
             '1000SPS' : 0xA1,
             '500SPS' : 0x92,
             '100SPS' : 0x82,
             '60SPS' : 0x72,
             '50SPS' : 0x63,
             '30SPS' : 0x53,
             '25SPS' : 0x43,
             '15SPS' : 0x33,
             '10SPS' : 0x20,
             '5SPS' : 0x13,
             '2d5SPS' : 0x03
             }

# registration definition
REG_DEF = {'STATUS' : 0,  # x1H
         'MUX' : 1,     # 01H
         'ADCON' : 2,   # 20H
         'DRATE' : 3,   # F0H
         'IO' : 4,      # E0H
         'OFC0' : 5,    # xxH
         'OFC1' : 6,    # xxH
         'OFC2' : 7,    # xxH
         'FSC0' : 8,    # xxH
         'FSC1' : 9,    # xxH
         'FSC2' : 10,   # xxH
        }

# command definition
CMD = {'WAKEUP' : 0x00,     # Completes SYNC and Exits Standby Mode 0000  0000 (00h)
       'RDATA' : 0x01,      # Read Data 0000  0001 (01h)
       'RDATAC' : 0x03,     # Read Data Continuously 0000   0011 (03h)
       'SDATAC' : 0x0F,     # Stop Read Data Continuously 0000   1111 (0Fh)
       'RREG' : 0x10,       # Read from REG rrr 0001 rrrr (1xh)
       'WREG' : 0x50,       # Write to REG rrr 0101 rrrr (5xh)
       'SELFCAL' : 0xF0,    # Offset and Gain Self-Calibration 1111    0000 (F0h)
       'SELFOCAL' : 0xF1,   # Offset Self-Calibration 1111    0001 (F1h)
       'SELFGCAL' : 0xF2,   # Gain Self-Calibration 1111    0010 (F2h)
       'SYSOCAL' : 0xF3,    # System Offset Calibration 1111   0011 (F3h)
       'SYSGCAL' : 0xF4,    # System Gain Calibration 1111    0100 (F4h)
       'SYNC' : 0xFC,       # Synchronize the A/D Conversion 1111   1100 (FCh)
       'STANDBY' : 0xFD,    # Begin Standby Mode 1111   1101 (FDh)
       'RESET' : 0xFE,      # Reset to Power-Up Values 1111   1110 (FEh)
      }

def wait_drdy(DRDY_PIN):
    for i in range(0,400000,1):
        if(GPIO.input(DRDY_PIN) == 0):
         break
    if(i >= 400000):
        print ("Time Out ...\r\n")