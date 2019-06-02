import os
import glob
import hashlib
import urllib
import win32com
from win32com import universal
from win32com.client import constants
from win32com.server.exception import COMException
from win32com.client import gencache, DispatchWithEvents
import winerror

from pathlib import Path, PureWindowsPath
import string
import msvcrt as m
import pandas as pd
import sys
from session import Sesh
from data import getEngine
import settings
from sqlalchemy import text
xl = win32com.client.Dispatch("Excel.Application")

engine = getEngine()
qry = text('SELECT * FROM attachments WHERE left(extension, 2)= "XL"')
conn = engine.connect()

df = pd.read_sql(qry, con=engine)
df['MD5'] = ""
fails = []
for a in df.itertuples():
    try:
        fn = a.PhysicalFileName
        with open(fn, 'rb') as getmd5:
            data = getmd5.read()
            gethash = hashlib.sha512(data).hexdigest()
            df.at[a.Index, 'SHA512'] = gethash
    except:
        fails.append(fn)
        print('FAILED: ', fn)

df.to_sql('md5s', con=engine, if_exists='replace')
pd.DataFrame({"Fails": fails}).to_sql(
    'err_md5s', con=engine, if_exists='replace')
