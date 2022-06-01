
import os 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


import time
import pyautogui
import cv2

from Bromo.bromo import Bromo
from selenium.webdriver.common.by import By



class Interation:
    
    def __init__(self):

        service = Service(ChromeDriverManager(log_level=0).install())

        options = Options()
        options.add_argument(
                    f'user-data-dir={os.getcwd()}/Profile 1')
        #service = Service(executable_path='chromeself.driver.exe')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.bromo = Bromo(self.driver)
        self.driver.get("https://casino.sportingbet.com/pt-br/games")


    def verificar_login(self):
        xpath_entrar ='/html/body/vn-app/vn-dynamic-layout-single-slot[2]/vn-responsive-header/header/nav/vn-header-section[2]/vn-h-button[1]/vn-menu-item/a/span'
        try:
            self.bromo.located(xpath_entrar, 5)
            return True
        except Exception as e:
            print(e)
            os.system('cls')
            print('login ja efetuado')
            return False
    
    
    def login(self, email = 'leandro2703palmeira@gmail.com', senha = 'Lps27031981'):
        try:
            click_entrar_js = 'document.querySelector("body > vn-app > vn-dynamic-layout-single-slot.slot.slot-single.slot-header > vn-responsive-header > header > nav > vn-header-section.navbar-wrapper-right > vn-h-button:nth-child(2) > vn-menu-item > a").click()'
            time.sleep(3)
            self.driver.execute_script(click_entrar_js)
    
            self.bromo.write('userId', email, method='id')
            
            senha_caixa_xpath = '//*[@id="password"]/input'
            time.sleep(3)
            self.bromo.write(senha_caixa_xpath, senha)
    
            time.sleep(3)
            entrar_xpath = '//*[@id="login"]/form/fieldset/section/div/button'

            entrar_js = 'document.querySelector("#login > form > fieldset > section > div > button").click()'
            #self.bromo.click(entrar_xpath)
            self.driver.execute_script(entrar_js)
        
        except Exception as e:
            print(e)
            print('erro no login')    
        
        
    def clicar_roleta(self):
        sala_click_js = 'document.querySelector("#gameIdentifier_homemostpopular_LiveDealerRoletaBrasil > div > div > a > cc-image-loader > div > img").click()'
        time.sleep(3)
        self.driver.execute_script(sala_click_js)
        
    
    def get_iframe(self, seletor, method = 'id'):
        
            time.sleep(10)
            if method == 'id':
                by = By.ID
            elif method == 'xpath':
                by = By.XPATH

            self.bromo.located(seletor,time = 30,  method=method)
            iframe_path = self.driver.find_element(by, seletor)
            self.driver.switch_to.frame(iframe_path)  

            return True
        
         
            
    def achar_numeros(self):
        numeros_html = self.outerHTML('//*[@id="root"]/div[2]/div/div/div[7]/div/div[2]/div/div/div[4]')
        return numeros_html
    
    
    def get_banking(self):
        xpath_banking = '//*[@id="root"]/div[2]/div/div/div[9]/div[3]'
        banking_html = self.outerHTML(xpath_banking)
        return banking_html
        
        
    
    
    def outerHTML(self, xpath):
        try:  
            self.bromo.located(xpath, 20)
            html = self.driver.find_element(
                    By.XPATH, xpath).get_attribute('outerHTML')
            return html
                
        except Exception as e:
            print('\n\n\n\nnao achou os numeros')
            print(e)
                
            return False
        
    
    
    def click_bet(self, option, confidence=0.7):
        x, y =pyautogui.locateCenterOnScreen(f'img/{option}.png', confidence=float(confidence))
        pyautogui.click(x, y)
        return True
                              
            
    def make_bet(self, option, apostas, confidence=0.7, delay=0.8):
        for _ in range(int(apostas)):
            self.click_bet(option, confidence)
            time.sleep(float(delay))
        

    def verify_bet(self):
        initial_numbers = self.achar_numeros()
        pass
        
        


if __name__ == '__main__':
    interation = Interation()
    interation.click_bet("even")
    
    '''
    interation = Interation()
    if interation.verificar_login() == True:
            print('vai fazer login')
            interation.login('coelhoembaixadormagico@gmail.com','Aulabot1')
    
    interation.clicar_roleta()
    interation.get_iframe('embedGameIframe')
    interation.get_iframe('vendor-LiveDealerRoletaBrasil')
    interation.bet_value_js()
    interation.bet_value_js()
    print('o menos foi')
    pass
    #time.sleep(15)


'''
    #os.system('cls')
    # 1: fechar o popup
    input('sair')
    #login()
