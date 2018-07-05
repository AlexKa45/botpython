import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

fromaddr = "kasperskiialex@gmail.com"
mypass = "Zoasler2909"
toaddr = "platonovaleks2909@gmail.com"

def send(message):
  msg.attach(MIMEText(message, 'plain'))
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(fromaddr, mypass)
  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  server.quit()
