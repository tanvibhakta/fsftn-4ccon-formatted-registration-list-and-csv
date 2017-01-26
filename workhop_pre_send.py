import sqlite3, smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#python talking to the database
c = sqlite3.connect('db.sqlite3').cursor()
test = 'tanvibhakta@gmail.com'

def send_mail(to,msg):
    from_addr = '4ccon@fsftn.org'
    passwd = '$Ccon!$32'
    smtpserver = smtplib.SMTP("mail.fsftn.org",587)
    print smtpserver.ehlo()
    print smtpserver.starttls()
    smtpserver.ehlo() # extra characters to permit edit
    smtpserver.login(from_addr, passwd)
    header = 'To:' + to + '\n' + 'From: ' + from_addr + '\n' + 'Subject: Regarding a heads up on your workshop!\n'
    msg = header + msg
    smtpserver.sendmail(from_addr, to, msg)
    print 'done!'
    smtpserver.quit()

#to find who paid
workshop_id_list = [22, 48, 14]

for workshop_id in workshop_id_list:

    c.execute('SELECT * FROM tickets_tickets JOIN proposals_proposal ON workshop_id==proposals_proposal.id WHERE proposals_proposal.id=? and (tickets_tickets.status==1 or tickets_tickets.status==2);', (workshop_id, ))
    field = c.fetchall()

    for i in range(len(field)):

        toaddr = field[i][9]
        order_type = field[i][6]
        workshop_id = field[i][17]
        phone_no = field[i][10]
        status = field[i][12]
        print workshop_id
        print status

        #start email
        msg = "Hey,\n\nKindly disregard the previous email. We are very sorry for any inconvenience caused. "


        msg += """\n\n
    Regards,
    FSMI
    4ccon.fsmi.in

     """

        #send_mail(test, msg)
