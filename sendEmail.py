import smtplib
import imghdr
from email.message import EmailMessage


EmailAddress = 'python.tenwarat@gmail.com'
EmailPassword = 'Ten28209'

contact = 'facelessten@gmail.com'
#%%
msg = EmailMessage()
msg['Subject']= 'test to send Photo'
msg['From']= EmailAddress
msg['To']= contact
msg.set_content('Fire detected!!!!!')

with open('fireDetect.jpg','rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
#%%
msg.add_attachment(file_data,maintype='image',subtype = file_type,filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

    smtp.login(EmailAddress,EmailPassword)
    smtp.send_message(msg)
    print('sending success')
    smtp.quit()

