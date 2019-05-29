from sqlalchemy import create_engine, engine
import cymysql
from settings import CONN_STR
import pandas as pd


def getEngine(str=CONN_STR, dbecho=False):
    engine = create_engine(str, echo=dbecho)
    return engine


# def getEngine(str=s.DB_PROD, dbecho=bool(s.DEBUG)):
#     engine = create_engine(
#         str, echo=dbecho)
#     return engine


engine = getEngine()
tmpengine = getEngine()


def GetQuery(str):
    cn = engine.raw_connection()
    try:
        cur = cn.cursor()
        df = pd.read_sql_query(str, cn)
    finally:
        try:
            df
        except:
            df = pd.DataFrame()
        cur.close
        cn.commit()
        cn.close()
    return df
