# Import required packages
import cv2
import pytesseract

# Mention the installed location of Tesseract-OCR in your system
# pytesseract.pytesseract.tesseract_cmd = 'System_path_to_tesseract.exe'

# Read image from which text needs to be extracted
Sample_img = cv2.imread("img.png")

# Preprocessing the image starts
# Sample_img = cv2.resize(img,(400,350))
Image_ht,Image_wd,Image_thickness = Sample_img.shape
Sample_img = cv2.cvtColor(Sample_img,cv2.COLOR_BGR2RGB)
texts = pytesseract.image_to_data(Sample_img)
my_text= ""
prev_y=0
for cnt,text in enumerate(texts.splitlines()):
    if cnt==0:
        continue
    text = text.split()
    if len(text)==12:
        x,y,w,h = int(text[6]),int(text[7]),int(text[8]),int(text[9])
        if len(my_text)==0:
            prey=y
        if prev_y-y>=10 or y-prev_y>=10:
            print(my_text)

            my_text= ""
        my_text = my_text + text[11] + " "
        prev_y=y
# Open the file in append mode
file = open("recognized.txt", "a")

# Appending the text into file
file.write(my_text)
# Close the file
file.close()