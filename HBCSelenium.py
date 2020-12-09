#webscraping Hollywood Ballroom using selenium 
import selenium 
from selenium import webdriver 
import time
import os.path
from os import path 


DRIVER_PATH = '/Users/rekikziku/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.keepandshare.com/calendar18/show.php?i=2582549&ifr=y&colorreset=y&vw=month&style=month&width=900&height=1600&scroll=y&themeChoice=777&dbc=600002&hc=FDFFDC&htc=600002&mntc=600002&mnbc=fffcfc&tbtc=000000&mbtc=FDFFDC&mbc=600002&mbbtc=600002&mbbc=FDFFDC&ltc=621300&sdc=fffcfc&pdc=fffcfc&tc=fffcfc&fdc=fffcfc&wdc=fffcfc&dehc=fffcfc&dehtc=60002&lgc=600002&lgtc=ffff99&nopopup=n&fsz=10&noviewmenu=n&noname=y&norequest=n&nobookings=n&nobreak=y&noprint=n&nosearch=y&noovl=n&notz=y&fd=y&sa=y&exedit=y&nonav=n&tagl=-1&ovll=-1")
#print(driver.title)
#driver.quit()

print("Hello World!")

"""
fname = "HollywoodBallroomCalander.csv"
FileExist = 1

if not path.exists(fname):
	FileExist = 0
f = open(fname)
if FileExist == 0:
	f.write("Date, Price, Time, Instructor")
"""


#all_links = driver.find_elements_by_class_name("daynum cal_date cal_display_border cal_display_monthdatenumber_textcolor cal_display_monthdatenumber_bgcolor")
all_links = driver.find_elements_by_class_name("cal_date") #date
all_links = driver.find_elements_by_class_name("calEventDisplay")
all_links = driver.find_elements_by_style("color: #000000;") # details 
all_links = driver.find_elements_by_style("color: #660000;") #name 

for posts in all_links:
	print(posts.text)



lstdata = [posts.text for posts in all_links]

with open('HBC.csv', 'w', newline='Date, Link') as csvfile:
    writer = csv.writer(csvfile)
   	writer.writerow(lstdata)
   	 #cvsWriter = csv.writer(csvfile, delimiter=',')
     #cvsWriter.writerow(header)
     #cvsWriter.writerows(sortedlist)
