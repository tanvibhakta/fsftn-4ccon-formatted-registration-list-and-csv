import sqlite3, smtplib
from email.mime.text import MIMEText

fromaddr = '4ccon@fsftn.org'

c = sqlite3.connect('db.sqlite3').cursor()
c.execute('SELECT email FROM tickets_tickets;')
toaddr = c.fetchone()

fp = open('text.txt', 'rb')
msg = "Hey, "
fp.close()

msg['Subject'] = 'Your 4ccon workshop registration'
msg['From'] = fromaddr
msg['To'] = toaddr

s = smtplib.SMTP('localhost')
s.sendmail(fromaddr, toaddr, msg.as_string())
s.quit()
