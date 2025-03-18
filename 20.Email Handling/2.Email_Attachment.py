import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


Email_Sender = 'sreejith.techwingsys@gmail.com'
Email_Password = 'lebt vvis mjlm fkbz'

Email_Receiver = 'sreejith.techwingsys@gmail.com'

Subject = 'Wishes'

msg = """
Dear Sreejith,

Good Morning!
"""

em = MIMEMultipart()
em['From'] = Email_Sender
em['To'] = Email_Receiver
em['Subject'] = Subject
em.attach(MIMEText(msg, 'plain'))

filename = 'Python Assignment 1.pdf'

with open(filename, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='pdf')
    attachment.add_header('content-Disposition', _value='attachment', filename=filename)
    em.attach(attachment)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Email_Sender, Email_Password)
    smtp.sendmail(Email_Sender, Email_Receiver, em.as_string())


