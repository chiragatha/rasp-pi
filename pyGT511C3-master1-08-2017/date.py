#!/usr/bin/python

from datetime import datetime
from time import sleep, strftime
from Main import *

# Main program block

# Initialise display
lcd_init()
print "Clock starting"
try:
    while True:
        lcd_byte(LCD_LINE_1, LCD_CMD)
        lcd_string(datetime.now().strftime('Today is : ' + '%A'),2)
        lcd_byte(LCD_LINE_2, LCD_CMD)
        lcd_string(datetime.now().strftime('%B %d %Y'),2)
        lcd_byte(LCD_LINE_3, LCD_CMD)
        lcd_string(datetime.now().strftime('Time: ' + '%r'),2)
        lcd_byte(LCD_LINE_4, LCD_CMD)
        lcd_string(datetime.now().strftime('*** RaspberryPi ***'),2)
        sleep(1)
except KeyboardInterrupt:
    lcd_clear()

# LINUX Command: date
# %A day of the week
# %a locale's abbreviated weekday name (Sun..Sat)
# %B locale's full month name, variable length (January..December)
# %c locale's date and time (Sat Nov 04 12:02:33 EST 1989)
# %d day of month (01..31)
# %D date (mm/dd/yy)
# %e day of month, blank padded ( 1..31)
# %p locale's upper case AM or PM indicator (blank in many locales)
# %P locale's lower case am or pm indicator (blank in many locales)
# %H hour (00..23)
# %I hour (01..12)
# %m month (01..12)
# %M minute (00..59)
# %r time, 12-hour (hh:mm:ss [AP]M)%Rtime, 24-hour (hh:mm)
# %s seconds since `00:00:00 1970-01-01 UTC' (a GNU extension)
# %S second (00..60); the 60 is necessary to accommodate a leap second
# %T time, 24-hour (hh:mm:ss)%uday of week (1..7); 1 represents Monday
# %U week number of year with Sunday as first day of week (00..53)
# %V week number of year with Monday as first day of week (01..53)
# %w day of week (0..6); 0 represents Sunday
# %W week number of year with Monday as first day of week (00..53)
# %x locale's date representation (mm/dd/yy)
# %X locale's time representation (%H:%M:%S)
# %y last two digits of year (00..99)
# %Y year (1970...)
# %z RFC-822 style numeric timezone (-0500) (a nonstandard extension)
# %Z time zone (e.g., EDT), or nothing if no time zone is determinable
