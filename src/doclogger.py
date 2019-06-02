import mysqlx
from rutils import pdf2str, rcat
from sqlalchemy.types import TEXT, VARCHAR, BOOLEAN, INT
import os
import settings
import pandas as pd
from sqlalchemy import create_engine, text
import concurrent.futures
import threading
import time


def init():
    qry = text(
        "SELECT * FROM vTextDocStore WHERE NOT logged and Extension in :extensions")


engine = create_engine(settings.CONN_STR)
df = pd.read_sql_query(qry, con=engine, params={"extensions": ['PDF']})


def get_text(pdfpath):
    y = pdf2str(pdfpath)
    return y


engine = create_engine(
    'mysql+cymysql://rstudio@localhost:3306/email?charset=utf8mb4')


def store_all_docs(df):
    for x, y in df.iterrows():
        try:
            flattext = get_text(y.PhysicalFileName)
            df.at[x, 'Text'] = flatpdf
        except:
            print(x, y.AttachmentID)


# NEW TEXT 3 has all the text,
# can only append table with medium / large text
cn = engine.raw_connect()
cn = engine.connection()
conn = cn.connection
df.to_pickle('txtstoredf', compression='infer')
print('\n'*100)
df.to_sql('nt3', con=engine, if_exists='append')
df.columns
sma = {'PhysicalFileName': VARCHAR, 'Logged': BOOLEAN, 'Translated': BOOLEAN, 'Domain': VARCHAR, 'Extension': VARCHAR,
       'AttachmentID': INT, 'Text': TEXT}
# get text type docs  pdfs into the database
# select all the docs that haven't been translated
#   DATA FRAME
#           AttID, FilePath E (TextType File, ^Stored)
#           Read2Text, Store
#
# open them
# regex strip
#
