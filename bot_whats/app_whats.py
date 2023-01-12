import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

search_group = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
send_message = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
automatic_message = 'Bom dia veia, isso é um teste de automação com python!'
verde = '\033[1;36;42m'
#windows = webdriver.Chrome()
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(
    r"user-data-dir={}".format(profile))

browser = webdriver.Chrome("./chromedriver.exe", chrome_options=options)

browser.get("https://web.whatsapp.com")
#windows.get("https://web.whatsapp.com/")
pyautogui.sleep(20)

list = ["##############" ]

for grupo in list:
    #windows.find_element(By.XPATH, search_group).send_keys(grupo)
    browser.find_element(By.XPATH, search_group).send_keys(grupo)
    pyautogui.sleep(2)
    pyautogui.press('enter')
    pyautogui.sleep(1)
    #windows.find_element(By.XPATH, send_message).send_keys(automatic_message)
    browser.find_element(By.XPATH, send_message).send_keys(automatic_message)
    pyautogui.sleep(2)
    pyautogui.press('enter')
    pyautogui.sleep(1)
    
print (f'{verde}mensagens enviadas')
    
