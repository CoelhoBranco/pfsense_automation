from dotenv import dotenv_values
from main import Pfsense

config = dotenv_values()
pfsense = Pfsense('Mapeamento_Instrumentacao')
pfsense.login(
    config['username'], config['password']
    )
pfsense.select_dhcp_server()
pfsense.register_data()