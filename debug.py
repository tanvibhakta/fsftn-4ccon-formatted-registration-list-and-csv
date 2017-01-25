import sqlite3, smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#### NAME EMAIL ID PASS TYPE CONTACT ORDER ID

fromaddr = '4ccon@fsftn.org'

#python talking to the database
c = sqlite3.connect('db.sqlite3').cursor()

#setting up the server
#s = smtplib.SMTP('localhost')

c.execute('SELECT * FROM tickets_tickets WHERE status==3 OR status==4;')
field = c.fetchall()

for i in range(3):
    msg = ""
    toaddr = field[i][9]

    name = field[i][8]

    order_type = field[i][6]

    ticket_id = field[i][0]
    workshop_id = field[i][17]

    if (order_type == "bronze" or order_type == "silver" or order_type == "platinum"):
        c.execute('SELECT title FROM proposals_proposal JOIN tickets_tickets ON proposals_proposal.id ==?;', (workshop_id, ))
        workshop_name = c.fetchone()
        print workshop_name[0]

        c.execute('SELECT prerequisites FROM proposals_proposal JOIN tickets_tickets ON proposals_proposal.id == ?;', (workshop_id, ))
        prerequisites = c.fetchone()
        msg += prerequisites[0]

        f = None
        file_name = ''.join(e for e in workshop_name[0] if e.isalnum()) + '.csv'

        #creates file using workshop name
        if os.path.isfile(file_name):
            f = open(file_name, 'a')
        else:
            f = open(file_name, 'w+')
