import shortuuid
import collections
# class uuidstore(object):
#     def __init__(self):
#         self._attuuid = ""
#         self._msguuid = ""
#         self._attUuidList = UuidList()
#         self._msgUuidList = UuidList()

#     @property
#     def AttUUID(self):
#         """
#         :type: str
#         """
#         return self._attuuid

#     @property
#     def MsgUUID(self):
#         """
#         :type" str
#         """
#         return self._msguuid


class uuidlist(object):
    def __init__(self):
        self._currentUUID = ""
        self.uuids = collections.OrderedDict()
        self._key = 0
        self.uuids[0] = ""

    @property
    def CurrentUUID(self):
        """
        :type: str
        """
        return self.uuids[self._key]

    def NextUUID(self):
        x = False
        while not x:
            uuid = shortuuid.uuid()
            if not uuid[:8] in self.uuids.values():
                self._key += 1
                self.uuids[self._key] = uuid[:8]
                x = True
        return self.uuids[self._key]

    # @CurrentUUID.setter
    # def _setCurrentUUID(self, value):
    #     """
    #     :type: str
    #     """
    #     if value in self:
    #         self._currentUUID = value
    #     else:
    #         print('Bad UUID')

    def Seed(self, n):
        for x in range(1, n):
            self.NextUUID()
