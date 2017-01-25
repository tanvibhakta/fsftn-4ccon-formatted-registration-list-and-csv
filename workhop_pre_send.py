import sqlite3, smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#python talking to the database
c = sqlite3.connect('db.sqlite3').cursor()

def send_mail(to,msg):
    from_addr = '4ccon@fsftn.org'
    passwd = '$Ccon!$32'
    smtpserver = smtplib.SMTP("mail.fsftn.org",587)
    print smtpserver.ehlo()
    print smtpserver.starttls()
    smtpserver.ehlo() # extra characters to permit edit
    smtpserver.login(from_addr, passwd)
    header = 'To:' + to + '\n' + 'From: ' + from_addr + '\n' + 'Subject: A heads up on your workshop!\n'
    msg = header + msg
    smtpserver.sendmail(from_addr, to, msg)
    print 'done!'
    smtpserver.quit()

#to find who paid
workshop_id_list = [22, 48, 14]

for workshop_id in workshop_id_list:

    c.execute('SELECT * FROM tickets_tickets JOIN proposals_proposal ON workshop_id==proposals_proposal.id WHERE proposals_proposal.id=?;', (workshop_id, ))
    field = c.fetchall()

    for i in range(len(field)):

        toaddr = field[i][9]
        order_type = field[i][6]
        workshop_id = field[i][17]
        phone_no = field[i][10]

        #start email
        msg = "Hey,\n\nFor your workshop on "

        #get workshop's name from_addr given id
        c.execute('SELECT title FROM proposals_proposal WHERE id ==?;', (workshop_id, ))
        workshop_name = c.fetchone()
        if workshop_id == None: #balu case
            workshop_name = ["dummy"]
        else:
            msg += workshop_name[0]
        msg += " here's some information we just received from the speaker\n\n "

        #removes special characters
        #file_name = './reports/'+''.join(e for e in workshop_name[0] if e.isalnum()) + '.csv'

        # f = None
        # #creates file using workshop name
        # if os.path.isfile(file_name):
        #     f = open(file_name, 'a')
        # else:
        #     f = open(file_name, 'w+')
        #

        # var = ""
        # var += ticket_id +',' + name +',' + toaddr +',' + phone_no +',' + order_type
        # f.write(var)
        # f.close()

        #get workshop's prerequisites given id
        c.execute('SELECT prerequisites FROM proposals_proposal WHERE id == ?;', (workshop_id, ))
        prerequisites = c.fetchone()
        if workshop_id == None: # balu case
            pass
        else:
            msg += prerequisites[0]

        msg += """\n\nWe look forward to seeing you at 4CCon!

    Regards,
    FSMI
    4ccon.fsmi.in

    Srravya : +91 9962943247
    Anand : +91 9043475346
    4ccon@fsftn.org
    044 -43504670 """

        send_mail(toaddr, msg)
