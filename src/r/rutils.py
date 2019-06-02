import os
#import rpy2
from rpy2 import robjects, rinterface
#from rpy2.robjects import Formula, Environment
# from rpy2.robjects.vectors import IntVector, FloatVector, StrSexpVector,
#from rpy2.robjects.lib import grid
from rpy2.robjects.packages import importr  # , data
from rpy2.rinterface import RRuntimeError
import warnings


scjr = importr("scjr")
base = importr('base')
#rcat = rinterface.baseenv['cat']
rpaste = base.paste
rcat = base.cat


def pdf2str(filename):
    pdftxt = scjr.pdf_content(filename)
    y = base.paste(pdftxt, sep='', collapse='')
    return y[0]


path = r'c:/pyext/.c.johnson370---1--.pdf'
#txt = scjr.pdf_content(path)
# (StrSexpVector(list(x)))
# rcat(y)
