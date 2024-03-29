import smtplib
import json


class Mailer:
    

    def log_in(self):
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()

            self.server.login(self.sender_gmail, self.gmail_password)
        except smtplib.SMTPAuthenticationError:
            print('Email or password is wrong. System couldn\'t log into smtp server.')
            exit(3)

    def send_mail(self, url, product_name, price):
        subject = 'Price Fell Down!'
        tr2_eng = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
        body = f"{product_name} is cheaper now. Check the link below: \n{url}".translate(
            tr2_eng)

        msg = f"Subject: {subject}\n\n{body}"

        self.server.sendmail(self.sender_gmail, self.receiver_email, msg)
        print(
            f'An email has been sent for {product_name} when its price is {price}.')

    def log_out(self):
        self.server.quit()