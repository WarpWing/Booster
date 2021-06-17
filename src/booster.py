import time
import multiprocessing
import threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# Import Libraries

# Import song list from videos.txt and push it into a list. A quick and dirty fix
f = open("videos.txt", "r")
vidarray = []
for i in f:
    vidarray.append(i.strip())


# Import Video Class
class Video():
    
    def __init__(self, vidurl):
       self.vidurl = vidurl

    def boost(video):
        FFO = webdriver.FirefoxOptions() # FFO is FireFox Options
        FFO.headless = True
        FFP = webdriver.FirefoxProfile()
        FFP.set_preference("media.volume_scale", "0.0")
        browser = webdriver.Firefox(executable_path="./geckodriver",options=FFO,firefox_profile=FFP) # I know I should put variables in another section of the class but they won't recognize the variables. It's only one function so it's fine :)
        browser.get(f"{video.vidurl}")
        WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play']"))).click()
        time.sleep(60)
        browser.quit()
             


# Actual instance
for i in range(6): 
    for i in vidarray:
        x = Video(i)
        threading.Thread(target=x.boost).start()


