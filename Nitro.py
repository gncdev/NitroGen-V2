import random
import string
from time import sleep
import requests


def gencode():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(19))


class NitroGenerator:
    def __init__(self):
        self.codes = []
        self.check()

    def check(self):
        while True:
            code = gencode()
            self.codes.append(code)
            response = requests.get(
                "https://discord.com/api/v7/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
            data = response.json()
            if data["message"] == 'Unknown Gift Code':
                print("Not worked: " + code)
            elif data["message"] == 'The resource is being rate limited.' or 'You are being rate limited.':
                print('Rate Limited: ' + code)
                print('Waiting')
                print(data)
                sleep(int(data['retry_after'])/1000)
            else:
                print("Worked: " + code)
                file = open("workedcodes.txt", "a+")
                file.write("\n" + code)


NitroGenerator()
