from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
import time, pause, datetime

####################################################
#               FABS BOOKING BOT                   #
#                    v0.7                          #
# ------------------------------------------------ #
#                  To Do:                          #
# - make the time.sleep dependant on the loading   #
# - possibly a GUI                                 #
####################################################

PATH = "C:\Program Files (x86)\msedgedriver.exe" # Update for your Edge driver
edge_options = EdgeOptions()
edge_options.use_chromium = True
driver = Edge(executable_path=PATH, options=edge_options)
driver.get("https://nyuad.dserec.com/online/capacity_widget")

##########################################
#              USER SETTINGS             #
##########################################
username = "username" # Your login
password = "password" # Your password
facility = "facility" # "gym" or "pool" or "wogym"
slot = 3 #slot number, indexing starts at 1
##########################################

 This calculates when should the bot perform login and booking
if time.localtime()[3] <= 7:
	run = time.localtime()
elif time.localtime()[3] > 7:
	run = time.localtime(time.time() + 24*3600)
botlogin = datetime.datetime(run[0], run[1], run[2], 6, 55, 0)
botrun = datetime.datetime(run[0], run[1], run[2], 7, 0, 1)

# Navigates to desired facility
def choosefacility(facility):
	time.sleep(1)
	if facility == "gym":
		driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[1]/ul/li[8]").click() # clicks on the fitness center
	elif facility == "pool":
		driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[1]/ul/li[2]").click() # clicks on pool
	elif facility == "wogym":
		driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[1]/ul/li[13]").click() # clicks on the WO fitness center
	for i in range(2): # goes to the slot page of 2 days in advance
		driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/a[2]/i").click()
	time.sleep(1)

# Clicks on the slot
def pickslot(t):
	driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div/div/div/div["+str(t)+"]").click() # Clicks on the slot		
	time.sleep(1)
	if isitopen() == True: # Verifies if the slot is open, if not it will just close the action window
		try:
			driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[2]/button[2]").click() # Confirm selection
			return True # booking success
		except:
			return False
	elif isitopen() == False:
		driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button").click() # Close
		return False # booking fail

# Checks if the slot is open or not
def isitopen(): 
	txt = driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[1]").text # Reads the text
	if "will open" in txt:
		return False
	else:
		return True

# Logs in the user	
def login(user,pd):
	print("Freeze until 6:55AM")
	pause.until(botlogin) # if the login happens too early the session will expire	
	driver.find_element_by_xpath("/html/body/div/div/ul/li").click() # Click the login button
	driver.find_element_by_xpath("/html/body/div[2]/div[2]/a").click() # Logs in as a local User
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/input").send_keys(user) # As of now it is hardcored, because it doesn't accept variable 
	driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/input").send_keys(pd) # Inserts pwd
	driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/div/button").click() # Enter

# Commain chain
def book(facility, slot, username, password):

	login(username,password) # Logs in
	choosefacility(facility) # Navigates to desired facility

	print("Freeze until 7AM")
	pause.until(botrun) # Pauses until the system time is 7am and 1 second

	booked = False # Loop that will keep on trying to book until successful
	while booked == False:
		booked = pickslot(slot)
	print("Slot booked")

book(facility, slot, username, password)