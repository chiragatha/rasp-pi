#!/usr/bin/python
#import

import RPi.GPIO as GPIO
import time
from time import sleep
import os
import urllib2
from datetime import datetime
from datetime import date
import datetime
from array import array
import client
from client import txtfile
from client import decision
from RPLCD import CharLCD, cleared, cursor
GPIO.setwarnings(False)

# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 3
LCD_D5 = 2
LCD_D6 = 11
LCD_D7 = 5
LED_ON = 15

print 'LCD Sample App Started...'

# Define some device constants
LCD_WIDTH = 20    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

print 'step-1'
def main():
  # Main program block
 
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7
  GPIO.setup(LED_ON, GPIO.OUT) # Backlight enable

  print 'step-2'
 
  # Initialise display
  lcd_init()

  print 'step-3'
 
  # Toggle backlight on-off-on
  lcd_backlight(True)
  time.sleep(0.5)
  lcd_backlight(False)
  time.sleep(0.5)
  lcd_backlight(True)
  time.sleep(0.5)

  print 'step-4'
 
  while False:

    print 'inside while'
    # Send some centred test
    lcd_string("--------------------",LCD_LINE_1,2)
    lcd_string("Rasbperry Pi",LCD_LINE_2,2)
    lcd_string("Model B",LCD_LINE_3,2)
    lcd_string("--------------------",LCD_LINE_4,2)

    print 'inside while1' 
    time.sleep(3) # 3 second delay
 
    lcd_string("Raspberrypi-spy",LCD_LINE_1,3)
    lcd_string(".co.uk",LCD_LINE_2,3)
    lcd_string("",LCD_LINE_3,2)
    lcd_string("20x4 LCD Module Test",LCD_LINE_4,2)
 
    time.sleep(3) # 20 second delay
 
    # Blank display
    lcd_byte(0x01, LCD_CMD)
 
    time.sleep(3) # 3 second delay
 
def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_string(message,line,style):
  # Send string to display
  # style=1 Left justified
  # style=2 Centred
  # style=3 Right justified
 
  if style==1:
    message = message.ljust(LCD_WIDTH," ")
  elif style==2:
    message = message.center(LCD_WIDTH," ")
  elif style==3:
    message = message.rjust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
 
def lcd_backlight(flag):
  # Toggle backlight on-off-on
  GPIO.output(LED_ON, flag)
class keypad():
    # CONSTANTS   
    KEYPAD = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
    ["*",'0',"#"]
    ]
     
    ROW         = [18,23,24,25]
    COLUMN      = [4,17,22]
     
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
     
    def getKey(self):
         
        # Set all columns as output low
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
         
        # Set all rows as input
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
         
        # Scan rows for pushed key/button
        # A valid key press should set "rowVal"  between 0 and 3.
        rowVal = -1
        for i in range(len(self.ROW)):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i
                 
        # if rowVal is not 0 thru 3 then no button was pressed and we can exit
        if (rowVal <0) or (rowVal>3):
            self.exit()
            return
         
        # Convert columns to input
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
         
        # Switch the i-th row found from scan to output
        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)
 
        # Scan columns for still-pushed key/button
        # A valid key press should set "colVal"  between 0 and 2.
        colVal = -1
        for j in range(len(self.COLUMN)):
            tmpRead = GPIO.input(self.COLUMN[j])
            if tmpRead == 1:
                colVal=j
                 
        # if colVal is not 0 thru 2 then no button was pressed and we can exit
        if (colVal <0) or (colVal>2):
            self.exit()
            return
 
        # Return the value of the key pressed
        self.exit()
        return self.KEYPAD[rowVal][colVal]
         
    def exit(self):
        # Reinitialize all rows and columns as input at exit
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
if __name__ == '__main__':
    try:
        main()
        kp = keypad()
        lcd_string("Welcome to IMOBPOS",LCD_LINE_2,2)
        #lcd_string("Choose Payment mode",LCD_LINE_2,2)
        lcd_string(" 1-Card   2-Aadhaar ",LCD_LINE_3,2)
        lcd_string("3-Wallet 4-Bitcoin",LCD_LINE_4,2)
        
        os.system("gpio mode 6 out && gpio mode 5 out")

        while True:
            try:
                urllib2.urlopen("http://www.google.com").close()
            except urllib2.URLError:
                print "Not Connected"
                symbol = "X"
                #symbol1="X"
                os.system("gpio write 6 0 && gpio write 5 1")
                time.sleep(1)
                break
            else:
                print "Connected"
                symbol ="W"
                #symbol1="B"
                os.system("gpio write 6 1 && gpio write 5 0")
                break
            finally:
                lcd_string("%s"%(symbol),LCD_LINE_1,3)    
        def digit():
            num = None
            while num == None:
                num = kp.getKey()
            return num
        def disp(d):
            lcd_string(d,LCD_LINE_2,1)
            lcd_string("",LCD_LINE_1,2)
            lcd_string("",LCD_LINE_3,2)
            lcd_string("",LCD_LINE_4,2)

        
        def q(d):
            if d == '#':
                  os.system('python Main.py')
                
            if d =='1':
                  print "1 is selected"
                  disp("Swipe Your Card")
                  info = "4264190134426294=19121010010300"
                  #info =raw_input("Please swipe the card")
                  if info >= 1:
                      parameter = "1"
                      client.decision(parameter)
                      file=open("tosend.txt",'w')
                      info=info.replace(' ' ,' ' )
                      if (int(info[0]) == 4):
                          print("\nIt is a VISA card")
                      elif(int(info[0]) == 5):
                          print("It is a MASTER card")
                      elif(int(info[0]) == 6):
                          print("It is a Discover card")
                                  
                      year=int("20"+info[17]+info[18])
                      month=int(info[19]+info[20])
                      print("year is %s and month is %s" %(year,month))   
                      now = datetime.datetime.now()
                      current_year = now.year
                      current_month = now.month
                      print (current_year)
                      if (year == current_year and month <= current_month):
                          print("card is valid")
                          file.write("%s"%(info))
                          file.close()
                          client.txtfile(info)
                      elif (year > current_year):
                          print("Card is valid")
                          file.write("%s"%(info))
                          file.close()
                          client.txtfile(info)
                      else:
                          print("Card Invalid")

                  elif card_info == None:
                      print("No data received")
                  else:
                      print("No data received")
                  print ('Closing connection...')


                  lcd_string("Thank you",LCD_LINE_3,2)
                  sleep(5)
                  os.system('python Main.py')
                  
                  
            if d =='2':
                  parameter ='2'
                  client.decision(parameter)
                  print "2 is selected"
                  os.system('python merge.py')
                  sleep(5)
                  os.system('python Main.py')
                  
            if d =='3':
                  print "Wallet is selected"
                  lcd_string("Choose Your Wallet",LCD_LINE_1,2)
                  lcd_string("1-Mobikwik 2-Oxigen ",LCD_LINE_2,2)
                  lcd_string("3-Wirecard 4-IMOBPOS",LCD_LINE_3,2)
                  lcd_string("5-Freecharge",LCD_LINE_4,2)

                  def r(m):
                    if m == '#':
                      lcd_string('Thank you',LCD_LINE_2,2)
                      sleep(5)
                      os.system('python Main.py')
                    if m == '1':
                      print "Mobikwik is selected"
                      disp("Mobikwik is selected")
                      sleep(5)
                      os.system('python Main.py')
                    if m == '2':
                      print "Oxigen is selected"
                      disp("Oxigen is selected")
                      sleep(5)
                      os.system('python Main.py')
                    if m == '3':
                      print "Wirecard is selected"
                      disp("Wirecard is selected")
                      sleep(5)
                      os.system('python Main.py')
                    if m == '4':
                      print "IMOBPOS is selected"
                      disp("IMOBPOS is selected")
                      sleep(5)
                      os.system('python Main.py')
                    if m == '5':
                      print "Freecharge is selected"
                      disp("Freecharge is selected")
                      sleep(5)
                      os.system('python Main.py')

                  d2 = digit()
                  r(d2)
                  sleep(1)

                  
                  
            if d =='4':
                  print "Bitcoin is selected"
                  disp("Bitcoin is Selected")
                  sleep(5)
                  os.system('python Main.py')
                  
                    
                  
                  
        
        d1 = digit()
        q(d1)
        sleep(1)
               
        
        

    except KeyboardInterrupt:
        pass
    finally:
        print("")
        
  
  
