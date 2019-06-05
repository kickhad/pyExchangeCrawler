import pandas as pd
from sqlalchemy import create_engine, text
from yandex_translate import YandexTranslate
import pickle
from tqdm import tqdm

tr = YandexTranslate('trnsl.1.1.20190603T185607Z.d5f8270a6abdda7a.2c1c0d646da6415e2fc567509f94f98fd95a2b24')
            

def get_trans(row):
    idx = row.Index
    tr = get_translator()
    try:
        td = tr.translate(row.Text, 'fr-en') 
        # print(str(td['text']).replace(' ', '')[:20])
        df3.at[idx, 'Text'] = str(td['text'])
    except:
        df3.at[idx,'Text'] = ''
        print('trans err')
    

    # df3[row.Index] = t.text


def get_data():
    qry = text(
        "SELECT AttachmentID, Text FROM nt3 limit 10")
    engine = create_engine(
        'mysql+cymysql://rstudio@localhost:3306/email?charset=utf8mb4')
    df = pd.read_sql_query(qry, con=engine)

    for x, y in df.iterrows():
        try:
            txt = df.at[x, 'Text']
            df.at[x, 'Text'] = txt.replace('\r\n', 'NEWROW')
        except:
            print(x, ' error')
            df.at[x, 'Text'] = ''
    return df
def clean_data(df):
    for x, y in df.iterrows():
        txt = y.Text
        df.at[x, 'Text'] = y.Text.replace('NEWROW', '\r\n')



if __name__ == "__main__":
    df = get_data()

    df3 = pd.DataFrame({"Text": []}, index=AttID)
    pint = 0
    trans(df)
    clean_data(df3)
    try:
        df3.to_sql('tre', con=engine, if_exists='replace')
        print('indb')
    except:
        with open('errpickle.pck', 'wb') as fn:
            pickle.dump(df3, fn)
        print("Err")
