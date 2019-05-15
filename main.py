import sys
import os
from session import Sesh
from folderrecurse import pcur
import pandas as pd

# GET OUTLOOK NAMESAPACE
session = Sesh()
for box in session.ol_boxes:
    box_n = session.Outlook.GetFolderFromID(box)
    pcur(session, box_n.parent)

session.WrtieToDB()
