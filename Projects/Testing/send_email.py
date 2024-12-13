import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "sanjarbekwork@gmail.com"
receiver = "sanjarbeksocial@gmail.com"
password = "kdyz kunw qbot lwtg"

subject = "Test Email"
body = "Hello my friend"

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
    print("Email sent")
except smtplib.SMTPException as e:
    print(f"Error: {e}")
