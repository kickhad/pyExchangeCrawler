from sqlalchemy import engine, text
from data import engine, GetQuery
import pandas as pd
import sys
import os
from shutil import move, copyfile, copy2, copyfileobj
df = GetQuery("call email_attachments_byaddress('');")
df['Moved'] = ''
df['NewPath'] = ''
print(df.columns)
for index, row in df.iterrows():
    file = df['PhysicalFileName'][index]
    srcFolder = os.path.split(file)[0]
    fileName = os.path.split(file)[1]
    destFolder = srcFolder + '/' + '' + '/'
    destPath = destFolder + fileName
    try:
        move(file, destPath)
        df['NewPath'][index] = destPath
    except:
        print("MoveFailed", file, destPath)
        df['Moved'][index] = False

# file = df['PhysicalFileName'][index]
# srcFolder = file[0]
# fileName = file[1]
# destFolder = srcFolder + 'METRO' + '/'
# copyfile()
# #srcFolder = os.path.split(df[row,'PhysicalFileName'])[0]
