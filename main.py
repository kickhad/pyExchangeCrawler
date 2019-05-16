import sys
import os
from session import Sesh
from folderrecurse import pcur
import pandas as pd

# GET OUTLOOK NAMESAPACE
session = Sesh()
#pcur(session, session.Outlook.GetDefaultFolder(6))
for box in session.ol_boxes:
    box_n = session.Outlook.GetFolderFromID(box)
    pcur(session, box_n.parent)

session.WrtieToDB()
