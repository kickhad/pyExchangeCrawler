import sys
import pandas as pd
import os


folder = dict()
emailfrom = dict()
body = dict()
atts = dict()
uid = dict()
subj = dict()
atts_dict = dict()
convoId = dict()
convoIdx = dict()
entry = dict()
rxd = dict()
df = pd.DataFrame


def pcur(session, ofolder):

    current_folder = ""
    if ofolder.items.count > 0:
        #msg_idx = session.msg_idx

        for x in ofolder.items:
            if x.messageclass == 'IPM.Note':
                # for zz in range(10, 15):
                #     x = ofolder.items(1)
                if current_folder != x.Parent.FolderPath:
                    current_folder = x.Parent.FolderPath
                    print("Scanning " + current_folder)
                session.msg_idx += 1
                msg_idx = session.msg_idx
                folder[msg_idx] = x.Parent.FolderPath
                if x.SenderEmailType == 'EX':
                    emailfrom[msg_idx] = x.SenderName
                else:
                    emailfrom[msg_idx] = x.SenderEmailAddress

                body[msg_idx] = x.body
                atts[msg_idx] = x.attachments.count
                uid[msg_idx] = session.msg_uid
                convoId[msg_idx] = x.ConversationID
                convoIdx[msg_idx] = x.ConversationIndex
                entry[msg_idx] = x.EntryID
                subj[msg_idx] = x.Subject
                rxd[msg_idx] = str(x.ReceivedTime)

                concat_att = ""
                for y in x.attachments:
                    # If not an embeded ole attachment
                    if y.type == 1:
                        session.att_idx += 1
                        concat_att = session.att_uid + " , " + concat_att
                        fn = os.path.splitext(y.FileName)
                        # print(fn[0])
                        new_fn = session.Path + \
                            fn[0] + session.msg_uid + \
                            "-" + session.att_uid + fn[1]
                        y.SaveAsFile(new_fn)
                    atts_dict[msg_idx] = concat_att

    if ofolder.folders.count > 0:
        for y in ofolder.folders:
            pcur(session, y)
    if not not folder:
        data = [folder, emailfrom, body, atts, subj,
                atts_dict, uid, convoId, convoIdx, entry, rxd]
        session.AppendDataFrame(data)
