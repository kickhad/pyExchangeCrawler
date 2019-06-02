import session as s

import timeit
from settings import DAYS_TO_CACHE
import pandas as pd
from data import GetQuery
from sqlalchemy import create_engine
import datetime
import pytz


def GetOutlookEntryIds(session, ofolder, recur=True, debug=False):
    print('\t', ofolder.name, ofolder.items.count, 'items to scan.',
          '\n', len(session.EntryIdsList), ' items selected.', '\r\n')
    # ' selecting past ', DAYS_TO_CACHE, ' days')
    if ofolder.items.count > 0:
        start = timeit.default_timer()

        storeid = ""
        for x in ofolder.items:
            pass
            if not storeid:
                storeid = x.parent.storeid

            if x.messageclass == 'IPM.Note':
                session.EntryIdsList.append(x.entryid)
                session.StoreIdsList.append(storeid)
                session.AttCountList.append(x.attachments.count)
        if recur:
            if ofolder.folders.count > 0:
                for y in ofolder.folders:
                    #print('Recursing', y.folderpath)
                    next_fld = session.Outlook.GetFolderFromID(
                        y.EntryID, y.StoreID)
                    GetOutlookEntryIds(session, next_fld)


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
