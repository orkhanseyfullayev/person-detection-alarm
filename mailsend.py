from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import datetime

def mail_send(image_path):
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d  %H:%M:%S")

    subject = "ALARM!"
    message = f"Movement detected on camera!<br><br><img src='cid:image1'><br>Alarm Time: {formatted_time}"

    sender_email = "your_email@example.com" # Your email address
    password = "your_email_password" # Your email password
    send_to = "recipient@example.com" # Recipient email address

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = send_to

    msg.attach(MIMEText(message, 'html'))

    with open(image_path, 'rb') as file:
        img = MIMEImage(file.read())
        img.add_header('Content-ID', '<image1>')

    mail = SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(sender_email, password)
    mail.send_message(msg)
    mail.quit()
    print("Mail Sent!")

if __name__ == "__main__":
    mail_send('current_frame.jpg')
