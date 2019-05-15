import sys
from sqlalchemy import create_engine
import pandas as pd
import win32com
from win32com import universal
from win32com.client import constants
from win32com.server.exception import COMException
from win32com.client import gencache, DispatchWithEvents
import winerror


class Sesh(object):

    def __init__(self):
        self.__engine = create_engine(
            "mysql+mysqlconnector://rstudio@localhost:3306/tmp", echo=True)
        self.__msg_int = 0
        self.__att_int = 0
        self.__msg_uids = pd.read_sql(
            'SELECT * from `final`.`email_msg_uids` WHERE not MsgUID in (select MsgUID from `final`.`email_msgs`) LIMIT 200', self.__engine)
        self.__att_uids = pd.read_sql(
            'SELECT * from `final`.`email_att_uids` WHERE not AttUID in (select AttUID from `final`.`email_atts`) LIMIT 200', self.__engine)
        self.__ol_boxes = ["0000000088A9AE601D4FBF4092794F7DADA800F00180ABE5D4B62B1BBB4AA951CDA06B3165AD00000000010C0100",
                           "0000000052D39FFD9378D611965500508B5C12B401002F5A794942E9D21195FC0008C7E9CC5F000003DD578E0000"]
        self.__path = 'c:/pyext/'
        self.__outlook = win32com.client.Dispatch(
            "Outlook.Application").GetNamespace("MAPI")
        self.__colnames = ['OutlookFolder', 'EMailFrom', 'Body', 'AttCount', 'Subject',
                           'AttsUIDs', 'EmailUID', 'ConversationID', 'ConversationIndex', 'EntryID', 'Received']
        self.__df_msgs = pd.DataFrame(columns=self.__colnames)

    def AppendDataFrame(self, df):
        if self.__df_msgs.empty:
            df1 = pd.DataFrame(df)
            self.__df_msgs = df1.T
            print('DataFrame Created')
        else:
            df0 = pd.DataFrame(df)
            df1 = df0.T
            self.__df_msgs = self.__df_msgs.append(df1, ignore_index=True)
            print('DataFrame Updated')

    def WrtieToDB(self):
        df = self.__df_msgs
        df.columns = self.__colnames
        df.to_sql('thing0', con=self.__engine,
                  if_exists='replace', index=False)

    @property
    def DataFrameMsgs(self):
        """
        :type: DataFrame
        """
        return self.__df_msgs

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

    @property
    def att_uid(self):
        """
        :type: string
        """
        return self.__att_uids.loc[self.__att_int]["AttUID"]

    @property
    def msg_uid(self):
        """
        :type: string
        """
        return self.__msg_uids.loc[self.__msg_int]["MsgUID"]

    def __get_msg_idx(self):
        """
        :type: int
        """
        return self.__msg_int

    def __set_msg_idx(self, value):
        """
        :type: int
        """
        self.__msg_int = value

    def __get_att_idx(self):
        """
        :type: int
        """
        return self.__att_int

    def __set_att_idx(self, value):
        """
        :type: int
        """
        self.__att_int = value
    msg_idx = property(__get_msg_idx, __set_msg_idx)
    att_idx = property(__get_att_idx, __set_att_idx)

    def refresh_uis(self):
        self.__msg_uis = pd.read_sql(
            'SELECT * from `final`.`email_msg_uids` WHERE not MsgUID in (select MsgUID from `final`.`email_msgs`)', self.__engine)
        self.__att_uis = pd.read_sql(
            'SELECT * from `final`.`email_att_uids` WHERE not AttUID in (select AttUID from `final`.`email_atts`)', self.__engine)

    def is_empty(self, tup):
        y = False
        for x in tup:
            y = not x or y
            if y:
                return y
        return y
