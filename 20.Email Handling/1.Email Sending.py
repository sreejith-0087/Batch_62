from email.message import EmailMessage
import ssl #Secure Socket Layer
import smtplib  #Simple Mail Transfer Protocol


Email_Sender = 'sreejith.techwingsys@gmail.com'
Email_Password = 'lebt vvis mjlm fkbz'

Email_Receiver = 'sreejith.techwingsys@gmail.com'

Subject = 'Wishes'

msg = """
Dear Sreejith,

Good Morning!
"""

em = EmailMessage()
em['From'] = Email_Sender
em['To'] = Email_Receiver
em['Subject'] = Subject

em.set_content(msg)

con = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=con) as smtp:
    smtp.login(Email_Sender, Email_Password)
    smtp.sendmail(Email_Sender, Email_Receiver, em.as_string())
