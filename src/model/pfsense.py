import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from Bromo.bromo import Bromo


class PFSense:
    
    def __init__(self):
        service = Service(ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        self.bromo = Bromo(self.driver)
        self.driver.get("https://fw.nidf.ufrj.br/")
        
        self.driver.maximize_window()
        
    def login(self, username, password):
        self.setUser(username)
        self.setPassword(password)
        self.sign_in()
    
    
    def select_dhcp_server(self):
        self.select_service()
        self.select_dhcp_server()
        self.add_button_dhcp()
       
        
    def skip_certificate(self, time = 10):
        self.bromo.located("proceed-link", time, "id")
        self.driver.execute_script('document.querySelector("#proceed-link").click()')
        return True
     
        
    def input_field(self, field, value):
        self.bromo.write(field, value)
    
        pass
    
    
    def setUser(self, username):
        self.user = username
        self.bromo.write('//*[@id="usernamefld"]', username)


    def setPassword(self, password):
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
    pfsense = PFSense()
    pfsense.skip_certificate()     
    pfsense.setUser()
    pfsense.setPassword()
    pfsense.sign_in()
    time.sleep(10)
    pfsense.driver.close()
        
    
    
    
