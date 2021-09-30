from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from msedge.selenium_tools import Edge, EdgeOptions
import time, pause, datetime

####################################################
#               FABS BOOKING BOT                   #
#                    v0.5                          #
# Requirements:                                    #
# MsEdge driver & Selenium 3.14                    #
# "local account" on FABS                          #
# pause package (pip install pause)                #
# ------------------------------------------------ #
#                  To Do:                          #
# - make the time.sleep dependant on the loading   #
# - possibly a GUI                                 #
####################################################

PATH = "C:\Program Files (x86)\msedgedriver.exe" # Update for your Edge driver
edge_options = EdgeOptions()
edge_options.use_chromium = True
driver = Edge(executable_path=PATH, options=edge_options)
actions = ActionChains(driver)
driver.get("https://nyuad.dserec.com/online/capacity_widget")

#              USER SETTINGS             #
##########################################
username = "your username"
password = "your password"
facility = "1" # "gym" or "pool"
slot = 3 #slot number, indexing starts at 1
##########################################


# This calculates when should the bot run
if time.localtime()[3] <= 7:
	run = time.localtime()
elif time.localtime()[3] > 7:
	run = time.localtime(time.time() + 24*3600)

botlogin = datetime.datetime(run[0], run[1], run[2], 6, 55, 0)
botrun = datetime.datetime(run[0], run[1], run[2], 7, 0, 1)


# Books from Co-Ed gym
def gym(t):
	time.sleep(1)
	actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 50,600).click().perform() #clicks on the fitness center
	for i in range(2): # goes to the slot page of 2 days in advance
		driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/a[2]/i").click()
	time.sleep(1)
	pickslot(t) # clicks on the slot

# Books for the swimming pool
def pool(t):
	time.sleep(1)
	actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 50,330).click().perform()
	for i in range(2):
		driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/a[2]/i").click()
	time.sleep(1)
	pickslot(t)

# Clicks on the slotF
def pickslot(t):
	print("Freeze until 7AM")
	pause.until(botrun) # Pauses until the system time is 7am and 1 second
	driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div/div/div/div["+str(t)+"]").click() # Clicks on the slot		
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[2]/button[2]").click() # Confirm

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

def book(facility, slot, username, password):
	login(username,password)
	if facility == "gym":
		gym(slot)
	elif facility == "pool":
		pool(slot)

book(facility, slot, username, password)