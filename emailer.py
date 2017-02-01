def send_email(user, pwd, recipient, subject, body):
    import smtplib
    import sys

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"
	print sys.exc_info()[0]


my_name = raw_input("Your Name: ")
my_email = raw_input("Your Email: ")
my_password = raw_input("Email Password: ")
my_bishop = raw_input("Your Bishop's Last Name: ")
my_bishop_email = raw_input("Your Bishop's Email: ")
my_bishop_phone = raw_input("Your Bishop's Phone #: ")
my_ward = raw_input("Your Ward Name: ")

while(1):
	ward_member = raw_input('New Ward Member: ')
	previous_bishop_last_name = raw_input('Former Bishop Last Name: ')
	previous_bishop_email = raw_input('Former Bishop email: ')

	email_msg = 'Bishop %s,\n\nThe %s Ward has received the membership records of %s and would like to extend a calling as soon as possible.\n\nIf you have any comments about strengths, or concerns regarding a calling being extended, a temple recommend being issued, or an ecclesiastical endorsement given to this member, please email Bishop %s at:\n\n\t\t%s\n\nOr call or text at %s\n\nThank you,\n%s\nWard Clerk\n%s' % (previous_bishop_last_name, my_ward, ward_member, my_bishop, my_bishop_email, my_bishop_phone, my_name, my_ward)

	send_email(my_email, my_password, previous_bishop_email, ward_member + ' Prior Unit Ward Calling', email_msg)
	print
