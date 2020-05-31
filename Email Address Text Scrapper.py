import re
import os.path

# Opening the file containing emails
f = open(r"C:\Users\sarou\Desktop\emailsample.txt", 'r')
# Declaring the saveing location
save_location = r"C:\Users\sarou\Desktop"
# Declaring the name of saved file
saved_file_name = "Emails.txt"
# Reading the file of emails 
text = f.read()
# Making a pattren for emails
pattren = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9\.\-\_]+\.[a-zA-Z0-9\.\-\_]+")
# Search and appending the file for the pattren
result = pattren.findall(text)
# A List is made containing all emails
# Making a new file with output cvs file being saved on your desktop 
output = open( os.path.join(save_location, saved_file_name), "w+")
# Iterating through list and writing it in the file 
for i in range ( len(result)):
    output.write("\n"+ result[i] + "," )
# Closing the file 
output.close()




