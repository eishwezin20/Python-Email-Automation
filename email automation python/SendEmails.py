from smtplib import SMTP  

sender = ' '    // your mail here
Password = ' '          //  your password
recipient = ' ' //  to?

connect_server = SMTP( host ='smtp.mail.yahoo.com', port = 587)
connect_server
connect_server.starttls()
connect_server.login(user = sender, password = Password)
connect_server.sendmail(
	from_addr = sender, 
	to_addrs = recipient, msg = 'Subject:Discount Offer\n\nHi, there.')
connect_server.close()
