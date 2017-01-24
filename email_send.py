import sqlite3, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fromaddr = '4ccon@fsftn.org'

#python talking to the database
c = sqlite3.connect('db.sqlite3').cursor()

#setting up the server
#s = smtplib.SMTP('localhost')

c.execute('SELECT * FROM tickets_tickets WHERE status==3 OR status==4;')
field = c.fetchall()

for i in range(len(field)):

    test = 'tanvibhakta@gmail.com'

    toaddr = field[i][9]
    print toaddr

    name = field[i][8]
    print name

    order_type = field[i][6]
    print order_type

    ticket_id = field[i][0]
    workshop_id = field[i][17]

    msg = "Hey, "
    msg.attach(name)

    if (order_type == "bronze" or order_type == "silver" or order_type == "platinum"):
        c.execute('SELECT title FROM proposals_proposal JOIN tickets_tickets ON proposals_proposal.id ==?;', (workshop_id, ))
        workshop_name = c.fetchall()

        c.execute('SELECT prerequisites FROM proposals_proposal JOIN tickets_tickets ON proposals_proposal.id == ?;', (workshop_id, ))
        prerequisites = c.fetchall()

    if (order_type is "gold" or "platinum"):
        pass
        #just text here


    # msg['Subject'] = 'Your 4ccon workshop registration'
    # msg['From'] = fromaddr
    # msg['To'] = test
    #

        #s.sendmail(fromaddr, toaddr, msg.as_string())


#s.quit()
