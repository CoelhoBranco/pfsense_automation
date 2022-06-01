import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from Bromo.bromo import Bromo


class Interation:
    
    def __init__(self):
        service = Service(ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        self.bromo = Bromo(self.driver)
        self.driver.get("https://fw.nidf.ufrj.br/")
        
        self.driver.maximize_window()
    
    
    def click_advanced(self):
        self.bromo.click('//*[@id="details-button"]')
        
        self.bromo.click('//*[@id="proceed-link"]')
        
        
    def user(self, username):
        self.bromo.write('//*[@id="usernamefld"]', username)

    
    def password(self, password):
        self.bromo.write('//*[@id="passwordfld"]', password)
    
    
    def sign_in(self):
        self.bromo.click('//*[@id="total"]/div/div[2]/div/form/input[4]')
        
    
    def select_service(self):
        self.bromo.click('//*[@id="pf-navbar"]/ul[1]/li[4]/a')
    
    
    def select_dhcp_server(self):
        self.bromo.click('//*[@id="pf-navbar"]/ul[1]/li[4]/ul/li[13]/a')
        
    
    def add_button_dhcp(self):
        self.bromo.click('//*[@id="2"]/div/nav/a')
    
    def mac(self, address):
        self.bromo.write('//*[@id="mac"]', address)    
    
    
    def id_client(self, id):
        self.bromo.write('//*[@id="cid"]', id)
        
    
    def description(self, description):
        self.bromo.write('//*[@id="descr"]', description)
        
    
    def ip(self, address):
        self.bromo.write('//*[@id="ipaddr"]', address)
    
    def save(self):
        self.bromo.click('//*[@id="save"]')
    
        
if __name__ == '__main__':
    interation = Interation()
    interation.click_advanced()
    
    time.sleep(5)        
    interation.user('qualquermerda')
    time.sleep(60)
    interation.driver.close()
        
    
    
    