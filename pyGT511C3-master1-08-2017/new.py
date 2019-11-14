from datetime import date
import datetime
from array import array
import client
from client import txtfile
import os
info = "4264190134426294=19121010010300"

if info >= 1:
    file=open("tosend.txt",'w')
    info=info.replace(' ' ,' ' )
    if (int(info[0]) == 4):
        print("\nIt is a VISA card")
    elif(int(info[0]) == 5):
        print("It is a MASTER card")
    elif(int(info[1]) == 6):
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
        file.write("Card Info: %s, Validity year:  %s, Validity month:  %s "%(info,year,month))
        file.close()
        client.txtfile(info)
    elif (year > current_year):
        print("Card is valid")
        file.write("Card Info: %s, Validity year:  %s, Validity month:  %s "%(info,year,month))
        file.close()
        client.txtfile(info)
    else:
        print("Card Invalid")

elif card_info == None:
    print("No data received")
else:
    print("No data received")


   
os.system('python fingerprint.py')
print ('Closing connection...')

