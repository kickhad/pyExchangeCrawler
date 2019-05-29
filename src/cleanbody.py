import os
import sys
import clipboard
import re
import pandas as pd
from data import getEngine
from session import Sesh
import settings
engine = getEngine()

df = pd.read_sql('SELECT * FROM bodys', con=engine)
print(df)
lbody = []
lids = []
lidx = []
for idx, body, ids in df.itertuples():
    lbody.append(body)
    lids.append(ids)
    lidx.append(idx)
print(1)
newlbody = lbody

with open('remove.txt', 'r') as f:
    strs = f.read().split('\n')


for n in range(0, len(lbody)):
    for s in strs:
        newlbody[n] = re.sub(s, ' ', lbody[n])


print(len(lbody[1])-len(newlbody[1]))

df1 = pd.DataFrame(
    {
        'index': lidx,
        'Body': newlbody,
        'BodyID': lids
    }
)
clipboard.copy(newlbody[1139])

df1.to_sql('newbody', con=engine, if_exists='replace')
