import sys
import pandas as pd
import datetime
import pytz
import os


# atts4df = []
# atts_uuid = dict()
# atts_fns = dict()
# atts_fnexts = dict()
# atts_newfns = dict()
# atts_size = dict()
# atts_msguuid = dict()
# folder = dict()
# emailfrom = dict()
# body = dict()
# atts = dict()
# uid = dict()
# subj = dict()
# atts_dict = dict()
# convoId = dict()
# convoIdx = dict()
# entry = dict()
# rxd = dict()


def pcur(session, ofolder, recur=True, debug=False):

    current_folder = ""
    if ofolder.items.count > 0:

        for x in ofolder.items:
            try:
                tdelta = datetime.datetime.now(pytz.utc) - x.ReceivedTime
                if tdelta.days < 366:
                    gooddate = True
            except:
                gooddate = False

            if x.messageclass == 'IPM.Note' and gooddate:
                # for zz in range(10, 15):
                #     x = ofolder.items(1)
                if current_folder != x.Parent.FolderPath:
                    current_folder = x.Parent.FolderPath
                    print("Scanning " + current_folder)
                olduuid = session.msg_uid
                newuuid = session.NextMsgUuid()
                testchangex = session.msg_uid == newuuid
                # print('Pre MsgUUID :', '\t', olduuid, '\n')
                # print('Post MsgUUID :', '\t', session.msg_uid)
                msg_idx = session.msg_idx
                uid[msg_idx] = session.msg_uid
                folder[msg_idx] = x.Parent.FolderPath
                if x.SenderEmailType == 'EX':
                    emailfrom[msg_idx] = x.SenderName
                else:
                    emailfrom[msg_idx] = x.SenderEmailAddress

                body[msg_idx] = x.body
                atts[msg_idx] = x.attachments.count
                convoId[msg_idx] = x.ConversationID
                convoIdx[msg_idx] = x.ConversationIndex
                entry[msg_idx] = x.EntryID
                subj[msg_idx] = x.Subject
                rxd[msg_idx] = str(x.ReceivedTime)

                concat_att = ""
                for y in x.attachments:
                    # If not an embeded ole attachment
                    try:
                        fn = os.path.splitext(y.FileName)
                    except:
                        continue

                    if y.type == 1 and not fn[1] in ['png', 'gif', 'jpg']:
                        olduuid = session.att_uid
                        session.NextAttUuid()
                        # print('Pre AttUUID :', '\t', olduuid, '\n')
                        # print('Post AttUUID :', '\t', session.att_uid)
                        curr_attIdx = session.att_idx
                        concat_att = session.att_uid + " , " + concat_att
                        # print(fn[0])
                        new_fn = session.Path + \
                            fn[0] + session.msg_uid + \
                            "-" + session.att_uid + fn[1]
                        y.SaveAsFile(new_fn)
                        atts_fns[curr_attIdx] = fn[0]
                        atts_fnexts[curr_attIdx] = fn[1]
                        atts_newfns[curr_attIdx] = new_fn
                        atts_size[curr_attIdx] = y.Size
                        atts_msguuid[curr_attIdx] = session.msg_uid
                        atts_uuid[curr_attIdx] = session.att_uid
                    atts_dict[msg_idx] = concat_att
                    concat_att = ""

    if recur:
        if ofolder.folders.count > 0:
            for y in ofolder.folders:
                pcur(session, y)

    if not not folder:
        msgs4df = [folder, emailfrom, body, atts, subj,
                   atts_dict, uid, convoId, convoIdx, entry, rxd]
        atts4df = [atts_uuid, atts_fns, atts_fnexts,
                   atts_newfns, atts_size, atts_msguuid]

        session.AppendDataFrame('msgs', msgs4df)
        session.AppendDataFrame('atts', atts4df)
        loadvars()


def loadvars():
    atts4df = []
    atts_uuid = dict()
    atts_fns = dict()
    atts_fnexts = dict()
    atts_newfns = dict()
    atts_size = dict()
    atts_msguuid = dict()
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


loadvars()
