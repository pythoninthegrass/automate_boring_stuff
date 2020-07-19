#!/usr/bin/env python3

import pyzmail
from datetime import date
from getpass import getpass
from imapclient import IMAPClient
from pprint import pprint

# init
conn = IMAPClient('imap.gmail.com', ssl=True, use_uid=True)

# creds
eml_addr = input('Please enter your Gmail address: ')
passwd = getpass('Enter app-specific password: ')

# login
# conn.login('<sender_email>', '<password>')
conn.login(eml_addr, passwd)

# check inbox
select_info = conn.select_folder('INBOX', readonly=True)
print('%d messages in INBOX' % select_info[b'EXISTS'])

# list folders
conn.list_folders()

# find email
messages = conn.search([u'SINCE', date(2020, 1, 1)])
for msgid, data in conn.fetch(messages, ['ENVELOPE']).items():
    envelope = data[b'ENVELOPE']
    print('ID # %d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))

# read individual messages
raw = conn.fetch([10], ['BODY[]'])
msg = pyzmail.PyzMessage.factory(raw[10][b'BODY[]'])

msg.get_subject()
msg.get_addresses('from')
msg.get_addresses('to')

msg.text_part                                               # MailPart<*text/plain charset=UTF-8 len=2990>
msg.html_part                                               # MailPart<*text/html charset=UTF-8 len=19484>
msg.html_part == None                                       # false
print(msg.text_part.get_payload().decode('UTF-8'))          # body message

# delete emails
conn.select_folder('[Gmail]/Spam', readonly=False)
uids = conn.search('SINCE 1-Jan-2020')
# conn.delete_messages(uids)
# conn.delete_messages([10, 13, 14, 15])

# quit
conn.logout()