# merge multiple pdf files into one
from PyPDF2 import PdfFileMerger, PdfFileReader
mergedObject = PdfFileMerger()
# name/rename the files with a common pattern like - "file1.pdf", "file2.pdf", "file3.pdf",...,"filen.pdf"
for file_number in range(1, n):
    mergedObject.append(PdfFileReader('file' + str(file_number)+ '.pdf', 'rb'))
# moment of truth 
mergedObject.write("joined-pdf.pdf")
