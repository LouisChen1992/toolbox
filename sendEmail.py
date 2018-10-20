import os
import argparse
import smtplib
from email.mime.text import MIMEText

parser = argparse.ArgumentParser(description='Send Email Notification')
parser.add_argument('--FROM', help='From') # set a default value
parser.add_argument('--TO', help='To') # set a default value
parser.add_argument('--p', help='p')
parser.add_argument('--s', default='Email Noticifation', help='Subject')
parser.add_argument('--MSG', default='', help='Message')
args = parser.parse_args()

s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login(args.FROM, args.p)

if os.path.exists(args.MSG):
	with open(args.MSG, 'r') as f:
		msg = MIMEText(''.join(f.readlines()))
else:
	msg = MIMEText('')
msg['Subject'] = args.s
msg['From'] = args.FROM
msg['To'] = args.TO
s.send_message(msg)
s.quit()
