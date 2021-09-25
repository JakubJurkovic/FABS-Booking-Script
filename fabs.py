from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from msedge.selenium_tools import Edge, EdgeOptions

####################################################
#               FABS BOOKING BOT                   #
#                    v0.3                          #
# This script uses MsEdge driver & Selenium 3.14   #
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
username = "username"
password = "password"
facility = "facility" # "gym" or "pool"
slot = "1" # give relative numerical position of the slot, e.g. 1 if you want the first slot
##########################################


# Books from Co-Ed gym
def gym(t,user,pd):
	time.sleep(1)
	login(user,pd)
	actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 0,0) #r esets the mouse position
	actions.move_by_offset(50, 570).click().perform() # hardcoded position of the fitness center
	for i in range(2): # goes to the slot page of 2 days in advance
		driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/a[2]/i").click()
	time.sleep(1)
	pickslot(t,user,pd) # clicks on the slot

# Books for the swimming pool
def pool(t,user,pd):
	login(user,pd)
	actions.move_to_element_with_offset(driver.find_element_by_tag_name('body'), 0,0)
	actions.move_by_offset(50, 300).click().perform()
	for i in range(2):
		driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/a[2]/i").click()
	time.sleep(1)
	pickslot(t,user,pd)

# Clicks on the slot
def pickslot(t,user,pd):
	waitforseven() # A loop that will sleep the system until it is 7am
	driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div/div/div/div["+t+"]").click() # Clicks on the slot		
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div/section/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/div[2]/button[2]").click() # Confirm

# Logs in the user	
def login(user,pd):	
	driver.find_element_by_xpath("/html/body/div/div/ul/li").click() # Click the login button
	driver.find_element_by_xpath("/html/body/div[2]/div[2]/a").click() # Logs in as a local User
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/input").send_keys(user) # As of now it is hardcored, because it doesn't accept variable 
	driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/input").send_keys(pd) # Inserts pwd
	driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/div/button").click() # Enter

# A loop that will sleep the system for 1 sec until it is 7AM
def waitforseven():
	while (time.localtime()[3]) != 7:
		if time.localtime()[4] < 59:
			print(str((59-time.localtime()[4])*60)+" seconds") # Gives info for how many seconds is the code frozen
			time.sleep((59-time.localtime()[4])*60)

		else:
			print("1 sec")
			time.sleep(1)

def book(facility, slot, username, password):
	if facility == "gym":
		gym(slot, username, password)
	elif facility == "pool":
		pool(slot, username, password)

book(facility, slot, username, password)