import requests
import misc

def check(token):
    try:
        data = requests.post("https://hcaptcha.com/siteverify", {"secret": misc.config["captcha"]["secret"], "response": token}).json()["success"]
        return data
    except:
        return False