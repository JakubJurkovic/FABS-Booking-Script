from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from msedge.selenium_tools import Edge, EdgeOptions

####################################################
#               FABS BOOKING BOT                   #
#                    v0.4.3                        #
# This script uses MsEdge driver & Selenium 3.14   #
# The bot requires a "local account" on FABS       #
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

##########################################
#              USER SETTINGS             #
##########################################
username = "username"
password = "password"
facility = "facility" # "gym" or "pool"
slot = "1" # give relative numerical position of the slot, e.g. 1 if you want the first slot
##########################################


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
	waitforseven() # A loop that will sleep the system until it is 7am
	driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div/div/div/div["+str(t)+"]").click() # Clicks on the slot		
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[2]/button[2]").click() # Confirm

# Logs in the user	
def login(user,pd):
	waitforsix55() # if the login happens too early the session will expire	
	driver.find_element_by_xpath("/html/body/div/div/ul/li").click() # Click the login button
	driver.find_element_by_xpath("/html/body/div[2]/div[2]/a").click() # Logs in as a local User
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/input").send_keys(user) # As of now it is hardcored, because it doesn't accept variable 
	driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/input").send_keys(pd) # Inserts pwd
	driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/div/button").click() # Enter

# A loop that will sleep the system for 1 sec until it is 7AM
def waitforseven():
	while (time.localtime()[3]) < 7:
		if time.localtime()[4] < 59:
			print("Waiting for "+str((59-time.localtime()[4])*60)+" seconds") # Gives info for how many seconds is the code frozen
			time.sleep((59-time.localtime()[4])*60)

		else:
			print("Waiting for 1 sec")
			time.sleep(1)

# A loop that will sleep the system until 6:55AM
def waitforsix55():
	while time.localtime()[3] < 6 and time.localtime()[4] < 55:
		if time.localtime()[4] < 54:
			print("Waiting for "+str((54-time.localtime()[4])*60)+" seconds") # Gives info for how many seconds is the code frozen
			time.sleep((54-time.localtime()[4])*60)

		else:
			print("Waiting for 1 sec")
			time.sleep(1)

def book(facility, slot, username, password):
	login(username,password)
	if facility == "gym":
		gym(slot)
	elif facility == "pool":
		pool(slot)

book(facility, slot, username, password)