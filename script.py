from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import random 
import time


#setting browser
driver = webdriver.Chrome() 
actions = ActionChains(driver)
url = 'https://tinder.com/'
driver.get(url)
#logging in an getting up to the swipping stage
time.sleep(5)
element = driver.find_element_by_xpath("//span[text() = 'Log in with phone number']")
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//div[starts-with(@class, 'Fz')]")
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//input[contains(@placeholder, 'Search')]")
element.click()
element.send_keys('Argentina')
time.sleep(5)
element = driver.find_element_by_xpath("//span[text() = 'Argentina']")
element.click()
element = driver.find_element_by_name("phone_number")
element.send_keys(91164320135)
time.sleep(2)
element = driver.find_element_by_xpath("//span[text() = 'Continue']")
element.click()
user_input = str(input("Code Received: "))
element = driver.find_elements_by_xpath("//input[contains(@class, 'Fz')]")
for i in element:
	i.send_keys(user_input[element.index(i)])
element = driver.find_element_by_xpath("//span[text() = 'Continue']")
element.click()
time.sleep(3)
#once logged in
element = driver.find_element_by_xpath("//span[contains(text(), 'Allow')]")
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//button[@aria-label= 'Enable']")
element.click()
time.sleep(2)
element = driver.find_element_by_xpath("//span[text() = 'I Accept']") 
element.click()
time.sleep(5)

def human_lagging():
	if random.randint(0,1) ==1:
		actions.send_keys(Keys.ARROW_UP).perform()
		time.sleep(random.uniform(2,4))

	time.sleep(random.randint(1,2))
	for i in range(random.randint(0,3)):
		actions.send_keys(Keys.SPACE).perform()
		time.sleep(random.uniform(2,3))


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
			continue

def first_interaction():	
	pick_up_lines = ['You seem interesting, like someone I\'d like to know better. So tell me, when was the last time you did something truly sponteanour or adventurous?',
					'Hey, better Sunday adventure: Netflix binges, hot yoga class or agressive tequila sipping?', 
					'Cereal First Or Milk First?', 
					'You\'ve got one joke to lighten the mood, this is a critical moment here. Hit me with your best weapon. What\'s the joke?' , 
					'Just looking to make a bid', 
					'A plateau', 
					'So do you have any killer opening lines on Tinder?',
					'Hi, I\'d like to add you to my professional network on Linkedin', 
					'Hit me with your best joke or pun haha',
					'You\'re cute, bet you have a great laugh', 
					'Love your profile,looks like you know how to have fun. Have you been (travelling, playing sport, going out) lately?',
					'Sorry for being so direct, but WOW.', 
					'Touche, I like the way you swipe!', 
					'Hey you\'re so cinematic'
					'Hi, you are a lucky girl', 
					'You\'re so cute, i\'d hold your hand in public', 
					'You don\'nt know how many times I had to swipe left to find you', 
					'Prettiest smile, I\'ve seen on tinder',
					'That akward moment when you try to message a girl and all you can think of is hello', 

					]
	matches = driver.find_elements_by_xpath("//a[contains(@class, 'matchListItem')]")
	del matches[0]
	for i in matches:
		message_box = driver.find_element_by_xpath("//textarea[contains(@placeholder, 'Type a message')]")
		matches[i].click()
		message_box.send_keys(random.choice(pick_up_lines))
		time.sleep(3)
		actions.send_keys(Keys.ENTER).perform()


def second_hit():
	restarting_lines = ['Or if youre hoping Ill post some shirtless gym selfies, before you respond... you are in luck. They\'ll be up later this week',
						'Uh oh, radio silence. Should I grab my cape and tights to come rescue you?']
	
	driver.find_element_by_xpath("//button[text()= 'Messages']").click()

	message_matches = driver.find_elements_by_xpath("//div[contains(@class, 'Ell')]")
	for i in message_matches:
		i.click()
		total_messages = len(driver.find_elements_by_xpath("//span[contains(@class, 'text')]"))
		if total_messages == 2:
			restarting_line = random.choice(restarting_lines)
			message_box.send_keys(restarting_line)
			time.sleep(2)
			actions.send_keys(Keys.ENTER).perform()	

input('Password to run program:')
while True :
	try: 
		human_lagging()
		swiping()
	except:
		try: 
			while True :
				first_interaction()
		except:
			while True :
				second_hit()



		