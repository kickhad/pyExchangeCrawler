# SET PATH = % PATH % ; C: \Users\B313422\Documents\R\R-3.5.3\bin;
import rpy2.interactive as r
import rpy2.interactive.packages
import rpy2.rinterface as rinterface
r.packages.importr("tm")
r.packages.importr("pdftools")

rlib = r.packages.packages
readPDF = rlib.tm.readPDF
pdf_text = rlib.pdftools.pdf_text
z = pdf_text(r'c:\pyext\.c.johnson370---1--.pdf')
document < -Corpus(URISource(pdf_file), readerControl=list(reader=pdf_read))
result < - content(document[[1]])

rinterface.initr()
rinterface.endr()
print(z)