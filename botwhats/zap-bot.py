from selenium import webdriver
import time

class Whatsbot:
    def __init__(self):
        self.mensage = "Bom Dia Grupo, como vcs estão?"
        self.grupos = ['Bobões']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
           
    def Enviarmsg(self):
#<span dir="auto" title="Bobões" Bobões</span>
#):<div tabindex="-1" class="p3_M1">
#<span data-testid="send" data-icon="send" class>…</span>
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)
        
        grupo = self.driver.find_element_by_xpath(f"//spam[@title='{grupo}']")
        grupo.click()
        chat_box = self.driver.find_element_by_class_name('p3_M1')
        chat_box.click()
        chat_box.send_keys(self.memsage)
        self.drive.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(3)
        botao_enviar.click()
        tipe.sleep(5)
        
        

bot = Whatsbot()
bot.Enviarmsg





#//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]