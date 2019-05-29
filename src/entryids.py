import session as s

import timeit
from settings import DAYS_TO_CACHE
import pandas as pd
from data import GetQuery
from sqlalchemy import create_engine
import datetime
import pytz


def GetOutlookEntryIds(session, ofolder, recur=False, debug=False):
    print('\n\t', ': Scanning ', ofolder.name,
          ' selecting past ', DAYS_TO_CACHE, ' days')
    if ofolder.items.count > 0:
        print('\t\t', ofolder.items.count, 'items to scan')
        start = timeit.default_timer()

        storeid = ""
        for x in ofolder.items:
            if not storeid:
                storeid = x.parent.storeid

            # gooddate = False
            # try:
            #     tdelta = datetime.datetime.now(pytz.utc) - x.ReceivedTime
            #     if tdelta.days < DAYS_TO_CACHE:
            #         gooddate = True
            # except:
            #     pass

            if x.messageclass == 'IPM.Note':
                session.EntryIdsList.append(x.entryid)
                session.StoreIdsList.append(storeid)
                session.AttCountList.append(x.attachments.count)
            elif x.messageclass != 'IPM.Note':
                print('\n\t\t', x.messageclass)

        if recur:
            if ofolder.folders.count > 0:
                for y in ofolder.folders:
                    print('Recursing', y.folderpath)
                    GetOutlookEntryIds(session, y)


# def setdiff(session):
#
#     dfOutlookEntryId = pd.DataFrame(session.EntryIdsList)
#     dfDataBaseEntryIdSeries = GetQuery(
#         "SELECT EntryID, StoreID, 0 FROM email_final.lu_entry_id;")
#     # a is larger set
#     # c = a[~a.isin(b).all(1)]
#     c = dfOutlookEntryId[~dfOutlookEntryId.isin(
#         dfDataBaseEntryIdSeries).all(1)]
#     c.columns = ['EntryID', 'StoreID', 'AttCount']
#     #c.to_sql('netids', engine, if_exists='replace')
#     return c
