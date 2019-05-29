from sqlalchemy import create_engine, text
import cymysql
import pandas as pd
import csv

#df = pd.read_sql_query

engine = create_engine(
    'mysql+cymysql://rstudio@localhost:3306/email?charset?utf8mb4', echo=False)
qry = text(r'UPDATE emailaddress SET Domain = UPPER(:domain) WHERE REGEXP_INSTR(emailfrom, :searchstr , 1, 0, 0, :i)')
conn = engine.connect()
conn.execute(qry, domain='RBC', searchstr='rbc', i='i')

domain = []
searchstr = []
with open('C:\\Dev\\pyExchangeExtractor\\src\\DomainKeys.csv', 'r') as f:
    data = csv.reader(f)
    for row in data:
        domain.append(row[0].strip())
        searchstr.append(row[1].strip())
print(domain)

for n in range(0, len(domain)):
    print(domain[n], searchstr[n])
    conn.execute(qry, domain=domain[n], searchstr=searchstr[n], i='i')
print('Done')
