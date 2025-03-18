import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


Email_Sender = 'sreejith.techwingsys@gmail.com'
Email_Password = 'lebt vvis mjlm fkbz'

Email_Receiver = 'sreejith.techwingsys@gmail.com'

Subject = 'Call Latter'

html_content = """
<html>
    <body>
        <h2 style="color:green;">Dear Name,</h2>
        <p style="color:pink;"><i>This is a response to your job application for the profile of  python/Django.</i></p>
    </body>
</html>
"""


em = MIMEMultipart()
em['From'] = Email_Sender
em['To'] = Email_Receiver
em['Subject'] = Subject

html_part = MIMEText(html_content, 'html')
em.attach(html_part)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Email_Sender, Email_Password)
    smtp.sendmail(Email_Sender, Email_Receiver, em.as_string())

