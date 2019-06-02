import sys
from settings import CONN_STR, AR_ENTRY_ID, AS_ENTRY_ID, IN_ENTRY_ID
import datetime
import shortuuid
# from entryids import GetOutlookEntryIds, GetDatabaseEntryIds
from data import GetQuery
from sqlalchemy import create_engine
from uuidstore import uuidlist
import pandas as pd
import win32com
import shortuuid
from win32com import universal
from win32com.client import constants
from win32com.server.exception import COMException
from win32com.client import gencache, DispatchWithEvents
import winerror


class Sesh(object):

    def __init__(self):
        self.__engine = create_engine(
            CONN_STR, echo=False)
        # self.__msg_idx = 0
        # self.__att_idx = 0
        # # self.__msg_uids = pd.read_sql(
        #    'SELECT * from `final`.`email_msg_uids` WHERE not MsgUID in (select MsgUID from `final`.`email_msgs`) LIMIT 2000', self.__engine)
        # @self.__att_uids = pd.read_sql(
        #    'SELECT * from `final`.`email_att_uids` WHERE not AttUID in (select AttUID from `final`.`email_atts`) LIMIT 2000', self.__engine)
        # self._dfmsgs = pd.DataFrame(columns=self.__colnames)
        self.__ol_boxes = [AR_ENTRY_ID, AS_ENTRY_ID, IN_ENTRY_ID]
        self.__path = 'c:/pyext/'
        self.__outlook = win32com.client.Dispatch(
            "Outlook.Application").GetNamespace("MAPI")

        self._msgscolnames = ['OutlookFolder', 'EMailFrom', 'Body', 'AttCount',
                              'Subject', 'EmailUID', 'ConversationID', 'ConversationIndex', 'Received']
        self._attscolnames = ['Filename', 'Extension',
                              'StoredFilename', 'Size', 'MsgUUID', 'AttsIdx']
        # self.__attuids = uuidlist()
        # self.__attuids.NextUUID()
        # self.__msguuids = uuidlist()
        # self.__msguuids.NextUUID()
        self.__dfatts = pd.DataFrame()
        self.__dfMsgs = pd.DataFrame()
        self.__entryIdsList = list()
        self.__storeIdsList = list()
        self.__AttCountList = list()
        self.__dfEntrys = pd.DataFrame()

    def __get_dfEntrys(self):
        """
        :type: DataFrame
        """
        return self.__dfEntrys

    def __set_dfEntrys(self, value):
        """
        :type: DataFrame
        """
        self.__dfEntrys = value
    dfEntrys = property(__get_dfEntrys, __set_dfEntrys)

    # def __get_dfMsgs(self):
    #     """
    #     :type: DataFrame
    #     """
    #     return self.__dfMsgs

    # def __set_dfMsgs(self, value):
    #     """
    #     :type: DataFrame
    #     """
    #     self.__dfMsgs = value
    # dfMsgs = property(__get_dfMsgs, __set_dfMsgs)

    def __get_AttCountList(self):
        """
        :type: list
        """
        return self.__AttCountList

    def __set_AttCountList(self, value):
        """
        :type: list
        """
        return self.__AttCountList
    AttCountList = property(__get_AttCountList, __set_AttCountList)

    def __get_storeIdsList(self):
        """
        :type: list
        """
        return self.__storeIdsList

    def __set_storeIdsList(self, value):
        """
        :type: list
        """
        return self.__storeIdsList
    StoreIdsList = property(__get_storeIdsList, __set_storeIdsList)

    @property
    def Engine(self):
        """
        :type: Engine
        """
        return self.__engine

    def __get_EntryIdsList(self):
        """
        :type: list
        """
        return self.__entryIdsList

    def __set_EntryIdsList(self, value):
        """
        :type: List
        """
        self.__entryIdsList = value
    EntryIdsList = property(__get_EntryIdsList, __set_EntryIdsList)

    # def AppendDataFrame(self, target, df, debug=False):
    #     df1 = pd.DataFrame(df)
    #     colnames = ""
    #     if target == 'msgs':
    #         colnames = self._msgscolnames
    #     elif target == 'atts':
    #         colnames = self._attscolnames

    #     dft = pd.DataFrame(columns=colnames)
    #     dft = df1.T
    #     tblid = ""
    #     replacetable = 'append'
    #     if debug:
    #         tblid = datetime.datetime.now().strftime("_%j_%H%M")
    #         replacetable = 'replace'
    #     tblname = str(target+tblid)
    #     #dft.columns = colnames
    #     dft.to_sql(tblname, con=self.__engine,
    #                if_exists=replacetable, index=False)
    #     print(target, 'table written as', tblname)

    @property
    def dfMsgs(self):
        """
        :type: DataFrame
        """
        return self.__dfMsgs

    @dfMsgs.setter
    def dfMsgs(self, value):
        """
        :type: DataFrame
        """
        self.__dfMsgs = value

    @property
    def dfAtts(self):
        """
        :type: DataFrame
        """
        return self.__dfatts

    @property
    def Outlook(self):
        """
        :type: object
        """
        return self.__outlook

    @property
    def Path(self):
        """
        :type: string
        """
        return self.__path

    @property
    def ol_boxes(self):
        """
        :type: list
        """
        return self.__ol_boxes

    # @property
    # def att_uid(self):
    #     """
    #     :type: string
    #     """
    #     return self.__attuids.CurrentUUID

    # @property
    # def msg_uid(self):
    #     """
    #     :type: string
    #     """
    #     return self.__msguuids.CurrentUUID

    # def NextMsgUuid(self):
    #     """
    #     :type: string
    #     """
    #     self.__msg_idx += 1
    #     y = self.__msguuids.NextUUID()
    #     return y

    # def NextAttUuid(self):
    #     """
    #     :type: string
    #     """
    #     self.__att_idx += 1
    #     y = self.__attuids.NextUUID()
    #     return y

    def is_empty(self, tup):
        y = False
        for x in tup:
            y = not x or y
            if y:
                return y
        return y

    # def __get_msg_idx(self):
    #     """
    #     :type: int
    #     """
    #     return self.__msg_idx

    # def __set_msg_idx(self, value):
    #     """
    #     :type: int
    #     """
    #     self.__msg_idx = value

    # def __get_att_idx(self):
    #     """
    #     :type: int
    #     """
    #     return self.__att_idx

    # def __set_att_idx(self, value):
    #     """
    #     :type: int
    #     """
    #     self.__att_idx = value

    # msg_idx = property(__get_msg_idx, __set_msg_idx)
    # att_idx = property(__get_att_idx, __set_att_idx)

    # @property
    # def LoggedEntryIds(self)
    # """
    # :type: Series
    # """
    # return __loggedEntryIds

    # def WrtieToDB(self):
    #     dfmsgs = self._dfmsgs
    #     dfmsgs.columns = self.__colnames
    #     msgs
    #     attstblid = datetime.datetime.now().strftime("atts_%j_%H%M")

    #     # df.to_sql(attstblid, con=self.__engine,
    #    #           if_exists='replace', index=False)
    #     print('Msgs table written to ', msgstblid)
    #     print('Atts table written to ', attstblid)
    #     # dfatts = df['AttsUIDs'].T
    #     # x = dfatts.to_string(header=False, index=False).split('\n')
    #     # vals = [','.join(ele.split()) for ele in x]
    #     # y = ','.join(vals)

    #     self._dfmsgs = pd.DataFrame()
