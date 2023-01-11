from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui


windows = webdriver.Chrome()
windows.get("https://web.whatsapp.com/")
pyautogui.sleep(20)

list = ["cauã campos LTDA", "GRUPO PARA O TRABALHO" ]

for grupo in list:
    windows.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(grupo)
    pyautogui.sleep(2)
    pyautogui.press('enter')
    pyautogui.sleep(1)
    windows.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys('Não responda, essa é uma mensagem automatica!')
    pyautogui.sleep(1)
    pyautogui.press('enter')
    pyautogui.sleep(1)
    
    