import os
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
qry = text(r"SELECT PhysicalFileName, AttachmentID, Notes  FROM attachments WHERE left(extension, 2)= 'XL' and Notes is null")
conn = engine.connect()

df = pd.read_sql(qry, params={"domain": 'METRO',"excludeexts": "MSG"}, con=engine)
# is_xl = df.Extension.isin(['XLSX', 'XLSM', 'XLSB', 'XLS'])
# df_xl = df[is_xl]
# print(df_xl)
for a in df_xl.itertuples():
    fn = PureWindowsPath(a.PhysicalFileName.replace('/', '\\'))
    wb = xl.Workbooks.Open(Filename=fn, ReadOnly=True)
    x = input('Describe wb : \t')
    try:
        wb.Close()
    except:
        pass
    if x == 'q':
        break
    df.at[a.Index, 'Notes'] = x
conn = engine.connect()
conn.execute('INSERT INTO attachments (AttachmentID, Notes)SELECT * FROM (SELECT AttachmentID, Notes Nots FROM notes) s ON DUPLICATE KEY  UPDATE  Notes = Nots')
df.to_sql('notes', con=engine, if_exists='replace')
conn.execute('INSERT INTO attachments (AttachmentID, Notes)SELECT * FROM (SELECT AttachmentID, Notes Nots FROM notes) s ON DUPLICATE KEY  UPDATE  Notes = Nots')
