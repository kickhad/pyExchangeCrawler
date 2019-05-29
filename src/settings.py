import configparser

# from sqlalchemy import create_engine

# Load config_file
config = configparser.ConfigParser()
config.read("settings.ini")

# easy access attribs
DEBUG = config["DEFAULT"]["debug"]
PATH = config["DEFAULT"]["path"]
CONN_STR = config["DATABASE"]["production"]
DAYS_TO_CACHE = config["DEFAULT"]["DaysToCache"]
# config.sections()
# print('Done')
# config['DEFAULT'] = {
# 'PATH' : 'c:/pyext',
# 'DB_FINAL' : 'mysql+cymysqlconnector://rstudio@localhost:3306/email_final',
# 'DB_TEMP' : 'mysql+cymysqlconnector://rstudio@localhost:3306/tmp'
# }
# with open('settings.ini', 'w') as configfile:
#     config.write(configfile)
