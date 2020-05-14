import random
import string

from selenium import webdriver
import warnings



def gencode():
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(19))


def check():
	warnings.filterwarnings('ignore')
	brwsr = webdriver.PhantomJS()
	while True:
		code = gencode()
		brwsr.get(
			"https://discordapp.com/api/v6/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
		comedtext = brwsr.find_element_by_xpath('/html/body/pre').text
		if comedtext[36:-29] == 'You are being rate limited.':
			print("Not worked: " + code)
		else:
			print("Worked: " + code)
			file = open("workedcodes.txt", "a+")
			file.write("\n"+code)


# https://discordapp.com/api/v6/entitlements/gift-codes/CODEE?with_application=false&with_subscription_plan=true

check()
