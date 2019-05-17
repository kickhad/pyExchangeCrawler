import configparser
from sqlalchemy import create_engine

# Load config_file
config = configparser.ConfigParser()
config.read('settings.ini')

# easy access attribs
path = config.['DEFAULT'].['path']
db = config.['DATABASE'].['production']
tmpdb = config.['DATABASE'].['temp']


# config.sections()
# print('Done')
# config['DEFAULT'] = {
# 'PATH' : 'c:/pyext',
# 'DB_FINAL' : 'mysql+mysqlconnector://rstudio@localhost:3306/email_final',
# 'DB_TEMP' : 'mysql+mysqlconnector://rstudio@localhost:3306/tmp'
# }
# with open('settings.ini', 'w') as configfile:
#     config.write(configfile)
