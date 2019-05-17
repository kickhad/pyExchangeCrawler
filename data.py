from sqlalchemy import create_engine


def getEngine(str, dbecho=False):
    engine = create_engine(
        str, echo=dbecho)
    return engine
