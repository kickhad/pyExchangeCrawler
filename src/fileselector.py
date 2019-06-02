import os
import sys
import win32com
from win32com import universal
from win32com.client import constants
from win32com.server.exception import COMException
from win32com.client import gencache, DispatchWithEvents
import winerror
from pathlib import Path, PureWindowsPath
#import string
#import msvcrt as m
import pandas as pd
import settings
import session
from data import getEngine
from sqlalchemy import text
#xl = win32com.client.Dispatch("Excel.Application")
xl = gencache.EnsureDispatch("Excel.Application")
engine = getEngine()
qry = text(r"SELECT * from vfileselector where domain = :domain")
conn = engine.connect()

df = pd.read_sql(qry, params={"domain": 'LOBLAW',
                              "excludeexts": "MSG"}, con=engine)
is_xl = df.Extension.isin(['XLSX', 'XLSM', 'XLSB', 'XLS'])
is_pdf = df.Extension.isin(['PDF'])
df_xl = df[is_xl]
df_pdf = df[is_pdf]
# print(df_xl)

def xlloop(df):
    xl.Visible = True

    for a in df.itertuples():
        fn = PureWindowsPath(a.PhysicalFileName.replace('/', '\\'))
        try:
            wb = xl.Workbooks.Open(Filename=fn, ReadOnly=True)
            x = input('Describe wb : \t')
        except:
            x = 'Fail'
        try:
            wb.Close(SaveChanges=False)
        except:
            pass
        if x == 'q':
            break
        df.at[a.Index, 'Notes'] = x
        with open('tmp.csv', 'w') as temp:
            df.to_csv(path_or_buf=temp)

def pdfloop(df):
    for a in df.itertuples():
        fn = PureWindowsPath(a.PhysicalFileName.replace('/', '\\'))
        

    conn = engine.connect()
    conn.execute('INSERT INTO attachments (AttachmentID, Notes)SELECT * FROM (SELECT AttachmentID, Notes Nots FROM notes) s ON DUPLICATE KEY  UPDATE  Notes = Nots')
    df.to_sql('notes', con=engine, if_exists='replace')
    conn.execute('INSERT INTO attachments (AttachmentID, Notes)SELECT * FROM (SELECT AttachmentID, Notes Nots FROM notes) s ON DUPLICATE KEY  UPDATE  Notes = Nots')
attid=[]
txt0=[]
txt1=[]
txt2=[]

for x in df.itertuples():
    attid.append(x.AttachmentID)
    txt = x.Text
    try:
        if np.isnan(txt):
            txt0.append('')
            txt1.append('')
            txt2.append('')
    except:
        txt0.append(txt[:65534])
        txt1.append(txt[65535:131069])
        txt2.append(txt[131070:])

df3.to_sql('splitt', con=engine)
dfcrc = pd.read_sql_table('splitt', con=engine)

fa = []
fb = []
for x in dfcrc.itertuples():
    a = x.T0 + x.T1 + x.T2
    b = df.at[x.Index, 'Text']   
    
    fa.append(a)
    fb.append(b)
dffails = pd.DataFrame({"Conc" : fa, "Source" :fb})
len(fa)
z=0
for x, y in dfnan.iterrows():
    try:
        np.isnan(y.Text)
        df.at[x, 'Text'] = ''
        
    except:
        pass
print(z)
df.to_sql('nt', con=engine)