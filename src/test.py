# import sys
# import os
# #from tabulate import tabulate
# from session import Sesh
# from folderrecurse import pcur
# import pandas as pd
# from entryids import GetOutlookEntryIds
# # GET OUTLOOK NAMESAPACE
# session = Sesh()
# # pcur(session, session.Outlook.GetDefaultFolder(6), False)
# df1 = pd.DataFrame({'a': [1, 2, 3, 4, 5]})

# for x in df1.itertuples():
#     range(1, x.a)
# df1
# #msgs = session.dfMsgs()

# for ids in session.dfEntrys.itertuples():
#     x = session.Outlook.GetItemFromID(ids.EntryID, ids.StoreID)
#     idx = ids.Index
#     msguuid = ids.EmailUUID
#     msgs.loc[idx, 'OutlookFolder'] = x.parent.FolderPath
#     msgs.loc[idx, 'Subject'] = x.Subject
#     msgs.loc[idx, 'Received'] = str(x.ReceivedTime)
#     if x.SenderEmailType == 'EX':
#         msgs.loc[idx, 'EMailFrom'] = x.SenderName
#     else:
#         msgs.loc[idx, 'EMailFrom'] = x.SenderEmailAddress
#         msgs.loc[idx, 'Body'] = x.body
#         msgs.loc[idx, 'AttCount'] = x.attachments.count
#         msgs.loc[idx, 'ConversationID'] = x.ConversationID
#         msgs.loc[idx, 'ConversationIndex'] = x.ConversationIndex

# # # import sys
# # # import shortuuid
# # # import time
# # # u1 = shortuuid.uuid
# # # u2 = shortuuid.uuid
# # # inuse = []
# # # t0 = time.time()
# # # t1 = time.time()
# # # n = 1000000
# # # for x in range(1, n):
# # #     inuse.append(u1())


# # # t1 = time.time()
# # # newones = inuse.copy()
# # # for y in range(1, 100):
# # #     f = u2()
# # #     if not f in inuse:
# # #         newones.append(f)

# # # tf = time.time()

# # # print('Generate', t1 - t0)
# # # print('Check dupes', tf - t1)
# # # print('Total', tf-t0)
# # # print(len(inuse))
# # # print(len(newones))


# # from uuidstore import uuidlist
# # x = uuidlist()
# # x.CurrentUUID
# # x.Seed(10)
# # x.NextUUID()
# # y = x.NextUUID()
# # y
