from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import random 
import time


#setting browser
driver = webdriver.Chrome(ChromeDriverManager().install())
actions = ActionChains(driver)
url = 'https://tinder.com/'
driver.get(url)


def human_lagging():
	if random.randint(0,1) ==1:
		actions.send_keys(Keys.ARROW_UP).perform()
		time.sleep(random.uniform(4,6))

	time.sleep(random.randint(3,5))
	for i in range(random.randint(0,3)):
		actions.send_keys(Keys.SPACE).perform()
		time.sleep(random.uniform(5,7))


def swiping():
	try: 
		alternatives = ['swipe_right', 'swipe_left']
		choice = random.choices(alternatives, weights = [0.75, 0.25])
		if choice[0] == alternatives[0]:
			actions.send_keys(Keys.ARROW_RIGHT).perform()
		elif choice[0] == alternatives[1]:
			actions.send_keys(Keys.ARROW_LEFT).perform()
			if random.uniform(0,1) > 0.9:
				element = driver.find_element_by_xpath("//button[contains(@aria-label, 'Rewind')]")
				element.click()
			
		time.sleep(2)
		print(choice[0] + 'with a ' + str(random.uniform(0,1)) +'certainty')
	except:
		time.sleep(3)
		try:
			driver.find_element_by_xpath("//span[text()= 'Not interested']")
			driver.click()
		except:
			pass

hola = input('Send input once you are finished')
while True :
	human_lagging()
	swiping()




		