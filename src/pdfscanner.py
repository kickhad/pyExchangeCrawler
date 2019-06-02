from rpy2.robjects.packages import importr
import rutils
import pandas as pd
import os
import clipboard
import hyper
import pandas.rpy.common as com
from googletrans import Translator
from rpy2.robjects.vectors import StrSexpVector
from rutils import rpaste, rcat, pdf2str
# 'c:/pyext/S.C. JOHNSON & FILS LIMITEE-INV#960801323895---2--.pdf'
path = 'c:/pyext/Secondary/Avis de déduction---1--uzzejcpdv5J4nVseu5g5oi.pdf'
pdf_content = rutils.scjr.pdf_content
# BUILD PDF TEXT
# POPULATE DATA FRAME
# SEND FRAME TO TRANSLATE
# REPOPULATE DATAFRAME
en = ['', '', '']
fr = ['oui', 'poulette', 'avec']
df = pd.DataFrame({"English": en,
                   "French": fr
                   })
df
translator.translate(df['French'].iterrows())

scjr = importr("scjr")
scjr.pdf_to_rows(path)
pdfvec = pdf_content(path)
flatpdf = rutils.pdf2str(path)
str(flatpdf)
rcat(pdfvec)
str(pdfvec)
pystr = str(flatpdf)
flatpdf[0]
#listpystr = pystr.split(r'\\r\\n')
pystr_striped_newlines = pystr.replace('\\r\\n', ' ROWNEW ')
pystr_translated = translator.translate(pystr_striped_newlines)
pystr_replace_new_lines = pystr_translated.text.replace(' ROWNEW ', '\\r\\n')
pycat(pystr_replace_new_lines)
pycat(pystr)
z = translator.translate(flatpdf[0].split('\r\nz.'))
for f in pystrp1.split('\\r\\n'):
    z = translator.translate(flatpdf[0])
    print(z.text)
print()
translator = Translator()
clipboard.copy(pystr.replace('\\', '\\\\'))
rcat(rcat(StrSexpVector(listpystr)))


def pycat(str):
    pstr = str.split('\\r\\n')
    for p in pstr:
        print(p)


for x in z:
    print(x.text)
