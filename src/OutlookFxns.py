import sys
import pandas as pd
import datetime
import pytz
import os


def MessageExtract(session):
    print('\t\t', 'Extracting Messages ...')
    msgs = session.dfMsgs()

    for ids in session.dfEntrys.itertuples():
        x = session.Outlook.GetItemFromID(ids.EntryID, ids.StoreID)
        print(x.Subject)
        idx = ids.Index
        msgs.loc[idx, 'OutlookFolder'] = x.parent.FolderPath
        msgs.loc[idx, 'Subject'] = x.Subject
        msgs.loc[idx, 'Received'] = str(x.ReceivedTime)
        if x.SenderEmailType == 'EX':
            msgs.loc[idx, 'EMailFrom'] = x.SenderName
        else:
            msgs.loc[idx, 'EMailFrom'] = x.SenderEmailAddress
            msgs.loc[idx, 'Body'] = x.body
            msgs.loc[idx, 'AttCount'] = x.attachments.count
            msgs.loc[idx, 'ConversationID'] = x.ConversationID
            msgs.loc[idx, 'ConversationIndex'] = x.ConversationIndex
    return msgs


def AttachmentExtract(session):
    print('\n\t\t', 'Extracting Attachments ...')
    df_filtered = session.dfMsgs
    atts_fns = list()
    atts_fnexts = list()
    atts_newfns = list()
    atts_size = list()
    atts_olid = list()
    atts_idx = list()
    fails = []
    for ids in df_filtered.itertuples():
        try:
            x = session.Outlook.GetItemFromID(ids.EntryID)  # , ids.StoreID)
            print(x.Subject == ids.Subject)
            OutlookID = ids.OutlookID
            for y in x.attachments:
                # If not an embeded ole attachment
                try:
                    fn = os.path.splitext(y.FileName)
                except:
                    continue

            new_fn = session.Path + \
                fn[0] + str(OutlookID) + \
                "---" + str(y.index) + '--' + fn[1]
            y.SaveAsFile(new_fn)

            atts_fns.append(fn[0])
            atts_fnexts.append(fn[1].upper().replace('.', ''))
            atts_newfns.append(new_fn)
            atts_size.append(y.Size)
            atts_olid.append(OutlookID)
            atts_idx.append(y.index)
        except:
            print(ids.OutlookID, ' failed')
            fails.append([ids.EntryID, ids.StoreID])

    try:
        df = pd.DataFrame({
            'Filename': atts_fns,
            'Extension': atts_fnexts,
            'StoredFilename': atts_newfns,
            'Size': atts_size,
            'OutlookID': atts_olid
        })

        return df
    except:
        print('Couldnt write to DB')
    print(fails)
