#usar para tr    def register_data(self):
import pandas as pd
class Excel:
    
    def __init__(self, table_name):
        self.table_name = table_name
        
        #tirar daqui
        self.data = pd.read_excel(f'{table_name}.xlsx')
        self.config = dotenv_values()
    
    def registrar_data():
        for i, ip in enumerate(self.df['IP']):
            try:
                if self.df.loc[i ,'Cadastrado'] == 'OK' or  self.df.loc[i ,'Cadastrado'] == 'Erro no Cadastro':
                    print(f'IP: {ip} já cadastrado')
                    continue
                
                mac = self.df.loc[i ,'MAC']
                description = self.df.loc[i ,'Descricao']
                id = self.df.loc[i ,'Tag NIDF']

                self.mac(mac)
                self.id_client(id)
                self.description(description)
                self.ip(ip)
                self.save()


                time.sleep(int(self.config['delay']))
                self.add_button_dhcp()

                self.df.loc[i ,'Cadastrado'] = 'OK'
            except Exception as e:
                self.df.loc[i ,'Cadastrado'] = 'Erro no Cadastro'
                print(e)

        self.df.to_excel(f'{self.table_name}.xlsx', index=False )
        
    