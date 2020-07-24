import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail(address_book, sender, subject, html, username, password):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ','.join(address_book)
    msg['Subject'] = subject
    # msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(html, 'html'))
    text = msg.as_string()
    # print text
    # Send the message via our SMTP server
    s = smtplib.SMTP("mail.posoco.in", 587)
    s.starttls()
    s.login(username, password)
    s.sendmail(sender, address_book, text)
    s.quit()


# address_book = ['rohitkumar@posoco.in']
# sender = 'nagasudhir@posoco.in'
# subject = "Message subject"
# html = "<h1>hello</h1><br/>How are you"
# s = smtplib.SMTP("mail.posoco.in", 587)
# s.starttls()
# username = r"NC\uname"
# password = 'pass'
# sendEmail(address_book, sender, subject, html, username, password)
