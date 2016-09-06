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


my_email = raw_input("Your Email: ")
my_password = raw_input("Email Password: ")

while(1):
	ward_member = raw_input('Ward Member: ')
	bishop_last_name = raw_input('Bishop Last Name: ')
	bishop_email = raw_input('Bishop email: ')

	email_msg = 'Bishop %s,\n\nThe Provo YSA 91st Ward in Provo, Utah has received the membership records of %s and would like to extend a calling as soon as possible.\n\nIf you have any comments about strengths, or concerns regarding a calling being extended, a temple recommend being issued, or an ecclesiastical endorsement given to this member, please email Bishop Hansen at:\n\n\t\tjeff@johnnys.com\n\nOr call or text at 801-471-4834\n\nThank you,\nMarcus Tanner\nAssistant Clerk\nProvo YSA 91st Ward' % (bishop_last_name, ward_member)

	send_email(my_email, my_password, bishop_email, ward_member + ' Prior Unit Ward Calling', email_msg)
	print