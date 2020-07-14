import smtplib
import getpass
from email.mime.text import MIMEText


def send_email():
    sender_address = 'abhayverma132000@gmail.com'
    password = getpass.getpass()
    subject = "Learn.Inspire.Grow."
    msg = '''
        Hello everyone!
        We are pleased to announce that we are going to start a new batch 
        of AI Mafia, Hope you will join!
        
        Thank you!
        Abhay verma
    '''
    # server initialization
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_address, password)

    # draft my message body
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = sender_address
    msg['To'] = 'abhayverma132000@gmail.com'
    recipients = ['abhayverma132000@gmail.com', 'abhayverma851@gmail.com']

    server.sendmail(sender_address, recipients, msg.as_string())


send_email()
