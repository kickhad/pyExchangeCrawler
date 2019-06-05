import concurrent.futures  # import ProcessPoolExecutor, as_completed
import pickle
import threading
import time


import pandas as pd
from google.cloud import translate
from sqlalchemy import create_engine, text
from tqdm import tqdm

#import signal
#from collections import OrderedDict


thread_local = threading.local()
errs =[]
def get_translator():
    if not hasattr(thread_local, "tc"):
        thread_local.tc = translate.Client()
    # if not hasattr(thread_local, "translator"):
    #    thread_local.translator = Translator()
    return thread_local.tc


def get_trans(row):
    idx = row.AttID
    tr = get_translator()
    try:
        td = tr.translate(row.Text, target_language='en')
        df3.at[idx, 'Text'] = td['translatedText']
    except Exception as inst:
        errs.append(row.AttID)


def get_data():
    qry = text(
        "SELECT BodyID as AttID, Body as Text from bodys"
        #"SELECT AttachmentID, Text FROM nt3 WHERE TEXT is NOT NULL AND TEXT !=''"
        )
    engine = create_engine('mysql+cymysql://rstudio@localhost:3306/email?charset=utf8mb4')
    df = pd.read_sql_query(qry, con=engine)
    for x, y in df.iterrows():
        try:
            df.at[x, 'Text'] = y.Text.replace('\r\n', ' NEWROW ')
        except:
            print(x, ' error')
            df.at[x, 'Text'] = ''
    return df


def clean_data(df):
    for x, y in df.iterrows():
        txt = y.Text
        df.at[x, 'Text'] = y.Text.replace(' NEWROW ', '\r\n')


def trans(df):
    futures_list = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:    
        for x, y  in df.iterrows():
            futures_list += [executor.submit(get_trans, y)]       
        for f in tqdm(concurrent.futures.as_completed(futures_list), total=len(futures_list)):
            f.result()
    
        
        
        
        #pbar = tqdm(total=(len(df)+2), ascii=True)
        tqdm_parallel_map(executor, get_trans, df.itertuples())
        # future_to_tup = {executor.submit(get_trans, x): x for x in df.itertuples()}
        # for future in concurrent.futures.as_completed(future_to_tup):
        #     y = lqdm(future_to_tup[future], total=(len(df)+1). ascii=True)
        #     future.result()
            
            
    return df3
def tqdm_parallel_map(executor, fn, *iterables, **kwargs):
    """
    Equivalent to executor.map(fn, *iterables),
    but displays a tqdm-based progress bar.
    
    Does not support timeout or chunksize as executor.submit is used internally
    
    **kwargs is passed to tqdm.
    """
    futures_list = []
    for iterable in iterables:
        futures_list += [executor.submit(fn, i) for i in iterable]
    for f in tqdm(concurrent.futures.as_completed(futures_list), total=len(futures_list), **kwargs):
        yield f.result()

def get_test_data():
    lnum = list(range(0, 12))
    ltup = (
        'émarrer une entreprise, permis, propriété intellectuelle, soutien aux entreprises, vendre au gouvernement',
        'Assurance emploi, congés familiaux et congés de maladie, pensions, logement, aide financière aux études, personnes invalides',
        'Alimentation, nutrition, maladies, vaccins, médicaments, sécurité des produits et rappels',
        'Impôt sur le revenu, TPS/TVH, limites de contribution, credits d’impôt, organismes de charité ',
        'Environnement et ressources naturelles', 'Météo, climat, agriculture, faune, pollution, conservation, pêches',
        'Sécurité nationale et défense',
        'Militaire, cybersécurité, sûreté des transports, sécuriser la frontière, contre-terrorisme',
        'Culture, histoire et sport',
        'Arts, médias, patrimoine, langues officielles, identité nationale et financement',
        'Services de police, justice et urgences',
        "Sécurité, justice, se préparer en cas d'urgence, services aux victimes d'actes criminels")
    df = pd.DataFrame({
        "Text": ltup
    }, index=lnum)
    return df


# if __name__ == "__main__":
df = get_data()
errs = []
AttID= []
df3 = pd.DataFrame({"Text": []}, index=AttID)
trans(df)
clean_data(df3)


# try:
#     engine = create_engine('mysql+cymysql://rstudio@localhost:3306/email?charset=utf8mb4')
#     df3.to_sql('bodytrans', con=engine, if_exists='replace')
#     print('indb')
# except:
#     with open('errpickle.pck', 'wb') as fn:
#         pickle.dump(df3, fn)
#     print("Err")
