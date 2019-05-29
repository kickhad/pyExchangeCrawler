import os
import sys
import glob
import timeit
import getopt
from session import Sesh
from settings import DAYS_TO_CACHE
import shortuuid
from data import getEngine
from scanboxes import ScanBoxes
from OutlookFxns import MessageExtract, AttachmentExtract
import pandas as pd
from entryids import GetOutlookEntryIds
# GET OUTLOOK NAMESAPACE
session = Sesh()

boxes = True
scanboxes = False
attsQuery = ''
xtraxtmsgs = True
fetchatts = True
processmsgfiles = False

if scanboxes:
    ScanBoxes(session)

if xtraxtmsgs:
    engine = getEngine()
    if not scanboxes:
        try:
            session.dfEntrys = pd.read_sql_query(
                'SELECT * FROM newtbl WHERE concat(EntryID, StoreID0, StoreID1) not in (SELECT concat(EntryID, storeid0, storeid1) from  newtbl2', con=engine)
        except:
            session.dfEntrys = pd.read_sql_query(
                'SELECT * FROM newtbl', con=engine)
    msgs = session.dfEntrys
    for x in ['OutlookFolder', 'EMailFrom', 'Body', 'Subject', 'ConversationID', 'ConversationIndex', 'Received']:
        msgs[x] = ""
    session.dfMsgs = msgs.reindex

    msgsfull = MessageExtract(session)
    msgsfull.to_sql('newtbl2', con=engine, if_exists='append')

if fetchatts:
    engine = getEngine()
    qry = 'SELECT OutlookID, EntryID, concat(storeid0, storeid1) as StoreID from outlookids where OutlookID not in (select distinct outlookid from attachments)'
    session.dfMsgs = pd.read_sql_query(qry, con=engine)
    df = AttachmentExtract(session)
    try:
        df.to_sql('msgs', con=engine, if_exists='replace')
    except:
        pass

if processmsgfiles:
    SourceFileName = list()
    PhysicalFileName = list()
    FileExt = list()
    Saved = list()
    MsgFileUUID = list()

    for infile in glob.glob('c:\\pyext\\*.msg'):
        z = session.Outlook.OpenSharedItem(infile)
        if z.attachments.count > 0:
            suuid = shortuuid.uuid()
            MsgFileUUID.append(suuid)
            sourcefn = infile.split('\\')
            for att in z.attachments:
                SourceFileName.append(infile)
                fn = att.filename.split('.')
                fn_end = len(fn) - 1
                fn_name = ''.join(fn[0:fn_end])
                fn_ext = ''.join(fn[fn_end])
                print(fn_name, fn_ext)
                new_fn = session.Path + 'Secondary' + '/' + \
                    fn_name +  \
                    "---" + str(att.index) + '--' + \
                    suuid + '.' + fn_ext
                PhysicalFileName.append(new_fn)

                FileExt.append(fn_ext)
                try:
                    att.SaveAsFile(new_fn)
                    Saved.append(False)
                except:
                    print(att.filename, ' could not be saved from ', infile)
                    print('\t', 'as ', new_fn)
                    Saved.append = False
    df = pd.DataFrame({'SourceFileName': SourceFileName,            'PhysicalFileName': PhysicalFileName,
                       'FileExt': FileExt,            'Success': Saved})
    engine = getEngine()
    df.to_sql('secondaryatts', con=engine, if_exists='replace')

# z = session.Outlook.OpenSharedItem('c:\\pyext\\Détail du paiement le 20180601 - S.C. JOHNSON 3863---1--.msg')
# RECURSE MSG FILES SAVED

path = 'c:\\pyext\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if not 'Secondary' in r:
            if '.msg' in file:
                files.append(os.path.join(r, file))

for f in files:
    print(f)
