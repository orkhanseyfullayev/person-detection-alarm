from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import datetime

def mail_send(image_path):
    # Alarm zamanını al
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d  %H:%M:%S")  # Yıl-Ay-Gün Saat:Dakika:Saniye

    subject = "ALARM!"
    message = f"Kamerada haraket tespit edildi!<br><br><img src='cid:image1'><br>Alarm Zamanı: {formatted_time}"

    # SMTP sunucusu ve gönderici detayları
    myMailAdress = "muhtas2kouorkhan@gmail.com"
    password = "rqnh adnq dmtc ddui"
    sendTo = "orkhan.seyfullayev@gmail.com"

    # MIMEMultipart nesnesi oluştur
    msg = MIMEMultipart('related')  # 'related' alt-partları birbirine bağlamak için kullanılır
    msg['Subject'] = subject
    msg['From'] = myMailAdress
    msg['To'] = sendTo

    # E-posta metin içeriğini HTML olarak ekle
    msg.attach(MIMEText(message, 'html'))

    # Görüntüyü HTML içinde gömülü olarak ekle
    with open(image_path, 'rb') as file:
        img = MIMEImage(file.read())
        img.add_header('Content-ID', '<image1>')  # HTML içinde referans vermek için Content-ID kullan
        msg.attach(img)

    # SMTP sunucusu üzerinden giriş yap ve e-postayı gönder
    mail = SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(myMailAdress, password)
    mail.send_message(msg)
    mail.quit()
    print("Mail Sent!")

if __name__ == "__main__":
    mail_send('current_frame.jpg')  # Görüntü dosyasının yolu




# password'u: Google App Passwords bölümündenelde ettim. Linki:
# https://myaccount.google.com/u/3/apppasswords?rapt=AEjHL4OXzU-0hh3ZgDVsYP4DeHKE38JMQEbdb-53rZr-NVAm3lgwORe-1bsrnVvz373EBm776NpSHDm9ps8Cpo_A3EG6dgyxksgJyRuUjcICn9exZXCuLqg