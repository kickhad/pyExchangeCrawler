from sqlalchemy import create_engine, engine
import cymysql
import settings as s
import pandas as pd


def getEngine(str=s.DB_PROD, dbecho=bool(s.DEBUG)):
    engine = create_engine(
        str, echo=dbecho)
    return engine


engine = getEngine()
tmpengine = getEngine(s.DB_TEMP)


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
