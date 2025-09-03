#!/usr/bin/env python

from getpass import getpass
import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)

# init (200+ status == success)
conn.ehlo()

# encryption
conn.starttls()

# TODO: read file for creds
# creds (app-specific password)
# HARD-CODED
# conn.login('<sender_email>', '<password>')
# DYNAMIC
eml_from = input('Please enter your Gmail address: ')
passwd = getpass('Enter app-specific password: ')
eml_to = input("Please enter recipient's email address: ")
conn.login(eml_from, passwd)

# email to self
# HARD-CODED
# conn.sendmail('<sender_email>', '<recipient_email>', "Subject: Hello world!\n\nGreeting,\n\nNot as sexy as the first, but very, very, useful.\n\nCheers,\nSelf")
# DYNAMIC
conn.sendmail(eml_from, eml_to, "Subject: Hello world!\n\nGreeting,\n\nNot as sexy as the first, but very, very, useful.\n\nCheers,\nSelf")

# quit
conn.quit()
