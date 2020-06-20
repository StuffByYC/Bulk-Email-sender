from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import os
import pandas as pd 


data = pd.read_csv("Email ID.csv")
df=data

for index, row in df.iterrows():
    Name =  str(row['Name'])
    Email = str(row['Email'])
    print(Name)
    print(Email)
    
    # Your Email ID
    user = '********@gmail.com'
    
    #Enter your Application password check https://support.google.com/accounts/answer/185833?hl=en to get Application Password for Gmail
    app_password = "Enter app password here"
    host = 'smtp.gmail.com'
    port = 465
    to = Email
    
    subject = 'Business Proposal'
    # Content can be in html format or plain text ( Use html format to format text)
    content_txt = ' Enter your content here /n This is Easy'
    attachment1 = 'Service Price List.pdf'
    
    ### Define email ###
    message = MIMEMultipart()
    # add From 
    message['From'] = Header(user)
    # add To
    message['To'] = Header(to)     
    # add Subject
    message['Subject'] = Header(subject)
    # add content text
    # Instead of plain use html if you declared content_txt in HTML format 
    message.attach(MIMEText(content_txt, 'plain', 'utf-8')) 
    # add attachment1
    att_name = os.path.basename(attachment1)
    att1 = MIMEText(open(attachment1, 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename=' + att_name
    message.attach(att1)
        
    ### Send email ###
    server = smtplib.SMTP_SSL(host, port) 
    server.login(user, app_password)
    server.sendmail(user, to, message.as_string()) 
    server.quit() 
    print('Email Sent successfully')    
