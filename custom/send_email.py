"""Program to generate restaurant list and send via email.
"""

import base64
import jinja2
import inspect
import os
import sys
import smtplib
import tempfile

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__author__ = 'rboodher@juniper.net'

MY_DIR = os.path.dirname(os.path.abspath(
    inspect.getsourcefile(inspect.currentframe())))

# Headers for email template
HEADERS = (
    'NAME',
    'ADDRESS',
    'AVERAGE COST FOR TWO',
    'RATING'
)

# AWS SES SMTP credentials
SMTP_CONFIG = {
    'username': 'smtp-user-name',
    'password': 'smtp-user-password',
    'host': 'email-smtp.ap-south-1.amazonaws.com',
    'port': 587,
}

def render_html(foodie_list):
    """ render html
    """

    with open(os.path.join(MY_DIR, 'email_template.j2'), 'r') as fh:
        return jinja2.Template(fh.read()).render(
            headers=HEADERS,
            foodie_list=foodie_list)

def send_email(email_addr, html):
    """ Send FOODIE restaurants list to the recipients.

    :return: None
    """
    sender = 'rboodher@gmail.com'
    recipients = email_addr

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipients
    msg['Subject'] = 'FOODIE Restaurant Report!'

    html_part = MIMEText(open(html).read(), 'html')
    msg.attach(html_part)

    mail_server = smtplib.SMTP(SMTP_CONFIG['host'], SMTP_CONFIG['port'])
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.ehlo()
    mail_server.login(SMTP_CONFIG['username'], SMTP_CONFIG['password'])
    mail_server.sendmail(sender, recipients.split(','), msg.as_string())
    mail_server.quit()

def send_foodie_list(email_addr, foodie_list):
    """generate report and send it.
    """
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            html = render_html(foodie_list)
            with open(tmpdir + '/' + 'foodies_list.html', 'w') as fh:
                fh.write(html)
            send_email(email_addr, tmpdir + '/' + 'foodies_list.html')
    except (IOError, OSError) as err:
        sys.exit()
