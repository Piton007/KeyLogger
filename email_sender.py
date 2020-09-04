import smtplib
smtpServer = "smtp.gmail.com"
fromAddr = "user222@gmail.com"
toAddr = "josemowa@gmail.com"
text = "This is a test of sending email from user222"
server = smtplib.SMTP(smtpServer,25)
server.ehlo()
server.starttls()
server.sendmail(fromAddr,toAddr,text)
server.quit()

