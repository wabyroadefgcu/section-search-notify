#!/usr/bin/env python3

import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser

# Make sure to have a secret_config.txt file in the root folder of this project.
# See secret_config_example.txt for format.
config = configparser.ConfigParser()
config.read("secret_config.txt");

# Load all secret data into variables - make sure all listed variables are included in secret_config.txt
mail_server = config.get("configuration","mail_server");
mail_server_port = config.get("configuration","mail_server_port");
from_addr = config.get("configuration","from_addr");
password = config.get("configuration","password");
to_addr = config.get("configuration","to_addr");

def email_section_list(subject, body):
    """ set up the message"""
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    now = datetime.now()
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))


    # Connect to the server, authenticate and send message. May need to change account security
    # options to allow this.
    server = smtplib.SMTP(mail_server, mail_server_port)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()
    return 0
