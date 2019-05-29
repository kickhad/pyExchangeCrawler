import sys
import timeit
import getopt
import os
from session import Sesh
from settings import DAYS_TO_CACHE
import shortuuid
from data import getEngine
from OutlookFxns import MessageExtract, AttachmentExtract
import pandas as pd
from entryids import GetOutlookEntryIds


def ScanBoxes(session):
    for box in session.ol_boxes:
        box_n = session.Outlook.GetFolderFromID(box)
        print("Scanning Box :", box_n.parent.name)
        # try:
        GetOutlookEntryIds(session, box_n.parent)
        GetOutlookEntryIds(session, box_n)
        # except:
        print('oops')
    session.dfEntrys = pd.DataFrame({
        'EntryID': session.EntryIdsList,
        'StoreID': session.StoreIdsList,
        'AttCount': session.AttCountList})

    # nkeys=len(session.dfEntrys.index)
    # lkeys=[]
    # for x in range(0, nkeys):
    # uuid=shortuuid.uuid()
    # lkeys.append(uuid[:8])

    # uqlist=[]
    # for el in lkeys:
    # if el not in uqlist:
    #     uqlist.append(el)

    # while len(uqlist) < nkeys:
    # uuid=shortuuid.uuid()
    # lkeys.append(uuid[:8])
    # if el not in uqlist:
    #     uqlist.append(el)

    allmsgs = session.dfEntrys
    engine = getEngine()
    df1 = pd.read_sql_query('select * from vIds', con=engine)
    msgs = allmsgs[~allmsgs.isin(df1)].dropna()
    #        msgs['EmailUUID']=uqlist
    #msgs['AttCount'] = 0

    msgs.to_sql('newtbl', engine, if_exists='append')

    print('New msgs written')


print("Complete")
