import time
import pandas as pd

from controller import Interation


from dotenv import dotenv_values


"""
Necessary Libarys for run:
selenium
bromo
pandas
time

necessary files:
.env(username, password, time)

"""

class Pfsense:
    
    def __init__(self, table_name):
        self.interation = Interation()
        self.interation.click_advanced()
        
        self.table_name = table_name
        
        self.df = pd.read_excel(f'{table_name}.xlsx')
        self.config = dotenv_values()
                              
    
    def login(self, username, password):
        self.interation.user(username)
        self.interation.password(password)
        self.interation.sign_in()

    
    
    def select_dhcp_server(self):
        self.interation.select_service()
        self.interation.select_dhcp_server()
        self.interation.add_button_dhcp()

    
    def register_data(self):
        for i, ip in enumerate(self.df['IP']):
            try:
                if self.df.loc[i ,'Cadastrado'] == 'OK' or  self.df.loc[i ,'Cadastrado'] == 'Erro no Cadastro':
                    print(f'IP: {ip} já cadastrado')
                    continue
                
                mac = self.df.loc[i ,'MAC']
                description = self.df.loc[i ,'Descricao']
                id = self.df.loc[i ,'Tag NIDF']

                self.interation.mac(mac)
                self.interation.id_client(id)
                self.interation.description(description)
                self.interation.ip(ip)
                self.interation.save()


                time.sleep(int(self.config['delay']))
                self.interation.add_button_dhcp()

                self.df.loc[i ,'Cadastrado'] = 'OK'
            except Exception as e:
                self.df.loc[i ,'Cadastrado'] = 'Erro no Cadastro'
                print(e)

        self.df.to_excel(f'{self.table_name}.xlsx', index=False )
            
          
    
    
    
if __name__ == "__main__":
   
    config = dotenv_values()
    pfsense = Pfsense('Mapeamento_Instrumentacao')
    pfsense.login(
        config['username'], config['password']
        )
    pfsense.select_dhcp_server()
    pfsense.register_data()
    '''
    config = dotenv_values()
    pfsense = Pfsense()
    pfsense.login(
        config['username'], config['password']
        )
    pfsense.select_dhcp_server()
    pfsense.register_data()
    
    
    df = pd.read_csv('Mapeamento_Instrumentacao.csv',sep=';', encoding='latin-1')
    variable = df
    print(variable)'''
    
    
    '''
    df = pd.read_csv('Mapeamento_Instrumentacao.csv',sep=';', encoding='latin-1')
    config = dotenv_values()
    print(type(config['delay']))
   for i, ip in enumerate(df['IP']):
        print(df.loc[i ,'MAC'])
            #print(self.df.loc[i ,'MAC'])
            #self.interation.mac(self.df.loc[i ,'MAC'])        
        pass'''
    #pfsense = Pfsense()
    #pfsense.register_data()
    '''
    config = dotenv_values()
    pfsense = Pfsense()
    pfsense.login(
        config['username'], config['password']
        )
    pfsense.select_dhcp_server()
    time.sleep(30)
    
    
    '''
    
    
    
    
    
    
    
    
    #env = dotenv_values()
    #print(env['user'])
    