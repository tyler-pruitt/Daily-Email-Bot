#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:23:10 2020

@author: tylerpruitt
"""


import smtplib
import ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def next_week_day(day):
    if week_day == 'Mon':
        return 'Tue'
    elif week_day == 'Tue':
        return 'Wed'
    elif week_day == 'Wed':
        return 'Thu'
    elif week_day == 'Thu':
        return 'Fri'
    elif week_day == 'Fri':
        return 'Sat'
    elif week_day == 'Sat':
        return 'Sun'
    else:
        return 'Mon'

port = 465

from_email = input('Enter sender email address: ')
password = input('Enter password to ' + from_email + ': ')
to_email = input('Enter reciever email address: ')

while True:
    try:
        hour_send_message = int(input('Enter the hour of day (24hr time) to send the message: '))
        break
    except:
        print('Enter an integer for the hour (min=0, max=24).')

while True:
    try:
        minute_send_message = int(input('Enter the minute of the hour to send the message: '))
        break
    except:
        print('Enter an integer for the minute (min=0, max=59).')

print('Working...')

subject = '[' + time.asctime()[0:10] + '] Good Morning'

time_local = time.asctime()
week_day = time_local[0:3]
month = time_local[4:7]

try:
    date = int(time_local[8:10])
except:
    date = int(time_local[9:10])

hour = int(time_local[11:13])
minute = int(time_local[14:16])
second = int(time_local[17:19])
year = int(time_local[20:])

if week_day == 'Mon':
    body = """\
    Today is Monday.
    Here is the agenda for today:
    
    Input Monday Schedule Here
    
    This is an automatic message sent from Python."""
elif week_day == 'Tue':
    body = """\
    Today is Tuesday.
    Here is the agenda for today:
    
    Input Tuesday Schedule Here
    
    This is an automatic message sent from Python."""
elif week_day == 'Wed':
    body = """\
    Today is Wednesday.
    Here is the agenda for today:
    
    Input Wednesday Schedule Here
    
    This is an automatic message sent from Python."""
elif week_day == 'Thu':
    body = """\
    Today is Thursday.
    Here is the agenda for today:
    
    Input Thursday Schedule Here
    
    This is an automatic message sent from Python."""
elif week_day == 'Fri':
    body = """\
    Today is Friday.
    Here is the agenda for today:
    
    Input Friday Schedule Here
    
    This is an automatic message sent from Python."""
elif week_day == 'Sat':
    body = """\
    Today is Saturday.
    Here is the agenda for today:
    
    Input Saturday Schedule Here
    
    This is an automatic message sent from Python."""
else:
    body = """\
    Today is Sunday.
    Here is the agenda for today:
    
    Input Sunday Schedule Here
    
    This is an automatic message sent from Python."""

message = MIMEMultipart("alternative")
message['Subject'] = subject
message['From'] = from_email
message['To'] = to_email

part1 = MIMEText(body, "plain")

message.attach(part1)

next_day = week_day

while True:

    time_local = time.asctime()
    week_day = time_local[0:3]
    month = time_local[4:7]
    
    try:
        date = int(time_local[8:10])
    except:
        date = int(time_local[9:10])
    
    hour = int(time_local[11:13])
    minute = int(time_local[14:16])
    second = int(time_local[17:19])
    year = int(time_local[20:])

    if hour == hour_send_message and minute == minute_send_message and week_day == next_day:
        context = ssl.create_default_context()
    
        with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
            server.login(from_email,password)
        
            server.sendmail(from_email,to_email,message.as_string())
        
        print('')
        print('Message sent on ' + time_local[0:10] + '.')
        
        next_day = next_week_day(next_day)
        
    time.sleep(30)