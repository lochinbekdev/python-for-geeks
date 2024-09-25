import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import os
 

server = smtplib.SMTP('mail.jdpu.uz',25)

server.ehlo()

current_dir='/home/kali/project/pkb/python-for-geeks/extra/'

file_path_pass = os.path.join(current_dir, 'password.txt')

with open(file_path_pass,'r') as f:
    password = f.read()
    
server.login('mailtest@jdpu.uz',password)

msg=MIMEMultipart()
msg['From'] = 'Lochinbek'
msg['To']= 'occupytheweb@jdpu.uz'
msg['Subject'] = 'Just a test'


file_path_msg = os.path.join(current_dir, 'message.txt')

with open('file_path_msg') as f:
    message=f.read()
    
msg.attach(MIMEText(message,'plain'))

file_path = os.path.join(current_dir, 'screeen.png')
attachment=open(file_path,'rb')

p=MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={file_path}')
msg.attach(p)


text=msg.as_string()
server.sendmail('mailtest@jdpu.uz','occupytheweb@jdpu.uz',text)
