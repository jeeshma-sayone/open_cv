# importing required modules
import PyPDF2
import qrcode

# creating a pdf file object
pdfFileObj = open('sample.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
data = pageObj.extractText()
print(data)

# closing the pdf file object
pdfFileObj.close()

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('MyQRCode1.png')