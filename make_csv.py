import sqlite3, os

#python talking to the database
c = sqlite3.connect('db.sqlite3').cursor()

#to find who paid
c.execute('SELECT * FROM tickets_tickets WHERE (status==3 OR status==4) AND (order_type=="bronze" OR order_type=="silver" OR order_type=="platinum");')
field = c.fetchall()

for i in range(len(field)):

# order id name email ph no workshop_name order type

    toaddr = field[i][9]
    name = field[i][8]
    order_type = field[i][6]
    ticket_id = field[i][5]
    workshop_id = field[i][17]
    phone_no = field[i][10]

    #get workshop's name from given id
    c.execute('SELECT title FROM proposals_proposal JOIN tickets_tickets ON proposals_proposal.id ==?;', (workshop_id, ))
    workshop_name = c.fetchone()

    #removes special characters

    if workshop_id == None: #balu case
        workshop_name = ["dummy"]
    else:
        file_name = './reports/'+''.join(e for e in workshop_name[0] if e.isalnum()) + '.csv'

    #if os.path.exists(file_name):
    f = open(file_name, 'a')
    #else:
    #    f = open(file_name, 'w+')

    var = ""
    var += ticket_id +',' + name +',' + toaddr +',' + phone_no +',' + order_type
    f.write(var)
    f.close()
