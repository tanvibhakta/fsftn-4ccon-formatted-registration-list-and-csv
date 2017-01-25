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
    header = 'To:' + toaddr + '\n' + 'From: ' + from_addr + '\n' + 'Subject: Ticket\n'
    msg = header + msg
    smtpserver.sendmail(from_addr, toaddr, msg)
    print 'done!'
    smtpserver.quit()

#to find who paid
c.execute('SELECT * FROM tickets_tickets WHERE status==3 OR status==4;')
field = c.fetchall()

for i in range(len(field)):

    toaddr = field[i][9]
    name = field[i][8]
    order_type = field[i][6]
    ticket_id = field[i][5]
    workshop_id = field[i][17]
    phone_no = field[i][10]

    #start email
    msg = "Hey, "
    msg += name


    if (order_type == "bronze" or order_type == "silver" or order_type == "platinum"):

        #get workshop's name from_addr given id
        c.execute('SELECT title FROM proposals_proposal JOIN tickets_tickets ON proposals_proposal.id ==?;', (workshop_id, ))
        workshop_name = c.fetchone()
        msg += "\n\nThis is to remind you that you have registered for **"
        if workshop_id == None: #balu case
            workshop_name = ["dummy"]
        else:
            msg += workshop_name[0]
        msg += "** on Thursday, the 26th of January as a part of the 2nd National Conference, 4CCon.\n\nThe prerequisites for the workshop are:"

        #removes special characters
        file_name = './reports/'+''.join(e for e in workshop_name[0] if e.isalnum()) + '.csv'

        f = None
        #creates file using workshop name
        if os.path.isfile(file_name):
            f = open(file_name, 'a')
        else:
            f = open(file_name, 'w+')


        var = ""
        var += ticket_id +',' + name +',' + toaddr +',' + phone_no +',' + order_type
        f.write(var)
        f.close()

        #get workshop's prerequisites given id
        c.execute('SELECT prerequisites FROM proposals_proposal JOIN tickets_tickets ON proposals_proposal.id == ?;', (workshop_id, ))
        prerequisites = c.fetchone()
        if workshop_id == None: # balu case
            pass
        else:
            msg += prerequisites[0]


    if (order_type == "gold"):
        msg += "\n\nThis is to remind you that you have registered for 4CCOn, the 2nd National Conference of FSMI, starting on **Friday, the 27th of January.**"

    #messages are commom from_addr this point onwards
    msg += "\n\n Your ticket id is "
    msg += str(ticket_id)

    msg += """\n\nThe schedule for the conference can be found at 4ccon.fsmi.in/schedule\n\nThe venue of the conference is B.S. Abdur Rahman University (formerly Crescent Engineering College) at Vandalur. The venue is well connected by train and bus. If you are coming from_addr the city, you could take the local train to Vandalur. The closest bus stop is the Vandalur Zoo bus stop. The university is right next to the zoo. If you are travelling from_addr other parts of Tamil Nadu, you could take the train to Tambaram or bus to Chengalpet or Perungalathur and then reach the venue by local buses or share auto.

On reaching the campus, head over to the Convention Centre. You can collect your conference kit at the registration desk next to the Convention Centre. The workshops will commence at 10 a.m. at the Mechanical Department. We request you to be present at 9 a.m., so that there is enough time to collect your kit and head over to the workshop venue. As it is a big campus, it may take about 15 minutes to reach the Convention Centre from_addr the gate.

Kindly carry

1. Laptop, charger and spike buster if you so require.
2. An alteranate internet source if you have one (We will provide internet at the venue but we cannot be assured of speed or reliability).
3. ID proof and additionally, college ID card (if you are a student or from academia).
4. For outstation participants, we advise you to carry photocopies of your ID proof which maybe required at the time of checking-in at accommodation.

Please provide your name, ticket ID (as mentioned in your confirmation mail) and pass type (Bronze/Silver/Gold/Platinum) at the registration desk to collect your kit.

We look forward to seeing you at 4CCon!

Regards,
FSMI
4ccon.fsmi.in

Srravya : +91 9962943247
Anand : +91 9043475346
4ccon@fsftn.org
044 -43504670 """

    send_mail(toaddr,msg)
