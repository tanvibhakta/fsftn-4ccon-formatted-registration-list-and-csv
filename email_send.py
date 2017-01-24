import sqlite3, smtplib
from email.mime.text import MIMEText

fromaddr = '4ccon@fsftn.org'

#python talking to the database
c = sqlite3.connect('db.sqlite3').cursor()

#setting up the server
#s = smtplib.SMTP('localhost')

c.execute('SELECT * FROM tickets_tickets;')
field = c.fetchall()

for i in range(len(field)):

    test = 'tanvibhakta@gmail.com'
    print "Inside for"

        c.execute('SELECT email FROM tickets_tickets;')
        toaddr = c.fetchall()
        print toaddr[i]

        c.execute('SELECT name FROM tickets_tickets;')
        name = c.fetchall()
        print name[i]

        c.execute('SELECT order_type FROM tickets_tickets;')
        order_type = c.fetchall()
        print order_type[i]

        msg = ("Hey %s,/n/n/r" % (name, ))

        if (order_type is "bronze" or "silver" or "platinum"):
            c.execute('SELECT title FROM proposals_proposal JOIN tickets_tickets ON proposals_proposal.id == tickets_tickets.workshop_id;')
            workshop_name = c.fetchall()
            print workshop_name[i]

            c.execute('SELECT prerequisites FROM proposals_proposal JOIN tickets_tickets ON proposals_proposal.id == tickets_tickets.workshop_id;')
            prerequisites = c.fetchall()

        if (order_type is "gold" or "platinum"):
            pass
            #just text here


        msg['Subject'] = 'Your 4ccon workshop registration'
        msg['From'] = fromaddr
        msg['To'] = test


        #s.sendmail(fromaddr, toaddr, msg.as_string())


#s.quit()
