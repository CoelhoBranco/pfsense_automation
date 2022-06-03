from dotenv import dotenv_values
from model.pfsense import *

config = dotenv_values()

interation = Interation()
interation.click_advanced()

pfsense = PFSense()
pfsense.skip_certificate()
pfsense.login(config['username'], config['password'])   
time.sleep(10)
pfsense.driver.close()

pfsense = Pfsense('Mapeamento_Instrumentacao')
pfsense.login(
    config['username'], config['password']
    )
pfsense.select_dhcp_server()
pfsense.register_data()