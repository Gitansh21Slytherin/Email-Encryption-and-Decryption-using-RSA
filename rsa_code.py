
from smtplib import SMTP
import smtplib

import config
subject = "Test subject"
##msg = "Hello there, how are you today?"
server = smtplib.SMTP('smtp.gmail.com',465)
##server.ehlo()
server.startssl()
server.login(config.EMAIL_ADDRESS, config.PASSWORD)
message = 'Subject: {}\n\n{}'.format(subject, msg)
server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
##server.quit()
print("Success: Email sent!")
