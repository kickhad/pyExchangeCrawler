import pandas as pd
df = pd.DataFrame([['A', 2], ['A', 4], ['B,B', 6]])
df.columns = ['X', 'Y']

def 
dft = df['X'].T
x = dft.to_string(header=False, index=False).split('\n')
vals = [','.join(ele.split()) for ele in x]
y = ','.join(vals)
y