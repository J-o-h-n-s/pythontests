from asyncio import wait_for
import logging
import time
import os
from os.path import join, dirname
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from discordwebhook import Discord

os.system('cls' if os.name == 'nt' else 'clear')

print('Initializing...')

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
log_path = join(dirname(__file__), 'monitoring.log')

ID = os.environ.get("ID")
PASS = os.environ.get("PASS")
URL = os.environ.get("URL")
discord = Discord(url=URL)

logger = logging.getLogger('monitoring')
logger.setLevel(logging.DEBUG)
today = datetime.now()
fh = logging.FileHandler(log_path)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

opts = Options()
opts.add_argument("--headless")

delay = 10
def waitforload(wait_id):
  try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, wait_id)))
  except TimeoutException:
    print("Loading took too much time!")

driver = Firefox(options=opts)

wait = WebDriverWait(driver, 10)

print('Running...')

#discord.post(content='Running...')

driver.get('https://osis.kingston.ac.uk')

focused_window = driver.current_window_handle

assert len(driver.window_handles) == 1

driver.get('https://osis.kingston.ac.uk')

waitforload('MUA_CODE.DUMMY.MENSYS')

id_box = driver.find_element("id", "MUA_CODE.DUMMY.MENSYS")
id_box.send_keys(ID)

pass_box = driver.find_element("id", "PASSWORD.DUMMY.MENSYS")
pass_box.send_keys(PASS)


login_button = driver.find_element("name", "BP101.DUMMY_B.MENSYS")
login_button.click()

print('Logged in...')

try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.LINK_TEXT, "Click HERE to Access Accommodation Portal")))
except TimeoutException:
    print("Loading took too much time!")

link = driver.find_element(By.LINK_TEXT, "Click HERE to Access Accommodation Portal")
link.click()

print('Accommodation site open...')

wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
    if window_handle != focused_window:
        driver.close()
        driver.switch_to.window(window_handle)
        break

waitforload("div-X9c2a6828b2f849d0aaa5b6301587f37f")
time.sleep(2)

focused_window = driver.current_window_handle

book_button = driver.find_element("id", "div-X9c2a6828b2f849d0aaa5b6301587f37f")
book_button.click()
time.sleep(2)

print('In Booking portal...')

#wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
    if window_handle != focused_window:
        driver.close()
        driver.switch_to.window(window_handle)
        break
    
waitforload("div-NavButtonNext")
time.sleep(2)

focused_window = driver.current_window_handle

next = driver.find_element("id", "div-NavButtonNext")
next.click()

print('Next...')

waitforload("div-NavButtonNext")
time.sleep(2)

next = driver.find_element("id", "div-NavButtonNext")
next.click()

print('Next...')

waitforload("div-NavButtonNext")
time.sleep(2)

next = driver.find_element("id", "div-NavButtonNext")
next.click()

print('Next...')

waitforload("div-NavButtonNext")
time.sleep(2)

next = driver.find_element("id", "div-NavButtonNext")
next.click()

print('Next...')

waitforload("div-NavButtonNext")
time.sleep(2)

next = driver.find_element("id", "div-NavButtonNext")
next.click()

print('Next...')

waitforload("div-NavButtonFinish")
time.sleep(2)

finish = driver.find_element("id", "div-NavButtonFinish")
finish.click()

print('Through... Sleeping...')

time.sleep(15)

body = driver.find_element(By.TAG_NAME, 'body')

try:
  check = driver.find_element(By.ID, 'sX4e5110377edb43cfbd490fcfee60ccda')

  if 'No Access' in check.text:
    logger.info('Sjekket : ' + today.strftime("%H:%M %d.%m.%Y")) 
    print(check.text)

  else:
    discord.post(content='Ledig! Book!')
    print('Ledig! Book!')
    logger.info('ledig! ' + today.strftime("%H:%M %d.%m.%Y"))
        
except Exception as e:
  logger.info('Error on ' + today.strftime("%H:%M %d.%m.%Y") + ': ' + e.text)

driver.close()

exit()



