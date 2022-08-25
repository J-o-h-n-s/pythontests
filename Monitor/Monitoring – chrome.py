import logging
import time
import os
from os.path import join, dirname
from datetime import datetime
from selenium import webdriver
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

delay = 10
def waitforload(wait_id):
  try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, wait_id)))
  except TimeoutException:
    print("Loading took too much time!")
    logger.info('Error on ' + today.strftime("%H:%M %d.%m.%Y") + " Loading took too much time!")

driver = webdriver.Chrome()

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
    newdelay = 15
    myElem = WebDriverWait(driver, newdelay).until(EC.presence_of_element_located((By.LINK_TEXT, "Click HERE to Access Accommodation Portal")))
except TimeoutException:
    print("Loading took too much time!")
    logger.info('Error on ' + today.strftime("%H:%M %d.%m.%Y") + " Loading took too much time!")

link = driver.find_element(By.LINK_TEXT, "Click HERE to Access Accommodation Portal")
link.click()

wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
    if window_handle != focused_window:
        driver.close()
        driver.switch_to.window(window_handle)
        break

waitforload("div-X9c2a6828b2f849d0aaa5b6301587f37f")
time.sleep(2)

print('Accommodation site open...')

focused_window = driver.current_window_handle

book_button = driver.find_element("id", "div-X9c2a6828b2f849d0aaa5b6301587f37f")
book_button.click()
time.sleep(2)

print('In Booking portal...')

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
  body = driver.find_element(By.TAG_NAME, 'body')

  if 'No Access' in body.text:
    logger.info('Sjekket : ' + today.strftime("%H:%M %d.%m.%Y") + ' - ' + body.text) 
    print(body.text)
    driver.close()

  else:
    boook = driver.find_element(By.ID, 'div-NavButtonNext')
    boook.click()
    try:
      newbody = driver.find_element(By.TAG_NAME, 'body')

      if 'There are no rooms available for you for this process.' in newbody.text:
        logger.info('Sjekket : ' + today.strftime("%H:%M %d.%m.%Y")) 
        print(body.text)
        driver.close()

      else:
            discord.post(content='Ledig! Book! @here '+ today.strftime("%H:%M %d.%m.%Y"))
            print('Ledig! Book!')
            logger.info('ledig! ' + today.strftime("%H:%M %d.%m.%Y"))
            driver.close()

    except Exception as e:
      logger.info('Error on ' + today.strftime("%H:%M %d.%m.%Y") + ': ' + e.text)
      discord.post(content='Error while running script @ ' + today.strftime("%H:%M %d.%m.%Y") + ' Error has been logged')
      driver.close()

except Exception as e:
  logger.info('Error on ' + today.strftime("%H:%M %d.%m.%Y") + ': ' + e.text)
  discord.post(content='Error while running script @ ' + today.strftime("%H:%M %d.%m.%Y") + ' Error has been logged')
  driver.close()

exit()




